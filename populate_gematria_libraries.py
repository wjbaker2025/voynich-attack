#!/usr/bin/env python3
"""
Script to populate gematria libraries from the Hebrew Tanach.

This script searches through all books of the Hebrew Tanach to find words
semantically related to various thematic concepts, calculates their gematria
values, and populates the corresponding library JSON files.
"""

import json
import os
import re
from collections import defaultdict
from typing import Dict, List, Tuple, Set

# Hebrew letter to gematria value mapping (standard values)
GEMATRIA_VALUES = {
    'א': 1, 'ב': 2, 'ג': 3, 'ד': 4, 'ה': 5, 'ו': 6, 'ז': 7, 'ח': 8, 'ט': 9,
    'י': 10, 'כ': 20, 'ך': 20, 'ל': 30, 'מ': 40, 'ם': 40, 'נ': 50, 'ן': 50,
    'ס': 60, 'ע': 70, 'פ': 80, 'ף': 80, 'צ': 90, 'ץ': 90,
    'ק': 100, 'ר': 200, 'ש': 300, 'ת': 400
}

def strip_diacritics(hebrew_text: str) -> str:
    """Remove vowel points, cantillation marks, and non-Hebrew characters from Hebrew text."""
    # Hebrew vowel points and cantillation marks range: U+0591 to U+05C7
    # Keep only Hebrew letters (U+05D0 to U+05EA)
    hebrew_letters = set('אבגדהוזחטיכךלמםנןסעפףצץקרשת')
    return ''.join(char for char in hebrew_text if char in hebrew_letters)

def calculate_gematria(hebrew_text: str) -> int:
    """Calculate the gematria value of Hebrew text."""
    clean_text = strip_diacritics(hebrew_text)
    return sum(GEMATRIA_VALUES.get(char, 0) for char in clean_text)

def load_tanach_books() -> Dict[str, Dict]:
    """Load all Tanach books from JSON files."""
    tanach_dir = 'reference_materials/the_hebrew_holy_bible-tanach'
    books = {}
    
    for filename in os.listdir(tanach_dir):
        if filename.endswith('.json') and filename != 'README.md':
            filepath = os.path.join(tanach_dir, filename)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    books[filename] = data
            except Exception as e:
                print(f"Error loading {filename}: {e}")
    
    return books

def extract_words_from_tanach(books: Dict) -> List[Dict]:
    """Extract all unique Hebrew words with their English meanings from all Tanach books."""
    words_dict = {}  # Use dict to avoid duplicates by Hebrew word
    
    for book_filename, book_data in books.items():
        # Get the first (and typically only) book name key
        book_name = list(book_data.keys())[0]
        book_content = book_data[book_name]
        
        if 'chapters' not in book_content:
            continue
            
        chapters = book_content['chapters']
        
        for chapter_num, verses in chapters.items():
            for verse_num, words in verses.items():
                if not isinstance(words, list):
                    continue
                    
                for word_data in words:
                    if not isinstance(word_data, dict):
                        continue
                        
                    hebrew = word_data.get('hebrew', '')
                    english = word_data.get('english', '')
                    strongs = word_data.get('strongs', '')
                    
                    if not hebrew:
                        continue
                    
                    # Strip diacritics for the key to merge similar words
                    clean_hebrew = strip_diacritics(hebrew)
                    
                    # Skip if nothing left after cleaning
                    if not clean_hebrew:
                        continue
                    
                    # Store unique words
                    if clean_hebrew not in words_dict:
                        words_dict[clean_hebrew] = {
                            'hebrew': hebrew,  # Keep original with diacritics for display
                            'clean_hebrew': clean_hebrew,
                            'english': english,
                            'strongs': strongs,
                            'gematria': calculate_gematria(hebrew)
                        }
                    elif english and not words_dict[clean_hebrew]['english']:
                        # Update English if we didn't have it before
                        words_dict[clean_hebrew]['english'] = english
    
    return list(words_dict.values())

# Thematic keyword sets for each library (based on AGENTS.md)
# Expanded with more comprehensive semantic coverage
THEMATIC_KEYWORDS = {
    'A_library': {  # Adeptship - mastery, skill, expertise
        'keywords': [
            'master', 'expert', 'chief', 'head', 'skilled', 'wise', 'wisdom',
            'understanding', 'knowledge', 'skill', 'cunning', 'craftsman',
            'artisan', 'excellent', 'prince', 'leader', 'mastery', 'intelligent',
            'discerning', 'prudent', 'sage', 'elder', 'teacher', 'instructor',
            'captain', 'ruler', 'governor', 'overseer', 'superintendent',
            'wise-hearted', 'skilled worker', 'competent', 'ability', 'able',
            'proficient', 'adept', 'learned', 'enlightened', 'scholar'
        ]
    },
    'alpha_library': {  # Skill Constant - skill, craft, workmanship
        'keywords': [
            'skill', 'work', 'deed', 'craft', 'workmanship', 'craftsmanship',
            'handiwork', 'labor', 'service', 'device', 'instrument', 'tool',
            'vessel', 'make', 'build', 'create', 'form', 'fashion', 'design',
            'doing', 'practice', 'operation', 'production', 'construction',
            'fabricate', 'manufacture', 'artisan', 'wrought', 'made', 'works',
            'cunning work', 'skillful work', 'occupation', 'task', 'business',
            'craft', 'art', 'handicraft', 'technique', 'method'
        ]
    },
    'kappa_library': {  # Efficiency Constant - speed, directness, effectiveness
        'keywords': [
            'swift', 'quick', 'haste', 'speed', 'diligent', 'straight', 'upright',
            'right', 'success', 'prosper', 'flourish', 'advance', 'direct',
            'accomplish', 'complete', 'finish', 'perfect', 'effective',
            'hasten', 'hurry', 'rapid', 'expedite', 'immediate', 'prompt',
            'forthwith', 'speedily', 'suddenly', 'at once', 'straightway',
            'efficient', 'productive', 'fruitful', 'thrive', 'prevail',
            'succeed', 'achieve', 'attain', 'fulfill', 'realize'
        ]
    },
    'N_library': {  # Collective Force - groups, assemblies, collectives
        'keywords': [
            'nation', 'people', 'assembly', 'congregation', 'multitude', 'host',
            'army', 'troop', 'company', 'tribe', 'family', 'community', 'all',
            'together', 'gather', 'unite', 'unity', 'whole', 'entire',
            'peoples', 'nations', 'tribes', 'families', 'kindred', 'clan',
            'band', 'group', 'gathering', 'council', 'meeting', 'throng',
            'crowd', 'mass', 'collection', 'body', 'force', 'legion',
            'assembled', 'united', 'collective', 'common', 'general'
        ]
    },
    'k_library': {  # To Know - knowledge, understanding, wisdom
        'keywords': [
            'know', 'knowledge', 'wisdom', 'understanding', 'perceive', 'see',
            'discern', 'insight', 'learn', 'teach', 'instruct', 'aware',
            'recognize', 'comprehend', 'realize', 'consider', 'regard',
            'known', 'knew', 'knowing', 'acquainted', 'familiar', 'informed',
            'conscious', 'cognizant', 'enlightened', 'educated', 'learned',
            'discovered', 'revealed', 'understood', 'grasped', 'apprehended',
            'perceived', 'observed', 'noted', 'marked', 'distinguished'
        ]
    },
    'd_library': {  # To Dare - courage, bravery, boldness
        'keywords': [
            'courage', 'strong', 'mighty', 'bold', 'brave', 'valiant', 'warrior',
            'hero', 'fearless', 'not afraid', 'fear not', 'strengthen', 'power',
            'force', 'valor', 'fortitude', 'courageous', 'daring', 'intrepid',
            'dauntless', 'undaunted', 'heroic', 'gallant', 'stalwart', 'stout',
            'resolute', 'determined', 'steadfast', 'unwavering', 'firm',
            'venture', 'risk', 'challenge', 'confront', 'face', 'defy'
        ]
    },
    'w_library': {  # To Will - will, desire, volition, purpose
        'keywords': [
            'will', 'desire', 'choose', 'willing', 'consent', 'purpose', 'intent',
            'heart', 'delight', 'pleasure', 'wish', 'want', 'incline', 'favor',
            'goodwill', 'accept', 'choice', 'elect', 'select', 'prefer',
            'determination', 'resolve', 'decision', 'mind', 'soul', 'spirit',
            'longing', 'yearning', 'craving', 'appetite', 'aspiration',
            'volition', 'intention', 'aim', 'goal', 'plan', 'design'
        ]
    },
    's_library': {  # To Keep Silent - silence, quiet, stillness, secrecy
        'keywords': [
            'silence', 'silent', 'quiet', 'still', 'stillness', 'peace', 'rest',
            'calm', 'hush', 'secret', 'hide', 'conceal', 'restrain', 'cease',
            'keep silence', 'hold peace', 'speechless', 'mute', 'dumb',
            'tacit', 'unspoken', 'wordless', 'soundless', 'noiseless',
            'tranquil', 'serene', 'placid', 'peaceful', 'composed',
            'hidden', 'veiled', 'covered', 'obscured', 'clandestine',
            'covert', 'private', 'confidential', 'undisclosed'
        ]
    },
    'I_library': {  # Imagination - forming mental images, devising, planning
        'keywords': [
            'imagination', 'imagine', 'form', 'device', 'thought', 'think',
            'vision', 'dream', 'devise', 'plan', 'purpose', 'intent', 'frame',
            'inclination', 'meditation', 'consider', 'ponder', 'contrive',
            'conceive', 'envision', 'visualize', 'picture', 'fancy',
            'invent', 'create', 'fabricate', 'construct', 'design',
            'scheme', 'plot', 'project', 'blueprint', 'conception',
            'idea', 'notion', 'concept', 'mental', 'mind', 'heart'
        ]
    },
    'F_library': {  # Faith - belief, trust, faithfulness
        'keywords': [
            'faith', 'believe', 'trust', 'faithful', 'faithfulness', 'hope',
            'confidence', 'rely', 'depend', 'sure', 'firm', 'steadfast', 'amen',
            'truth', 'true', 'establish', 'certain', 'belief', 'believing',
            'trustworthy', 'reliable', 'dependable', 'loyal', 'devoted',
            'committed', 'dedicated', 'constant', 'stable', 'secure',
            'assurance', 'conviction', 'certitude', 'credence', 'reliance'
        ]
    },
    'D_library': {  # Disturbance - chaos, turmoil, confusion
        'keywords': [
            'trouble', 'tremble', 'shake', 'quake', 'rage', 'noise', 'tumult',
            'storm', 'tempest', 'whirlwind', 'terror', 'confusion', 'chaos',
            'turmoil', 'uproar', 'commotion', 'disturb', 'dismay', 'distress',
            'agitate', 'perturb', 'disquiet', 'unsettle', 'upset', 'disorder',
            'disarray', 'turbulence', 'upheaval', 'convulsion', '震', '震動',
            'raging', 'roar', 'thunder', 'earthquake', 'trembling', 'shaking',
            'fear', 'dread', 'panic', 'alarm', 'fright', 'horror'
        ]
    },
    'Delta_library': {  # Diaphane - clarity, purity, transparency, brightness
        'keywords': [
            'clear', 'pure', 'light', 'bright', 'shine', 'shining', 'crystal',
            'clean', 'clarity', 'transparent', 'radiant', 'brilliant', 'splendor',
            'glory', 'luminous', 'white', 'purify', 'refine', 'gleam', 'glitter',
            'sparkle', 'glisten', 'shimmer', 'glow', 'illuminate', 'brighten',
            'enlighten', 'lucid', 'limpid', 'pellucid', 'translucent',
            'unclouded', 'unblemished', 'spotless', 'stainless', 'immaculate',
            'pristine', 'cleanse', 'wash', 'purge', 'lustrous', 'resplendent'
        ]
    },
    'R_library': {  # Resonance - response, connection, vibration
        'keywords': [
            'answer', 'voice', 'sound', 'call', 'respond', 'echo', 'shout',
            'song', 'sing', 'cry', 'hear', 'listen', 'heart', 'proclaim',
            'declare', 'speak', 'utter', 'resound', 'reply', 'response',
            'music', 'melody', 'harmony', 'tune', 'tone', 'pitch', 'note',
            'chorus', 'chant', 'hymn', 'psalm', 'praise', 'worship',
            'exclaim', 'announce', 'pronounce', 'vocalize', 'articulate',
            'verbal', 'oral', 'acoustic', 'audible', 'sonic'
        ]
    },
    'Sigma_library': {  # Signal Integrity - truth, wholeness, perfection
        'keywords': [
            'truth', 'faithful', 'perfect', 'whole', 'complete', 'upright',
            'just', 'right', 'righteous', 'integrity', 'honest', 'sincere',
            'genuine', 'reliable', 'trustworthy', 'blameless', 'true',
            'verity', 'veracity', 'authenticity', 'accuracy', 'correctness',
            'exactness', 'precision', 'fidelity', 'honesty', 'candor',
            'straightforward', 'forthright', 'guileless', 'artless',
            'undefiled', 'uncorrupted', 'pure', 'sound', 'solid', 'firm'
        ]
    },
    'Lambda_library': {  # Astral Noise - falsehood, deception, interference
        'keywords': [
            'lie', 'false', 'falsehood', 'vanity', 'vain', 'idol', 'deceit',
            'deceive', 'sorcery', 'divination', 'worthless', 'empty', 'deception',
            'delusion', 'error', 'corrupt', 'pervert', 'lying', 'liar',
            'mendacity', 'untruth', 'fabrication', 'fiction', 'counterfeit',
            'fake', 'fraud', 'sham', 'pretense', 'guile', 'duplicity',
            'treachery', 'betrayal', 'trickery', 'cunning', 'craft',
            'magic', 'enchantment', 'witchcraft', 'spell', 'charm', 'curse'
        ]
    },
    'beta_library': {  # Sensitivity Exponent - receptiveness, listening, feeling
        'keywords': [
            'listen', 'hear', 'hearken', 'heart', 'tender', 'soft', 'gentle',
            'perceive', 'sense', 'feel', 'receive', 'attentive', 'incline',
            'ear', 'sensitive', 'responsive', 'hearing', 'heed', 'obey',
            'attend', 'regard', 'notice', 'observe', 'aware', 'conscious',
            'mindful', 'alert', 'watchful', 'vigilant', 'receptive',
            'open', 'accepting', 'welcoming', 'understanding', 'sympathetic',
            'compassionate', 'empathetic', 'caring', 'kind', 'merciful'
        ]
    }
}

def find_matching_words(all_words: List[Dict], keywords: List[str]) -> List[Dict]:
    """Find Hebrew words whose English meanings match the given keywords."""
    matches = []
    seen_clean_hebrew = set()
    
    for word in all_words:
        english = word.get('english', '').lower()
        clean_hebrew = word.get('clean_hebrew', '')
        
        if not english or clean_hebrew in seen_clean_hebrew:
            continue
        
        # Check if any keyword appears in the English meaning
        for keyword in keywords:
            if keyword.lower() in english:
                matches.append(word)
                seen_clean_hebrew.add(clean_hebrew)
                break
    
    return matches

def create_transliteration(hebrew: str) -> str:
    """Create a simple transliteration of Hebrew text."""
    # This is a simplified transliteration mapping
    trans_map = {
        'א': 'aleph', 'ב': 'bet', 'ג': 'gimel', 'ד': 'dalet', 'ה': 'he',
        'ו': 'vav', 'ז': 'zayin', 'ח': 'chet', 'ט': 'tet', 'י': 'yod',
        'כ': 'kaf', 'ך': 'kaf', 'ל': 'lamed', 'מ': 'mem', 'ם': 'mem',
        'נ': 'nun', 'ן': 'nun', 'ס': 'samech', 'ע': 'ayin', 'פ': 'pe',
        'ף': 'pe', 'צ': 'tsadi', 'ץ': 'tsadi', 'ק': 'qof', 'ר': 'resh',
        'ש': 'shin', 'ת': 'tav'
    }
    
    clean = strip_diacritics(hebrew)
    # For now, just return clean Hebrew - proper transliteration would be more complex
    return clean

def populate_library(library_name: str, all_words: List[Dict]) -> List[Dict]:
    """Populate a specific library with relevant words."""
    keywords = THEMATIC_KEYWORDS[library_name]['keywords']
    matching_words = find_matching_words(all_words, keywords)
    
    # Format for the library
    library_entries = []
    for word in matching_words:
        entry = {
            'hebrew': word['clean_hebrew'],
            'transliteration': create_transliteration(word['clean_hebrew']),
            'gematria': word['gematria'],
            'english': word.get('english', '')
        }
        library_entries.append(entry)
    
    # Sort by gematria value
    library_entries.sort(key=lambda x: x['gematria'])
    
    return library_entries

def main():
    """Main function to populate all gematria libraries."""
    print("Loading Tanach books...")
    books = load_tanach_books()
    print(f"Loaded {len(books)} books")
    
    print("\nExtracting words from Tanach...")
    all_words = extract_words_from_tanach(books)
    print(f"Extracted {len(all_words)} unique words")
    
    # Save all words for reference
    print("\nSaving word database...")
    with open('reference_materials/extracted_words.json', 'w', encoding='utf-8') as f:
        json.dump(all_words, f, ensure_ascii=False, indent=2)
    
    # Populate each library
    print("\nPopulating libraries...")
    for library_name in THEMATIC_KEYWORDS.keys():
        print(f"  Processing {library_name}...")
        library_entries = populate_library(library_name, all_words)
        
        output_path = f'gematria_libraries/{library_name}.json'
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(library_entries, f, ensure_ascii=False, indent=2)
        
        print(f"    Created {len(library_entries)} entries for {library_name}")
    
    print("\n✓ All libraries populated successfully!")
    
    # Print summary
    print("\n=== Summary ===")
    for library_name in sorted(THEMATIC_KEYWORDS.keys()):
        output_path = f'gematria_libraries/{library_name}.json'
        with open(output_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        print(f"{library_name}: {len(data)} entries")

if __name__ == '__main__':
    main()
