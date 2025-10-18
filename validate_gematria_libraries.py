#!/usr/bin/env python3
"""
Validation script for gematria libraries.

This script validates that:
1. All required library files exist
2. Each library contains valid JSON
3. Entries have required fields (hebrew, transliteration, gematria, english)
4. Gematria values are correctly calculated
5. Entries are sorted by gematria value
"""

import json
import os
import sys

# Hebrew letter to gematria value mapping (standard values)
GEMATRIA_VALUES = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
    'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90,
    'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
}

REQUIRED_LIBRARIES = [
    'A_library.json',
    'alpha_library.json',
    'kappa_library.json',
    'N_library.json',
    'k_library.json',
    'd_library.json',
    'w_library.json',
    's_library.json',
    'I_library.json',
    'F_library.json',
    'D_library.json',
    'Delta_library.json',
    'R_library.json',
    'Sigma_library.json',
    'Lambda_library.json',
    'beta_library.json'
]

def calculate_gematria(hebrew_text: str) -> int:
    """Calculate the gematria value of Hebrew text."""
    return sum(GEMATRIA_VALUES.get(char, 0) for char in hebrew_text)

def validate_library(filepath: str) -> tuple:
    """Validate a single library file. Returns (success, errors)."""
    errors = []
    
    # Check file exists
    if not os.path.exists(filepath):
        return False, [f"File does not exist: {filepath}"]
    
    # Check valid JSON
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        return False, [f"Invalid JSON: {e}"]
    except Exception as e:
        return False, [f"Error reading file: {e}"]
    
    # Check it's a list
    if not isinstance(data, list):
        return False, ["Root element must be an array"]
    
    # Check each entry
    prev_gematria = -1
    for i, entry in enumerate(data):
        # Check required fields
        if not isinstance(entry, dict):
            errors.append(f"Entry {i} is not an object")
            continue
        
        required_fields = ['hebrew', 'transliteration', 'gematria', 'english']
        missing = [f for f in required_fields if f not in entry]
        if missing:
            errors.append(f"Entry {i} missing fields: {missing}")
            continue
        
        # Validate gematria calculation
        hebrew = entry['hebrew']
        stated_gematria = entry['gematria']
        calculated_gematria = calculate_gematria(hebrew)
        
        if calculated_gematria != stated_gematria:
            errors.append(
                f"Entry {i} ({hebrew}): gematria mismatch - "
                f"stated {stated_gematria}, calculated {calculated_gematria}"
            )
        
        # Check sorting
        if stated_gematria < prev_gematria:
            errors.append(
                f"Entry {i} ({hebrew}): not sorted - "
                f"gematria {stated_gematria} comes after {prev_gematria}"
            )
        prev_gematria = stated_gematria
    
    return len(errors) == 0, errors

def main():
    """Main validation function."""
    print("Validating gematria libraries...\n")
    
    all_valid = True
    total_entries = 0
    
    for library_name in REQUIRED_LIBRARIES:
        filepath = os.path.join('gematria_libraries', library_name)
        success, errors = validate_library(filepath)
        
        if success:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
                entry_count = len(data)
                total_entries += entry_count
                print(f"✓ {library_name:25s} - {entry_count:5d} entries - VALID")
        else:
            all_valid = False
            print(f"✗ {library_name:25s} - INVALID")
            for error in errors[:5]:  # Show first 5 errors
                print(f"    {error}")
            if len(errors) > 5:
                print(f"    ... and {len(errors) - 5} more errors")
    
    print(f"\n{'='*60}")
    print(f"Total entries across all libraries: {total_entries:,}")
    
    if all_valid:
        print("\n✓ All libraries are valid!")
        return 0
    else:
        print("\n✗ Some libraries have errors")
        return 1

if __name__ == '__main__':
    sys.exit(main())
