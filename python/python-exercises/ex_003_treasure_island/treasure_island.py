print('''
*******************************************************************************
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
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

choice1 = input('You\'re at a crossroad. Where do you want to go? Type "left" or "right":\n').lower()

def dont_follow_instructions():
    # runs if the user does not follow the instructions correctly
    print('You don\'t know how to follow the instructions correctly!\nGAME OVER!')

if choice1 == 'right':
    print('You\'ve fall into a hole.\nGAME OVER!')

elif choice1 == 'left':
    choice2 = input('You\'ve come to a lake. Do you wanna "swin" or "wait"?\n').lower()
    if choice2 == 'swin':
        print('You were attacked by an angry trout.\nGAME OVER!')
    elif choice2 == 'wait':
        choice3 = input('You arrive at the island unharmed. There is a house with 3 doors with different colors. Which door color do you choose: "red", "yellow" or "blue"?\n').lower()
        if choice3 == 'red':
            print('You were burned by fire.\nGAME OVER!')
        elif choice3 == 'blue':
            print('You were eaten by beasts.\nGAME OVER!')
        elif choice3 == 'yellow':
            print('CONGRATULATIONS! YOU FOUND THE TREASURE! YOU WIN!')
        else:
            dont_follow_instructions()
    else:
        dont_follow_instructions()
else:
    dont_follow_instructions()