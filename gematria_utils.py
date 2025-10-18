"""
Shared utilities for gematria calculations and Hebrew text processing.

This module provides common functions and constants used across
the gematria library scripts.
"""

# Hebrew letter to gematria value mapping (standard values)
GEMATRIA_VALUES = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
    'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90,
    'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
}

# Set of valid Hebrew letters (consonants only)
HEBREW_LETTERS = set(GEMATRIA_VALUES.keys())

def strip_diacritics(hebrew_text: str) -> str:
    """
    Remove vowel points, cantillation marks, and non-Hebrew characters from Hebrew text.
    
    Args:
        hebrew_text: Hebrew text that may contain diacritical marks
        
    Returns:
        Clean Hebrew text with only consonant letters (א-ת)
    """
    return ''.join(char for char in hebrew_text if char in HEBREW_LETTERS)

def calculate_gematria(hebrew_text: str) -> int:
    """
    Calculate the gematria value of Hebrew text using standard values.
    
    Automatically strips diacritical marks before calculation.
    
    Args:
        hebrew_text: Hebrew text (may contain vowel points and cantillation)
        
    Returns:
        Integer gematria value
        
    Example:
        >>> calculate_gematria('אמת')  # truth (emet)
        441
        >>> calculate_gematria('שָׁלוֹם')  # peace (shalom) with diacritics
        376
    """
    clean_text = strip_diacritics(hebrew_text)
    return sum(GEMATRIA_VALUES.get(char, 0) for char in clean_text)
