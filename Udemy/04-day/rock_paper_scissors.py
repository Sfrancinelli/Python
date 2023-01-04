import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

compu_choice = random.randint(1,3)

while user_choice >= 0 and user_choice < 3:
    if user_choice == 0:
        print("Your pick\n" + rock)
        break
    elif user_choice == 1:
        print("Your pick\n" + paper)
        break
    elif user_choice == 2:
        print("Your pick\n" + scissors)
        break
    else:
        print("Please pick a correct number")

if compu_choice == 0:
    print("Computer pick\n" + rock)
elif compu_choice == 1:
    print("Computer pick\n" + paper)
elif compu_choice == 2:
    print("Computer pick\n" + scissors)

if user_choice == 0 and compu_choice == 0:
    print("It\'s a draw!")
elif user_choice == 1 and compu_choice == 1:
    print("It\'s a draw!")
elif user_choice == 2 and compu_choice == 2:
    print("It\'s a draw!")
elif user_choice == 0 and compu_choice == 1:
    print("You lost! Better luck next time!")
elif user_choice == 0 and compu_choice == 2:
    print("You win!")
elif user_choice == 1 and compu_choice == 0:
    print("You win!")
elif user_choice == 1 and compu_choice == 2:
    print("You lost! Better luck next time!")
elif user_choice == 2 and compu_choice == 0:
    print("You lost! Better luck next time!")
elif user_choice == 2 and compu_choice == 1:
    print("You win!")




