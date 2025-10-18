# Voynich Attack
The Voynich Manuscript is the Holy Grail of cipher mysteries. Dating from the late Middle Ages (*maybe*), the manuscript sports bizarre illustrations of extraterrestrial-looking plants, bevies of bathing beauties in networks of tubes, and thousands upon thousands of “words” written in an utterly unknown alphabet. 

By all the laws of cryptology, the Voynich should have been cracked decades ago. It never has. Not a single word has ever been deciphered despite drawing the gaze of the world's preeminent cryptographic agencies and the internet's most obsessive amateurs. What harm, then, in one more foolish foray into this most enchantingly cryptic enigma?

## Getting Started

To use the analysis tools in this repository, you need to install the required Python packages.

### 1. Installation

Navigate to this directory and use `pip` to install the dependencies listed in `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 2. Running the Analysis (Conscious-Relativity Integration)

This repository is used as a submodule within the `Conscious-Relativity` project. The entire workflow is managed from the parent repository's root directory.

**Step 1: Generate the Corpus**

First, ensure the individual book text files are created from the source JSON. Run this from the `Conscious-Relativity` root:

```bash
python scripts/export_corpus.py
```

This will populate the `vendor/voynich-attack/corpora/hebrew/` directory with the necessary `.txt` files.

**Step 2: Run the Analysis**

Next, run the main analysis script. This script will iterate through each book, perform a statistical analysis, and generate individual reports. Run this from the `Conscious-Relativity` root:

```bash
python run_voynich_analysis.py
```

The results will be saved in the `analysis_results` directory within the `Conscious-Relativity` project.

**Important**: Do not use the `examples/hebrew_analysis_example.py` script. It is not configured for the current project workflow. For more details on the integrated workflow, see `AGENTS.md`.


## Table of Contents
1. [Transcription](transcription)
1. [Voynich Stats](topics/voynich_stats/1grams)
    - Characters: [1-grams](topics/voynich_stats/1grams) •  [2-grams](topics/voynich_stats/2grams)
    - Tokens: [1-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/voynich_stats/1tks) •  [2-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/voynich_stats/2tks)
     - [Positional Ranks](topics/voynich_stats/tokens_by_position)
1. [Reference Corpora](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/biblio)
1. [Latin](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/latin_stats/1grams)
    - Letters: [1-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/latin_stats/1grams) •  [2-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/latin_stats/2grams)
    - Words: [1-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/latin_stats/1words) •  [2-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/latin_stats/2words)
1. [German](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/german_stats/1grams)
    - Letters: [1-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/german_stats/1grams) •  [2-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/german_stats/2grams)
    - Words: [1-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/german_stats/1words) •  [2-grams](https://github.com/alexanderboxer/voynich-attack/tree/main/topics/german_stats/2words)

