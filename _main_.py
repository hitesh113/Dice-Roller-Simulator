# Dice Roller Simulator

import random

rollNum = int(input("Enter your favourite number: ")) 

while True:
    rolled_Num=random.randint(1, 6)
    print("You roll: ", rolled_Num)

    user_input = input("Wanna roll again? (Yes/No): ")


    if user_input.lower() == "no":
        break

print("Thank You playing.")