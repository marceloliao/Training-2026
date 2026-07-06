#!/usr/bin/env python3
"""
Organize photos into folders by capture date (YYYY-MM-DD).

Scans a parent folder and all subfolders, reads EXIF dates when available,
and moves images into: <parent>/organized_by_date/<YYYY-MM-DD>/

Requires: pip install Pillow
"""

from __future__ import annotations

import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

try:
    from PIL import Image
    from PIL.ExifTags import Base as ExifBase
except ImportError:
    print("Missing dependency. Install with: pip install Pillow")
    sys.exit(1)

# Common photo/video extensions (videos use file mtime if no EXIF)
IMAGE_EXTENSIONS = {
    ".jpg",
    ".jpeg",
    ".jpe",
    ".png",
    ".gif",
    ".bmp",
    ".tif",
    ".tiff",
    ".webp",
    ".heic",
    ".heif",
    ".hif",
    ".raw",
    ".cr2",
    ".nef",
    ".arw",
    ".dng",
    ".orf",
    ".rw2",
}

VIDEO_EXTENSIONS = {
    ".mp4",
    ".mov",
    ".avi",
    ".mkv",
    ".m4v",
    ".wmv",
    ".3gp",
}

MEDIA_EXTENSIONS = IMAGE_EXTENSIONS | VIDEO_EXTENSIONS

OUTPUT_DIR_NAME = "organized_by_date"
DATE_FOLDER_PATTERN = re.compile(r"^\d{4}-\d{2}-\d{2}$")

EXIF_DATETIME_TAGS = (
    ExifBase.DateTimeOriginal,
    ExifBase.DateTimeDigitized,
    ExifBase.DateTime,
)


def parse_exif_datetime(value: object) -> datetime | None:
    if value is None:
        return None
    if isinstance(value, bytes):
        try:
            value = value.decode("utf-8", errors="replace").strip("\x00")
        except Exception:
            return None
    if not isinstance(value, str):
        return None
    value = value.strip()
    for fmt in ("%Y:%m:%d %H:%M:%S", "%Y-%m-%d %H:%M:%S"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


def get_capture_datetime(path: Path) -> datetime:
    """Best-effort capture date: EXIF first, then file modification time."""
    if path.suffix.lower() in IMAGE_EXTENSIONS:
        try:
            with Image.open(path) as img:
                exif = img.getexif()
                if exif:
                    for tag in EXIF_DATETIME_TAGS:
                        dt = parse_exif_datetime(exif.get(tag))
                        if dt:
                            return dt
        except Exception:
            pass

    stat = path.stat()
    return datetime.fromtimestamp(stat.st_mtime)


def unique_destination(folder: Path, filename: str) -> Path:
    dest = folder / filename
    if not dest.exists():
        return dest
    stem = Path(filename).stem
    suffix = Path(filename).suffix
    n = 1
    while True:
        candidate = folder / f"{stem}_{n}{suffix}"
        if not candidate.exists():
            return candidate
        n += 1


def should_skip_path(path: Path, parent: Path, output_root: Path) -> bool:
    try:
        rel = path.relative_to(parent)
    except ValueError:
        return True
    parts = rel.parts
    if parts and parts[0] == OUTPUT_DIR_NAME:
        return True
    if path == output_root or output_root in path.parents:
        return True
    return False


def collect_media_files(parent: Path, output_root: Path) -> list[Path]:
    files: list[Path] = []
    for path in parent.rglob("*"):
        if not path.is_file():
            continue
        if path.suffix.lower() not in MEDIA_EXTENSIONS:
            continue
        if should_skip_path(path, parent, output_root):
            continue
        files.append(path)
    return sorted(files)


def prompt_parent_folder() -> Path:
    print("Photo organizer — sort by capture date")
    print(f"Output will be created under: {OUTPUT_DIR_NAME}/YYYY-MM-DD/")
    print()
    while True:
        raw = input("Enter parent folder path: ").strip().strip('"').strip("'")
        if not raw:
            print("Please enter a path.")
            continue
        folder = Path(raw).expanduser().resolve()
        if not folder.exists():
            print(f"Not found: {folder}")
            continue
        if not folder.is_dir():
            print(f"Not a folder: {folder}")
            continue
        return folder


def prompt_move_or_copy() -> str:
    while True:
        choice = input("Move files (m) or copy files (c)? [m]: ").strip().lower()
        if choice in ("", "m", "move"):
            return "move"
        if choice in ("c", "copy"):
            return "copy"
        print("Enter 'm' for move or 'c' for copy.")


def main() -> int:
    parent = prompt_parent_folder()
    action = prompt_move_or_copy()
    output_root = parent / OUTPUT_DIR_NAME
    output_root.mkdir(parents=True, exist_ok=True)

    media_files = collect_media_files(parent, output_root)
    if not media_files:
        print("No photos or videos found in that folder tree.")
        return 0

    print(f"\nFound {len(media_files)} file(s). Processing...\n")

    moved = 0
    errors = 0
    unknown_date = 0

    for src in media_files:
        try:
            taken = get_capture_datetime(src)
            date_label = taken.strftime("%Y-%m-%d")
        except OSError as exc:
            print(f"  SKIP (read error): {src} — {exc}")
            errors += 1
            continue

        if date_label == "1970-01-01":
            unknown_date += 1

        dest_dir = output_root / date_label
        dest_dir.mkdir(parents=True, exist_ok=True)
        dest = unique_destination(dest_dir, src.name)

        if dest.resolve() == src.resolve():
            continue

        try:
            if action == "move":
                shutil.move(str(src), str(dest))
            else:
                shutil.copy2(str(src), str(dest))
            print(f"  {date_label}  <-  {src.relative_to(parent)}")
            moved += 1
        except OSError as exc:
            print(f"  ERROR: {src} — {exc}")
            errors += 1

    print()
    print("Done.")
    print(f"  {'Moved' if action == 'move' else 'Copied'}: {moved}")
    if errors:
        print(f"  Errors: {errors}")
    if unknown_date:
        print(
            f"  Note: {unknown_date} file(s) used file modification time "
            "(no EXIF date found)."
        )
    print(f"  Output: {output_root}")
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
