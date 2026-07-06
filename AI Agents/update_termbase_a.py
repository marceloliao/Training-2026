#!/usr/bin/env python3
"""Merge French terms from Termbase_B.xml into Termbase_A.xml."""

import copy
import xml.etree.ElementTree as ET
from pathlib import Path

START_UNMATCHED_ID = 5278
TERMBASE_A = Path(__file__).parent / "Termbase_A.xml"
TERMBASE_B = Path(__file__).parent / "Termbase_B.xml"


def is_english_language(language_elem: ET.Element) -> bool:
  """True when the language group is English (type attribute)."""
  return (language_elem.get("type") or "").strip().lower() == "english"


def is_french_language(language_elem: ET.Element) -> bool:
  """True when the language group is French with lang=FR."""
  return (language_elem.get("lang") or "").strip().upper() == "FR"


def get_english_terms(concept_grp: ET.Element) -> list[str]:
  terms: list[str] = []
  for language_grp in concept_grp.findall("languageGrp"):
    language = language_grp.find("language")
    if language is None or not is_english_language(language):
      continue
    for term_grp in language_grp.findall("termGrp"):
      term = term_grp.find("term")
      if term is not None and term.text is not None:
        terms.append(term.text.strip())
  return terms


def get_fr_language_grp(concept_grp: ET.Element) -> ET.Element | None:
  for language_grp in concept_grp.findall("languageGrp"):
    language = language_grp.find("language")
    if language is not None and is_french_language(language):
      return language_grp
  return None


def remove_fr_language_grp(concept_grp: ET.Element) -> None:
  for language_grp in list(concept_grp.findall("languageGrp")):
    language = language_grp.find("language")
    if language is not None and is_french_language(language):
      concept_grp.remove(language_grp)


def build_term_to_concept_grp_map(root: ET.Element) -> dict[str, ET.Element]:
  term_map: dict[str, ET.Element] = {}
  for concept_grp in root.findall("conceptGrp"):
    for term in get_english_terms(concept_grp):
      term_map[term] = concept_grp
  return term_map


def find_matching_concept_grp(
  terms: list[str], term_map: dict[str, ET.Element]
) -> ET.Element | None:
  for term in terms:
    if term in term_map:
      return term_map[term]
  return None


def main() -> None:
  tree_a = ET.parse(TERMBASE_A)
  tree_b = ET.parse(TERMBASE_B)
  root_a = tree_a.getroot()

  term_map = build_term_to_concept_grp_map(root_a)

  next_unmatched_id = START_UNMATCHED_ID
  matched = 0
  unmatched = 0
  skipped_no_fr = 0

  for concept_grp_b in tree_b.getroot().findall("conceptGrp"):
    fr_language_grp = get_fr_language_grp(concept_grp_b)
    if fr_language_grp is None:
      skipped_no_fr += 1
      continue

    english_terms = get_english_terms(concept_grp_b)
    matched_concept_grp = find_matching_concept_grp(english_terms, term_map)

    if matched_concept_grp is not None:
      remove_fr_language_grp(matched_concept_grp)
      matched_concept_grp.append(copy.deepcopy(fr_language_grp))
      matched += 1
    else:
      new_concept_grp = copy.deepcopy(concept_grp_b)
      concept_elem = new_concept_grp.find("concept")
      if concept_elem is not None:
        concept_elem.text = str(next_unmatched_id)
        next_unmatched_id += 1
      root_a.append(new_concept_grp)
      for term in english_terms:
        term_map[term] = new_concept_grp
      unmatched += 1

  tree_a.write(TERMBASE_A, encoding="unicode", xml_declaration=False)

  print(f"Processed {matched + unmatched + skipped_no_fr} conceptGrp elements from Termbase_B")
  print(f"  Matched (FR languageGrp copied): {matched}")
  print(f"  Unmatched (conceptGrp appended, IDs {START_UNMATCHED_ID}+): {unmatched}")
  print(f"  Skipped (no FR languageGrp in Termbase_B): {skipped_no_fr}")
  print(f"  Next unused ID would be: {next_unmatched_id}")
  print(f"Updated {TERMBASE_A}")


if __name__ == "__main__":
  main()
