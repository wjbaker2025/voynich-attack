#!/usr/bin/env python3
"""
Example usage of the populated gematria libraries.

This script demonstrates how to:
1. Load and query gematria libraries
2. Find words by gematria value
3. Search for specific Hebrew words
4. Calculate gematria for custom Hebrew text
"""

import json
from typing import List, Dict
from gematria_utils import calculate_gematria

def load_library(library_name: str) -> List[Dict]:
    """Load a gematria library."""
    with open(f'gematria_libraries/{library_name}', 'r', encoding='utf-8') as f:
        return json.load(f)

def find_by_gematria(library: List[Dict], value: int) -> List[Dict]:
    """Find all words in a library with a specific gematria value."""
    return [entry for entry in library if entry['gematria'] == value]

def find_by_hebrew(library: List[Dict], hebrew: str) -> Dict:
    """Find a word in a library by its Hebrew spelling."""
    for entry in library:
        if entry['hebrew'] == hebrew:
            return entry
    return None

def search_english(library: List[Dict], keyword: str) -> List[Dict]:
    """Search for words by English meaning."""
    keyword_lower = keyword.lower()
    return [entry for entry in library if keyword_lower in entry.get('english', '').lower()]

# Example 1: Load the Faith library and explore it
print("=" * 60)
print("Example 1: Exploring the Faith Library")
print("=" * 60)

faith_lib = load_library('F_library.json')
print(f"\nTotal entries in Faith library: {len(faith_lib)}")

# Show some entries
print("\nSample entries:")
for entry in faith_lib[100:105]:
    print(f"  {entry['hebrew']:15s} [{entry['gematria']:4d}] - {entry['english']}")

# Example 2: Find all words with a specific gematria value
print("\n" + "=" * 60)
print("Example 2: Finding Words by Gematria Value")
print("=" * 60)

target_value = 26  # YHVH = יהוה = 10+5+6+5 = 26
print(f"\nSearching for words with gematria value {target_value}...")

# Search across multiple libraries
libraries_to_search = ['k_library.json', 'F_library.json', 'Sigma_library.json']
for lib_name in libraries_to_search:
    lib = load_library(lib_name)
    matches = find_by_gematria(lib, target_value)
    if matches:
        print(f"\n{lib_name}:")
        for match in matches[:3]:  # Show first 3
            print(f"  {match['hebrew']:15s} - {match['english']}")

# Example 3: Calculate gematria for custom text
print("\n" + "=" * 60)
print("Example 3: Calculating Gematria for Custom Hebrew Text")
print("=" * 60)

test_words = {
    'אמת': 'truth (emet)',
    'אהבה': 'love (ahavah)',
    'חכמה': 'wisdom (chokmah)',
    'שלום': 'peace (shalom)'
}

print("\nGematria calculations:")
for hebrew, meaning in test_words.items():
    value = calculate_gematria(hebrew)
    print(f"  {hebrew:10s} = {value:4d}  ({meaning})")

# Example 4: Search by English meaning
print("\n" + "=" * 60)
print("Example 4: Searching by English Meaning")
print("=" * 60)

knowledge_lib = load_library('k_library.json')
wisdom_words = search_english(knowledge_lib, 'wisdom')
print(f"\nFound {len(wisdom_words)} words containing 'wisdom':")
for word in wisdom_words[:5]:  # Show first 5
    print(f"  {word['hebrew']:15s} [{word['gematria']:4d}] - {word['english']}")

# Example 5: Compare concepts across libraries
print("\n" + "=" * 60)
print("Example 5: Comparing Gematria Ranges Across Concepts")
print("=" * 60)

library_stats = {}
library_names = {
    'A_library.json': 'Adeptship',
    'k_library.json': 'Knowledge',
    'F_library.json': 'Faith',
    'd_library.json': 'Courage',
    's_library.json': 'Silence'
}

print("\nGematria value ranges:")
for lib_file, concept in library_names.items():
    lib = load_library(lib_file)
    if lib:
        values = [e['gematria'] for e in lib]
        print(f"  {concept:15s}: {min(values):4d} - {max(values):4d}  "
              f"(avg: {sum(values)//len(values):4d}, count: {len(lib)})")

# Example 6: Find overlapping gematria values
print("\n" + "=" * 60)
print("Example 6: Finding Overlapping Gematria Values")
print("=" * 60)

# Load two conceptually related libraries
truth_lib = load_library('Sigma_library.json')  # Signal Integrity (truth)
lies_lib = load_library('Lambda_library.json')  # Astral Noise (falsehood)

# Find gematria values that appear in both
truth_values = {e['gematria'] for e in truth_lib}
lies_values = {e['gematria'] for e in lies_lib}
overlap = truth_values & lies_values

print(f"\nFound {len(overlap)} gematria values that appear in both Truth and Lies libraries")
print("Example overlapping value (105):")

if 105 in overlap:
    truth_105 = find_by_gematria(truth_lib, 105)
    lies_105 = find_by_gematria(lies_lib, 105)
    
    print("\n  Truth/Integrity words with gematria 105:")
    for word in truth_105[:2]:
        print(f"    {word['hebrew']:15s} - {word['english']}")
    
    print("\n  Falsehood words with gematria 105:")
    for word in lies_105[:2]:
        print(f"    {word['hebrew']:15s} - {word['english']}")

print("\n" + "=" * 60)
print("Examples complete!")
print("=" * 60)
