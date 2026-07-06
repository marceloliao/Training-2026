#!/usr/bin/env python3
"""Update concept IDs in Termbase_B.xml by matching English terms against Termbase_A.xml."""

import xml.etree.ElementTree as ET
from pathlib import Path

START_UNMATCHED_ID = 5278
TERMBASE_A = Path(__file__).parent / "Termbase_A.xml"
TERMBASE_B = Path(__file__).parent / "Termbase_B.xml"


def is_english_language(language_elem: ET.Element) -> bool:
    """True when the language group is English (type attribute)."""
    return (language_elem.get("type") or "").strip().lower() == "english"


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


def build_term_to_concept_map(root: ET.Element) -> dict[str, str]:
    term_map: dict[str, str] = {}
    for concept_grp in root.findall("conceptGrp"):
        concept_elem = concept_grp.find("concept")
        if concept_elem is None or concept_elem.text is None:
            continue
        concept_id = concept_elem.text.strip()
        for term in get_english_terms(concept_grp):
            term_map[term] = concept_id
    return term_map


def find_matching_concept(terms: list[str], term_map: dict[str, str]) -> str | None:
    for term in terms:
        if term in term_map:
            return term_map[term]
    return None


def main() -> None:
    tree_a = ET.parse(TERMBASE_A)
    tree_b = ET.parse(TERMBASE_B)

    term_map = build_term_to_concept_map(tree_a.getroot())

    next_unmatched_id = START_UNMATCHED_ID
    matched = 0
    unmatched = 0

    for concept_grp in tree_b.getroot().findall("conceptGrp"):
        concept_elem = concept_grp.find("concept")
        if concept_elem is None:
            continue

        english_terms = get_english_terms(concept_grp)
        matched_concept = find_matching_concept(english_terms, term_map)

        if matched_concept is not None:
            concept_elem.text = matched_concept
            matched += 1
        else:
            concept_elem.text = str(next_unmatched_id)
            next_unmatched_id += 1
            unmatched += 1

    tree_b.write(TERMBASE_B, encoding="unicode", xml_declaration=False)

    print(f"Processed {matched + unmatched} conceptGrp elements")
    print(f"  Matched (from Termbase_A): {matched}")
    print(f"  Unmatched (assigned {START_UNMATCHED_ID}+): {unmatched}")
    print(f"  Next unused ID would be: {next_unmatched_id}")
    print(f"Updated {TERMBASE_B}")


if __name__ == "__main__":
    main()
