# This is a hangman game

import random

# Word Library
word_list = ["aardvark", "baboon", "camel", "cwm", "translation", "tesselation", "linguistically", "sequential logic", "nonce"]
# ASCII art
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']


# Make choice
chosen_word = random.choice(word_list)
# Mod Display to match target word
blanks = []
misses = []
for i in range(len(chosen_word)):
    if chosen_word[i] == " ":
        blanks.append(" ")
    else:
        blanks.append("_")

# This function lets us guess then drop
def makeguess(lives):
    global misses
    display_progress()
    print(stages[lives])
    display_misses()
    guess = input("Guess a letter : ").lower()
    valid = False
    for char in range(len(chosen_word)):
        if chosen_word[char] == guess:
            blanks[char] = guess[0]
            valid = True
        if chosen_word[char] in misses:
            valid = True
    if not valid:
        misses += guess

    return valid

def display_progress():
    disp_str = ""
    for letter in blanks:
        disp_str += letter + " "
    print(disp_str)

def display_misses():
    disp_str = ""
    for letter in misses:
        disp_str += "!" + letter + " "
    print(disp_str)

if __name__ == "__main__":
    print(
        """
 /  |                                   
(___| ___  ___  ___  _ _  ___  ___      
|   )|   )|   )|   )| | )|   )|   )     
|  / |__/||  / |__/ |  / |__/||  /      
               __/                                                         
        """
    )
    print("Welcome to Hangman!")

    lives = 6
    while "_" in blanks and lives > 0:
        if not makeguess(lives):
            lives -=1
    display_progress()
    print(stages[lives])
    display_misses()
    
    if lives == 0:
        print(f"Wow, You're a failure! You Died! The Answer was {chosen_word}")
    else :
        print("Congrats! You got it and saved your neck!")

