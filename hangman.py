import re
import random
with open("lines.txt") as f: # gets the content of lines.txt
    lines = f.readlines()

word = random.choice(lines).lower().strip() # This is the word to guess, later I'll make a system that gets one from a list
limit = 5 # This is the number of the guesses
i = 1 # This is for the loop
b = 0 # This is to know if the word is guessed

sequence = "_" * len(word) # This is the preview of the word



def change_char(s, p, r): # Function that changes the preview
    return s[:p]+r+s[p+1:]

while i <= limit: # If you still have guesses
    remainingGuesses = limit - i # If you still have guesses
    print(f"{sequence} | You still have {remainingGuesses} guesses") # prints the remaining guesses
    letter = input("Guess a letter or a word: ").lower() # the input
    if len(letter) >= 2: # if is longer than 1
        if letter == word: # if the input is the word
            print(f"You win, the word is '{word}'")
            break # breaks the loop
        else: # if it is not longer than 1
            print(f"You failed, {letter} is not in the word") # wrong
    if letter in word and len(letter) == 1: # if the input is 1 character
        for m in re.finditer(letter, word): # checks if there are multiple equal letters
            position = m.start() # the position (index) of the character
            sequence = change_char(sequence, position, letter) # updates the sequence
            b = b+1 # adds 1 to the number of guessed characters
    if b == len(word): # if the number of guessed characters is the same as the lenght of the word
        print(f"You win, the word is '{word}'")
        break
    i = i+1
else: # if you used all of your guesses
    print(f"You lose, the word is '{word}'")

















