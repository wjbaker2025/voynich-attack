import fs from 'fs';
import path from 'path';
import { fileURLToPath } from 'url';
import { loadGematriaLedger } from '../scripts/agents/lib/gematria.js';

// --- Configuration ---
const __dirname = path.dirname(fileURLToPath(import.meta.url));
const ROOT_PATH = path.resolve(__dirname, '..');
const HEBREW_BIBLE_PATH = path.join(ROOT_PATH, 'the_hebrew_holy_bible-tanach/individual_books');
const HEBREW_LEDGER_PATH = path.join(ROOT_PATH, 'reference_materials/gematria_ledger.json');
const ENOCHIAN_LEDGER_PATH = path.join(__dirname, 'authentic_enochian_ledger.json');
const OUTPUT_PATH = path.join(__dirname, 'enochian_tanach_authentic');
// --- End Configuration ---

/**
 * Creates a mapping from Hebrew letter values to Enochian letters.
 *
 * @param {object} hebrewLedger The Hebrew gematria ledger.
 * @param {object} enochianLedger The Enochian gematria ledger.
 * @returns {object} A mapping from Hebrew letters to Enochian letters.
 */
function createLetterMapping(hebrewLedger, enochianValues) {
  const mapping = {};
  
  // Create a reverse lookup for Enochian: value -> letter
  const enochianByValue = {};
  // FIX: Use the passed enochianValues object directly
  for (const [letter, value] of Object.entries(enochianValues)) {
    enochianByValue[value] = letter;
  }
  
  // Map each Hebrew letter to its corresponding Enochian letter
  for (const [hebrewLetter, hebrewValue] of Object.entries(hebrewLedger)) {
    if (enochianByValue[hebrewValue]) {
      const enochianLetter = enochianByValue[hebrewValue];
      mapping[hebrewLetter] = enochianLetter;
    } else {
      // For Hebrew letters without exact Enochian match (e.g., ת=400),
      // use the closest available value or a combination
      // ת (400) = Z (300) + U (100)
      if (hebrewValue === 400) {
        mapping[hebrewLetter] = 'ZU';
      } else {
        // Default fallback (should not happen with standard letters)
        mapping[hebrewLetter] = '';
      }
    }
  }
  
  return mapping;
}

/**
 * Transliterates a Hebrew word to Enochian using letter-to-letter mapping.
 *
 * @param {string} hebrewWord The Hebrew word to transliterate.
 * @param {object} letterMapping The Hebrew-to-Enochian letter mapping.
 * @returns {string} The Enochian transliteration.
 */
function transliterateWord(hebrewWord, letterMapping, vowelMapping) {
  let enochianWord = '';
  
  // Define punctuation marks to preserve
  const punctuationMarks = [
    '.', ',', '!', '?', ';', ':', 
    '״', '׳', // Hebrew punctuation
    '–', '—', // dashes
    '״', '׃', '׀', // Hebrew verse markers
    '､', // ideographic comma
    '\u00A0', // non-breaking space
  ];
  
  for (const char of hebrewWord) {
    if (letterMapping[char]) {
      // Transliterate Hebrew letters
      enochianWord += letterMapping[char];
    } else if (vowelMapping[char]) {
      // Transliterate Hebrew vowels
      enochianWord += vowelMapping[char];
    } else if (punctuationMarks.includes(char)) {
      // Preserve punctuation marks
      enochianWord += char;
    } else {
      // Preserve any other characters (like vowel points/nikud)
      enochianWord += char;
    }
  }
  
  return enochianWord;
}


/**
 * Main function to transliterate the Tanach.
 */
async function main() {
  console.log('--- Starting Letter-by-Letter Transliteration (Authentic) ---');

  // Load Ledgers
  const hebrewLedger = loadGematriaLedger(HEBREW_LEDGER_PATH);
  const enochianLedger = JSON.parse(fs.readFileSync(ENOCHIAN_LEDGER_PATH, 'utf8'));
  console.log('Gematria ledgers loaded.');

  // Create letter mapping
  const letterMapping = createLetterMapping(
    hebrewLedger, 
    enochianLedger.enochian.gematria_values
  );
  const vowelMapping = enochianLedger.hebrew_vowel_map;
  console.log('Letter and vowel mappings created.');

  // Create output directory
  if (!fs.existsSync(OUTPUT_PATH)) {
    fs.mkdirSync(OUTPUT_PATH);
  }

  // Process each book of the Bible
  const files = fs.readdirSync(HEBREW_BIBLE_PATH).filter(f => f.endsWith('.json'));

  for (const file of files) {
    const bookPath = path.join(HEBREW_BIBLE_PATH, file);
    const bookData = JSON.parse(fs.readFileSync(bookPath, 'utf8'));
    
    // Get the book name (the key in the JSON)
    const bookName = Object.keys(bookData)[0];
    const bookContent = bookData[bookName];
    const chapters = bookContent.chapters || {};
    
    const newBookData = {};

    console.log(`Processing ${bookName}...`);

    for (const [chapter, verses] of Object.entries(chapters)) {
      newBookData[chapter] = {};
      for (const [verse, wordArray] of Object.entries(verses)) {
        // Handle both string and array formats
        let hebrewWords = [];
        if (typeof wordArray === 'string') {
          hebrewWords = wordArray.split(' ');
        } else if (Array.isArray(wordArray)) {
          // Extract Hebrew text from each word object
          hebrewWords = wordArray.map(wordObj => wordObj.hebrew || '');
        }
        
        const enochianWords = hebrewWords.map(word => {
          if (!word) return '';
          return transliterateWord(word, letterMapping, vowelMapping);
        });
        newBookData[chapter][verse] = enochianWords.join(' ');
      }
    }

    // Write the new book file
    const outputFilePath = path.join(OUTPUT_PATH, file);
    const finalOutput = {
      book: bookName,
      chapters: newBookData
    };
    fs.writeFileSync(outputFilePath, JSON.stringify(finalOutput, null, 2));
    console.log(`Finished processing ${bookName}.`);
  }

  console.log('--- Transliteration Complete ---');
}

main().catch(console.error);

export { createLetterMapping, transliterateWord };
