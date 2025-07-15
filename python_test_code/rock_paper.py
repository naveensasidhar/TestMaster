
# computer choice variable
computer_choice = 'scissors'
# user choice variable
user_choice = input("Do You Want rock, paper, or scissors?\n")

if computer_choice == user_choice:
    print("Tie")
elif user_choice == "rock" and computer_choice == "scissors":
    print("Win")   
elif user_choice == "paper" and computer_choice == "rock":
    print("Win")      
elif user_choice == "scissors" and computer_choice == "paper":
    print("Win")
else:
    print("You Lost And Computer Won")          
