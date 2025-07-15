# import random built-in
import random

# Generate random number between 1 & 6
roll = random.randint(1,2)

#print("The computer rolled a " + str(roll))

# Let the user input A Value
guess = int(input("Guess The Number: \n"))

if roll == guess:
    print("Your Guess work Is Correct & Awesome "+ str(roll))
elif roll != guess:
    print("Prediction Was Not Good & Randome Number Is Different " + str(roll))    