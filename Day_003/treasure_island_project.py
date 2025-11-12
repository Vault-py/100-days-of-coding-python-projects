print(''' *******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/[TomekK]
******************************************************************************* ''')


print("Welcome to Vault Codes Treasure island, Your mission is to find the treasure")

direction = input("Where do you want to go to in the island, Left or Right").lower()

if direction == "left":

    option_1 = input("there is a big river front of you do you want to swim or wait ?").lower()

    if option_1 == "wait":

        door_color = input("there is 3 doors front of you which do you want to enter, Red, Blue or Yellow? ").lower()

        if door_color == "red":
            print("There is a fire, you are burned, Game over!")

        elif door_color == "blue":
            print("oops there are beats inside, you are eaten , Game over!")

        elif door_color == "yellow":
            print("You won!!!!, Congratulations!")

        else:
            print("invalid input, Game Over!")

    elif option_1 == "swim":
        print("There is trought in the water and you have been eaten")
    else:
        print("Game over invalid input, try again")
elif direction == "right":
    print("There was a big hole at the right, so you fell inside, you died game over!")


else:
    print("Invalid input try again")
    








