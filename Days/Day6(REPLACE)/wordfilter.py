# This script is meant to generate a list of curated english words

import statistics

def hasRepeatingChar(word):
    """
    This Function simply returns True if there is a repeating character in a recieved string
    if not, returns false."""
    seenchars = []
    for char in word:
        if char in seenchars:
            return True
        else:
            seenchars.append(char)
    return False

def gen_clean_english():
    # Create List of english words
    file = open("English.txt", "r+")
    english = file.readlines()
    englishn = []
    file.close()
    cleanedFile = open("CleanEnglish.txt", "w+")


    lengths = []
    for word in english:
        lengths.append( len(word[0:-1]) )
        englishn.append(word[0:-1])


    meanLength = statistics.mean(lengths)
    stdevLength = statistics.stdev(lengths)

    benchmarked_length = meanLength + stdevLength
    for word in english:
        if len(word) > benchmarked_length and hasRepeatingChar(word[0:-1]):
            cleanedFile.write(word)

    cleanedFile.close()


if __name__ == "__main__":
    gen_clean_english()