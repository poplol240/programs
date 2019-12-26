#93
#yay
#100% me

import random
hp = 3 
hot_dog = ""
cake = ""
burger = ""
room = 1
monster = False
num1 = 0
action = 0
last_action = 0


print("You fell in a cave.")
print("It is deep and dark, you can't see anything.")
print("You found a flashlite in your bag.")
print("Your goal is to escape.")
print("You see 2 doors.")

def bag():
    hot_dog ==True
    cake == False
    burger == True

def monster_hit():
    random.randint(1,6)
    if num1 == 1 or num1 == 2 or num1 == 3:
        hp =- 1
        monster == False
    elif num1 == 4 or num1 == 5 or num1 == 6:
        monster == False

if room == 2 or room == 4 or room == 5 or room == 8:
    monster = True

action = input("chose what you do: 1 = enter door 1, 2 = enter door 2, 3 = check your bag")
if action == 1:
    room == 2
elif action == 2:
    room == 7
elif action == 3:
    if hot_dog == True:
        print("You have a hot dog")
    elif cake == True:
        print("you have a cake")
    elif burger == True:
        print("You have a burger")


while True:
    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")




    if room == 1:
        action = input("chose what you do: 1 = enter door 1, 2 = enter door 2, 3 = check your bag")
        if action == "1":
            room == 2
        elif action == 2:
            room == 7
        elif action == 3:
            if hot_dog == True:
                print("You have a hot dog")
            elif cake == True:
                print("you have a cake")
            elif burger == True:
                print("You have a burger")


    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")
    
    elif room == 2:
        action = input("chose what you do: 1 = enter door 1, 2 = enter door 2, 3 = check your bag, 4 = fight the monster")
        if action == 1:
            room == 3
        elif action == 2:
            room == 4
        elif action == 3:
            if hot_dog == True:
                print("You have a hot dog")
            elif cake == True:
                print("you have a cake")
            elif burger ==True:
                print("You have a burger")
        elif action == 4:
            monster_hit()

    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")

    elif room == 3:
        action = input("chose what you do: 1 = enter door 1, 2 = check your bag")
        if action == 1:
            room == 2
        elif action == 2:
            if hot_dog == True:
                print("You have a hot dog")
            elif cake == True:
                print("you have a cake")
            elif burger == True:
                print("You have a burger")

    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")
    
    elif room == 4:
        action = input("chose what you do: 1 = enter door 1, 2 = enter door 2, 3 = check your bag, 4 = fight the monster")
        if action == 1:
            room == 5
        elif action == 2:
            room == 6
        elif action == 3:
            if hot_dog == True:
                print("You have a hot dog")
            elif cake == True:
                print("you have a cake")
            elif burger == True:
                print("You have a burger")
        elif action == 4:
            monster_hit()

    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")
    
    elif room == 5:
        action = input("chose what you do: 1 = enter door 1, 2 = check your bag, 3 = fight the monster.")
        if action == 1:
            room == 4
        elif action == 2:
            if hot_dog == True:
                print("You have a hot dog")
            elif cake == True:
                print("you have a cake")
            elif burger == True:
                print("You have a burger")
        elif action == 3:
            monster_hit()

    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")
    
    elif room == 6:
        action = input("chose what you do: 1 = enter door 1, 2 = check your bag")
        if action == 1:
            room == 10
        elif action == 3:
            if hot_dog == True:
                print("You have a hot dog")
            elif cake == True:
                print("you have a cake")
            elif burger == True:
                print("You have a burger")

    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")
    
    elif room == 7:
        action = input("chose what you do: 1 = enter door 1, 2 = enter door 2, 3 = check your bag")
        if action == 1:
            room == 8
        elif action == 2:
            room == 9
        elif action == 3:
            if hot_dog == True:
                print("You have a hot dog")
            elif cake == True:
                print("you have a cake")
            elif burger == True:
                print("You have a burger")

    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")
    
    elif room == 8:
        action = input("chose what you do: 1 = enter door 1, 2 = enter door 2, 3 = check your bag, 4 = fight the monster.")
        if action == 1:
            room == 4
        elif action == 2:
            room == 6
        elif action == 3:
            if hot_dog == True:
                print("You have a hot dog")
            elif cake == True:
                print("you have a cake")
            elif burger == True:
                print("You have a burger")
        elif action == 4:
            monster_hit()

    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")
    
    elif room == 9:
        action = input("chose what you do: 1 = enter door 1, 2 = check your bag")
        if action == 1:
            room == 7
        elif action == 2:
            if hot_dog == True:
                print("You have a hot dog")
            elif cake == True:
                print("you have a cake")
            elif burger == True:
                print("You have a burger")

    if room == 2 or room == 4 or room == 8:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 2 doors.")
    elif room == 5:
        print("You entered a room.")
        print("A monster attacks you!")
        print("You see 1 door.")
    elif room == 7:
        print("You entered a room.")
        print("You see 2 doors.")
    elif room == 3 or room == 6 or room == 9:
        print("You entered a room.")
        print("You see 1 doors.")
    elif room == 10:
        print("You won!!!")
        print("You survived with " + hp + ".")
        print("☺☻☺☻")









