# Gematria Library Population Report

This document summarizes the population of gematria libraries from the Hebrew Tanach.

## Overview

All gematria libraries have been populated using a comprehensive search of the Hebrew Tanach (39 books). The population script (`../populate_gematria_libraries.py`) extracts Hebrew words from all books, calculates their gematria values using standard Hebrew gematria, and categorizes them according to thematic concepts defined in `AGENTS.md`.

## Methodology

### Data Source
- **Source**: Hebrew Tanach (39 books) from `reference_materials/the_hebrew_holy_bible-tanach/`
- **Total unique words extracted**: 39,451
- **Format**: Each word includes Hebrew text (cleaned of diacritics), gematria value, and English translation

### Gematria Calculation
The script uses **standard Hebrew gematria** with the following letter values:
- א=1, ב=2, ג=3, ד=4, ה=5, ו=6, ז=7, ח=8, ט=9
- י=10, כ/ך=20, ל=30, מ/ם=40, נ/ן=50, ס=60, ע=70, פ/ף=80, צ/ץ=90
- ק=100, ר=200, ש=300, ת=400

### Text Processing
- Hebrew diacritical marks (vowel points and cantillation) are removed
- Only Hebrew letters (א-ת) are retained
- Words are deduplicated based on cleaned Hebrew text
- English meanings are preserved from the original verse data

### Thematic Matching
Each library corresponds to a specific concept from AGENTS.md. Words are matched based on their English translations containing relevant keywords. The keyword sets have been expanded beyond the examples in AGENTS.md to ensure comprehensive coverage.

## Library Statistics

| Library | Concept | Entries | Previous Count |
|---------|---------|---------|----------------|
| A_library.json | Adeptship (mastery, expertise) | 512 | 19 |
| alpha_library.json | Skill Constant (craft, workmanship) | 1,231 | 12 |
| kappa_library.json | Efficiency Constant (speed, directness) | 404 | 12 |
| N_library.json | Collective Force (groups, assemblies) | 2,614 | 12 |
| k_library.json | To Know (knowledge, understanding) | 562 | 12 |
| d_library.json | To Dare (courage, bravery) | 326 | 11 |
| w_library.json | To Will (volition, desire) | 2,219 | 9 |
| s_library.json | To Keep Silent (silence, secrecy) | 550 | 7 |
| I_library.json | Imagination (mental imagery, devising) | 487 | 10 |
| F_library.json | Faith (belief, trust) | 429 | 8 |
| D_library.json | Disturbance (chaos, turmoil) | 450 | 11 |
| Delta_library.json | Diaphane (clarity, purity) | 380 | 10 |
| R_library.json | Resonance (response, vibration) | 1,005 | 9 |
| Sigma_library.json | Signal Integrity (truth, wholeness) | 332 | 10 |
| Lambda_library.json | Astral Noise (falsehood, deception) | 572 | 8 |
| beta_library.json | Sensitivity Exponent (receptiveness) | 1,007 | 7 |

## JSON Format

Each library file contains an array of objects with the following structure:

```json
{
  "hebrew": "אמת",
  "transliteration": "אמת",
  "gematria": 441,
  "english": "truth"
}
```

Fields:
- `hebrew`: Hebrew word with diacritics removed (consonants only)
- `transliteration`: Currently set to the cleaned Hebrew (future enhancement could add romanization)
- `gematria`: Calculated gematria value using standard Hebrew gematria
- `english`: English meaning/translation from the original Biblical text

Entries are sorted by gematria value in ascending order within each library.

## Thematic Coverage

### A_library (Adeptship)
Focuses on mastery, expertise, and high skill levels. Keywords include: master, expert, chief, head, skilled, wise, wisdom, understanding, knowledge, craftsman, artisan, prince, leader, intelligent, discerning, prudent, sage, elder, teacher, instructor, etc.

### alpha_library (Skill Constant)
Represents skill, craft, and workmanship. Keywords include: skill, work, deed, craft, workmanship, handiwork, labor, service, device, instrument, tool, vessel, make, build, create, form, fashion, design, etc.

### kappa_library (Efficiency Constant)
Captures concepts of speed, directness, and effectiveness. Keywords include: swift, quick, haste, speed, diligent, straight, upright, success, prosper, flourish, advance, direct, accomplish, complete, finish, perfect, effective, etc.

### N_library (Collective Force)
Contains words related to groups and collectives. Keywords include: nation, people, assembly, congregation, multitude, host, army, troop, company, tribe, family, community, all, together, gather, unite, unity, etc.

### k_library (To Know)
Encompasses knowledge and understanding. Keywords include: know, knowledge, wisdom, understanding, perceive, see, discern, insight, learn, teach, instruct, aware, recognize, comprehend, realize, consider, etc.

### d_library (To Dare)
Represents courage and bravery. Keywords include: courage, strong, mighty, bold, brave, valiant, warrior, hero, fearless, not afraid, strengthen, power, force, valor, fortitude, etc.

### w_library (To Will)
Covers volition and desire. Keywords include: will, desire, choose, willing, consent, purpose, intent, heart, delight, pleasure, wish, want, incline, favor, goodwill, accept, etc.

### s_library (To Keep Silent)
Focuses on silence and secrecy. Keywords include: silence, silent, quiet, still, stillness, peace, rest, calm, hush, secret, hide, conceal, restrain, cease, keep silence, hold peace, etc.

### I_library (Imagination)
Contains words about mental imagery and devising. Keywords include: imagination, imagine, form, device, thought, think, vision, dream, devise, plan, purpose, intent, frame, inclination, meditation, etc.

### F_library (Faith)
Represents belief and trust. Keywords include: faith, believe, trust, faithful, faithfulness, hope, confidence, rely, depend, sure, firm, steadfast, amen, truth, true, establish, certain, etc.

### D_library (Disturbance)
Captures chaos and turmoil. Keywords include: trouble, tremble, shake, quake, rage, noise, tumult, storm, tempest, whirlwind, terror, confusion, chaos, turmoil, uproar, commotion, disturb, dismay, etc.

### Delta_library (Diaphane)
Focuses on clarity and purity. Keywords include: clear, pure, light, bright, shine, shining, crystal, clean, clarity, transparent, radiant, brilliant, splendor, glory, luminous, white, purify, refine, etc.

### R_library (Resonance)
Represents response and connection. Keywords include: answer, voice, sound, call, respond, echo, shout, song, sing, cry, hear, listen, heart, proclaim, declare, speak, utter, resound, etc.

### Sigma_library (Signal Integrity)
Contains words about truth and wholeness. Keywords include: truth, faithful, perfect, whole, complete, upright, just, right, righteous, integrity, honest, sincere, genuine, reliable, trustworthy, etc.

### Lambda_library (Astral Noise)
Captures falsehood and deception. Keywords include: lie, false, falsehood, vanity, vain, idol, deceit, deceive, sorcery, divination, worthless, empty, deception, delusion, error, corrupt, pervert, etc.

### beta_library (Sensitivity Exponent)
Represents receptiveness and listening. Keywords include: listen, hear, hearken, heart, tender, soft, gentle, perceive, sense, feel, receive, attentive, incline, ear, sensitive, responsive, etc.

## Notes

- The libraries for `chi_prime_library.json`, `Psi_library.json`, `D_opt_library.json`, and `sigma_library.json` are noted in AGENTS.md as being derived from other parameters or mathematical constructs, and were not populated through thematic word matching.

- The transliteration field currently contains the cleaned Hebrew text. A future enhancement could add proper romanization using standard transliteration systems (e.g., SBL, academic).

- All entries maintain their original Hebrew consonantal text, which can be cross-referenced with the full Tanach texts for context.

## Future Enhancements

Potential improvements for future iterations:

1. **Enhanced Transliteration**: Implement proper Hebrew-to-Latin transliteration (e.g., using SBL standards)
2. **Context Preservation**: Add verse references for each word occurrence
3. **Strong's Numbers**: Include Strong's Concordance numbers for deeper lexical analysis
4. **Multi-word Phrases**: Extract and include meaningful multi-word Hebrew phrases
5. **Semantic Clustering**: Use advanced NLP to find semantically similar words beyond keyword matching
6. **Root Analysis**: Group words by Hebrew roots for deeper thematic connections
7. **Frequency Analysis**: Track word frequency across different books and contexts

## Generated Files

- All `*_library.json` files in this directory
- `../reference_materials/extracted_words.json` - Full database of extracted words with gematria values
- `../populate_gematria_libraries.py` - The population script

---

Generated: October 2025
Script: `populate_gematria_libraries.py`
