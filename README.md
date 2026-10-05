CSC649 Setup
Description
This program accepts a sentence from the user and calculates both the word count and character count (including spaces). It also features input validation to handle empty entries gracefully.

How to Run
Ensure the Python virtual environment (.venv) is activated.
Run the script using the terminal by typing: python main.py (or simply click the green Run button in PyCharm).
Enter a sentence when prompted.

Test Results
Normal sentence: "Hello world" -> Word count: 2, Character count: 11
Empty input: "" -> Displays "You did not enter a sentence."
Extra spaces: "   Hello   world   " -> Word count: 2, Character count: 19

Limitation
The word count logic uses .split(), which treats any sequence of non-whitespace characters as a word. This means punctuation marks attached to a word are not filtered out, and standalone symbols are counted as words."# CSC649_1" 
