# Step 1

# TODO-1 Randomly choose a word from the word_list and assign it to a variable called chosen_word.

# TODO-2 Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

# TODO-3 Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# Step 2

# TODO-1 Create an empty list called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_","_","_","_","_"] with 5 "_" representing each letter to guess.

# TODO-2 Loop through each position in the chosen_word;
# If the lletter at that position matches 'guess' then reveal that letter in the display at that position.
# e.g If the user guessed "p" and the chosen word was "apple", then display should be ["_","p","p","_","_"].

# TODO-3 Print 'display' and you should see the guessed letter in the correcto position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.

# Step 3

# TODO-1 Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

# Step 4

# TODO-1 Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.

# TODO-2 If guess is not a letter in the chosen_word, then reduce 'lives' by 1. 
# If lives goes down to 0 then the game should stop and it should print "You lose."

# Join all the elements in the list and turn it into a String.

# TODO-3 Print the ASCII art from 'stages' that corresponds to the curren number of 'lives' the user has remaining.
import random

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

word_list = ["advark", "baboon", "camel"]

display = []

chosen_word = random.choice(word_list)

word_lenght = len(chosen_word)

end_of_game = False

lives = 6

guessed = False

for letter in chosen_word:
    display.append("_")

#Testing code
print(f"The chosen word is {chosen_word}")

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    for position in range(word_lenght):
        letter = chosen_word[position]
        if guess == letter:
            display[position] = guess
            guessed = True
    
    if guess not in chosen_word:
        guessed = False

    if not guessed:
        lives -= 1

    print(stages[lives])

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")
    elif lives == 0:
        end_of_game = True
        print("You lose!")



