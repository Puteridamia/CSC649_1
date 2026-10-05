# CSC649 Setup

## Description
This program accepts a sentence from the user and calculates the word count as well as character counts (both including and excluding spaces). It also features input validation to handle empty entries gracefully.

## How to Run
1. Ensure the Python virtual environment (`.venv`) is activated.
2. Run the script using the terminal by typing: `python main.py` (or click the green Run button in PyCharm).
3. Enter a sentence when prompted.

## Test Results
- **Normal sentence:** "Hello world" 
  - Word count: 2
  - Character count (including spaces): 11
  - Character count (excluding spaces): 10
- **Empty input:** "" 
  - Displays: "You did not enter a sentence."
- **Extra spaces:** "   Hello   world   " 
  - Word count: 2
  - Character count (including spaces): 13
  - Character count (excluding spaces): 10

## Limitation
The word count logic uses `.split()`, which treats any sequence of non-whitespace characters as a word. This means punctuation marks attached to a word are not filtered out, and standalone symbols are counted as words.