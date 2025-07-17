#Third Party
import random

# function part
def roll_dice():
    dice_total = random.randint(1,6) + random.randint(1,6)
    return dice_total

# Main definition
def main():
    player1 = input("Enter Player 1's Name:\n")
    player2 = input("Enter Player 2's Name:\n")

    roll1 = roll_dice()
    roll2 = roll_dice()

    print(player1, "rolled", roll1)
    print(player2, "rolled", roll2)

    if roll1 > roll2:
        print(player1, "Wins!!!")
    elif roll2 > roll1:
        print(player2, "Wins!!!")
    else:
        print("It's a Tie !!!")

# main Line
main()        