# playing rock, paper, scissors with the computer

user_input = input("Enter Rock, Paper or Scissors \n")

choices = ["Rock", "Paper", "Scissors"]
import random
comp_input = choices[random.randint(0,2)]

print(comp_input)