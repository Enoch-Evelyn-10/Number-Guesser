#Number Guessing Game
#User will pick  a number 1-20 
# Find a way to have a random number generated
# Check for and save user input
#Compare user input to generated number 
#If matched print correct if not print incorrect 


#genrate a random number 
import random

number = random.randint(1,10)

#record user input
guessnumber= int(input("Choose a number from 1-10: "))

if number == guessnumber:
    print("Correct, the number was:",number)
else:
    print("Incorrect the number was:", number)