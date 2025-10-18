# Enochian Transliteration

This directory contains tools for transliterating the Hebrew Bible (Tanach) into Enochian script while preserving gematria values.

## Files

- **`authentic_enochian_ledger.json`** - Enochian gematria ledger with letter values and alphabet mappings
- **`transliterate_tanach_authentic.js`** - Script to transliterate Hebrew Bible to Enochian

## Usage

To run the transliteration:

```bash
cd enochian_transliteration
node transliterate_tanach_authentic.js
```

The script will:
1. Read all books from `../the_hebrew_holy_bible-tanach/individual_books/`
2. Create a letter-to-letter mapping based on gematria values
3. Transliterate each Hebrew letter to its corresponding Enochian letter
4. Save output to `./enochian_tanach_authentic/`

## Output

The script processes all 39 books of the Hebrew Bible and generates JSON files with Enochian transliterations. Each output file contains:
- Book name
- Chapters and verses in Enochian script
- Direct letter-to-letter transliteration preserving the structure and gematria values

### How It Works

The transliteration uses a **direct letter-to-letter mapping** based on matching gematria values:

| Hebrew Letter | Value | → | Enochian Letter | Value |
|---------------|-------|---|-----------------|-------|
| א | 1 | → | A | 1 |
| ב | 2 | → | B | 2 |
| ג | 3 | → | C | 3 |
| ד | 4 | → | D | 4 |
| ה | 5 | → | E | 5 |
| ו | 6 | → | F | 6 |
| ז | 7 | → | G | 7 |
| ח | 8 | → | H | 8 |
| ט | 9 | → | I | 9 |
| י | 10 | → | L | 10 |
| כ | 20 | → | M | 20 |
| ל | 30 | → | N | 30 |
| מ | 40 | → | O | 40 |
| נ | 50 | → | P | 50 |
| ס | 60 | → | Q | 60 |
| ע | 70 | → | R | 70 |
| פ | 80 | → | S | 80 |
| צ | 90 | → | T | 90 |
| ק | 100 | → | U | 100 |
| ר | 200 | → | X | 200 |
| ש | 300 | → | Z | 300 |
| ת | 400 | → | ZU | 300+100 |

**Example:** The Hebrew word **בראשית** (Genesis) transliterates to:
- ב (2) → B
- ר (200) → X
- א (1) → A
- ש (300) → Z
- י (10) → L
- ת (400) → ZU

Result: **BXAZLZU**

### Phonetic Reference

For pronunciation, refer to the alphabet mapping:
- A = Un, B = Pa, C = Ged, D = Gal, E = Or, F = Graph, G = Na, H = Tal, I = Gon, L = Ur
- M = Mals, N = Ger, O = Doux, P = Pal, Q = Med, R = Don, S = Ceph, T = Van, U = Fam
- X = Gisg, Z = Veh

So **BXAZLZU** is pronounced: **Pa-Gisg-Un-Veh-Ur-Veh-Fam**

## Enochian Alphabet

The Enochian alphabet consists of 21 letters with the following phonetic representations:

| Letter | Phoneme | Value |
|--------|---------|-------|
| A | Un | 1 |
| B | Pa | 2 |
| C | Ged | 3 |
| D | Gal | 4 |
| E | Or | 5 |
| F | Graph | 6 |
| G | Na | 7 |
| H | Tal | 8 |
| I | Gon | 9 |
| L | Ur | 10 |
| M | Mals | 20 |
| N | Ger | 30 |
| O | Doux | 40 |
| P | Pal | 50 |
| Q | Med | 60 |
| R | Don | 70 |
| S | Ceph | 80 |
| T | Van | 90 |
| U | Fam | 100 |
| X | Gisg | 200 |
| Z | Veh | 300 |

## Notes

- The output directory (`enochian_tanach_authentic/`) is excluded from version control via `.gitignore`
- The transliteration uses a deterministic letter-to-letter mapping, so each run will produce identical results
- Hebrew diacritics (nikud/vowel points) are removed, but **punctuation marks are preserved** to maintain sentence boundaries and structure
- The Hebrew letter ת (tav, value=400) is transliterated as ZU (300+100) since Enochian has no single letter with value 400
- The output contains only Enochian letters (A-Z); phonetic representations are provided in the alphabet reference for pronunciation

## Text Directionality

Like Hebrew, **Enochian is written right-to-left**. According to John Dee's *Five Books of Mystery*, the angel Uriel explicitly instructed:

> "...as all the writing and reding of that holy language is from the right hand to the left, So the begynning of the boke must be, (as it were, in respect of our most usuall manner of bokes, in all languages of latin, greke, english &c) at the ende of the boke: and the ende, at the begynning, as in the hebru bible."

### Implementation Notes

The JSON output stores text in standard left-to-right order for compatibility with digital systems. For proper display:

- **Web rendering**: Use CSS `direction: rtl` and `unicode-bidi: bidi-override` to render text right-to-left
- **Print formatting**: Text should be displayed from right to left, with the book beginning at what would be the "end" in Western books
- **Word order**: Words within each verse maintain their logical order from the Hebrew; the right-to-left direction applies to the overall text flow

Example CSS for web display:
```css
.enochian-text {
  direction: rtl;
  text-align: right;
  unicode-bidi: bidi-override;
}
```
