import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
number = random.randint(1,100)

def compare(number, guess):
    global lives
    if number < guess:
        print("Too high")
        print("Guess again.")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    elif number > guess:
        print("Too low")
        print("Guess again.")
        lives -= 1
        print(f"You have {lives} attempts remaining to guess the number.")
    elif lives == 0:
        print("You've run out of guesses, you lose!")
    else:
        print(f"You got it! The answer was {number}.")

# Test code
print(f"The correct answer is {number}")
lives = 10
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

if difficulty == 'hard':
    lives = 5
    print("You have 5 attempts remaining to guess the number")
elif difficulty == 'easy':
    lives = 10
    print("You have 10 attempts remaining to guess the number.")
else:
    print("Please choose a valid difficulty")

guess = 0 

while guess != number and lives > 0:
    guess = int(input("Make a guess: "))
    compare(number,guess)






