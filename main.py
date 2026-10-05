# CSC649: My first Python experiment

sentence = input("Enter a sentence: ")

if sentence.strip() == "":
    print("You did not enter a sentence.")
else:
    word_count = len(sentence.split())
    char_including_spaces = len(sentence)
    char_excluding_spaces = len(sentence.replace(" ", ""))

    print("Word count:", word_count)
    print("Character count (including spaces):", char_including_spaces)
    print("Character count (excluding spaces):", char_excluding_spaces)