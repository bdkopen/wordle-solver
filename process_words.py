# Fetch all possible Wordle words from the text file and return them.
def getPossibleWords():

    with open('wordle_words.txt') as file:
        words_raw = file.readlines()

    words = []

    # Strip off any whitespace or line breaks
    for x in words_raw:
        words.append(x.strip())

    return words
    file.close()