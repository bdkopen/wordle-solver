# Fetch all possible Wordle words from the text file and return them.
def getPossibleWords():
    words_raw = []

    with open('wordle_words.txt') as file:
        words_raw = file.readlines()

    file.close()

    words = []

    # Strip off any whitespace or line breaks
    for word in words_raw:
        words.append(word.strip())

    return words
