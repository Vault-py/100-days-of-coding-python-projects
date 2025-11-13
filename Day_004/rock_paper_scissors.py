
print("Welcoemto Vault codes, Rock, paper and scissors game, feel free to play to know how good you are in prediction")
game = ["rock", "paper", "scissors"]


import random

computer = random.choice(game)



user = input("Choose, Type Rock, paper, or scissors").lower()


if computer == "rock" and user == "scissors":
    print(f"you chose : {user}\n  Computer Chose: {computer}, which means you lost!!")

elif computer == "scissors" and user == "rock":
    print(f"you chose : {user}\n Computer Chose: {computer}, which means you won!!, congrats")

elif computer == "scissors" and user == "paper":
    print(f"you chose : {user}\n  Computer Chose: {computer}, which means you lost!!")


elif computer == "paper" and user == "scissors":
    print(f"you chose : {user}\n  Computer Chose: {computer}, which means you won!!")


elif computer == "rock" and user == "paper":
    print(f"you chose : {user}\n  Computer Chose: {computer}, which means you won!!")

elif computer == "paper" and user == "rock":
    print(f"you chose : {user}\n  Computer Chose: {computer}, which means you lost!!")

elif computer == user:
    print("Its a tie ")

else:
   print( "invalid input, try again ")

