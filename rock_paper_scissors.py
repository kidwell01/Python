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

print("Welcome to the game of rock, paper, scissors.\nYou will be playing against the computer, but don't be scared you can win!!!")
game = ["rock","paper","scissors"]
my_choice = input("Now make a choice, rock, paper or scissors? \n").lower()

if my_choice == "rock":
  print(f"Your choice:\n {rock}")
elif my_choice == "paper":
  print(f"Your choice:\n {paper}")
elif my_choice == "scissors":
  print(f"Your choice:\n {scissors}")
else:
  print("Invalid choice!")
  

comp_choice = random.choice(game)
if comp_choice == "rock":
  print(f"Computer's choice:\n {rock}")
elif comp_choice == "paper":
  print(f"Computer's choice:\n {paper}")
else:
  print(f"Computer' choice:\n {scissors}")

if my_choice == comp_choice:
  print("It's a tie!!!")
elif (my_choice == "rock" and comp_choice == "scissors") or (my_choice == "paper" and comp_choice == "rock") or (my_choice == "scissors" and comp_choice == "paper"):
  print("You win!!!")
else:
  print("You lose!!")