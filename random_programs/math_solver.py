import random

usable_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
final_result = []
usable_nums.remove("1")

done = 0
appended = False

nb1 = ""
nb2 = ""
nb3 = ""
nb4 = ""
nb5 = ""
nb6 = ""
nb7 = 1
nb8 = ""
nb9 = ""
nb10 = ""

while True:

    nb1 = random.choice(usable_nums)
    while nb1 == 1 or 0:
        nb1 = random.choice(usable_nums)
    usable_nums.remove(nb1)

    nb2 = random.choice(usable_nums)
    usable_nums.remove(nb2)

    nb3 = random.choice(usable_nums)
    usable_nums.remove(nb3)

    nb4 = random.choice(usable_nums)
    while nb4 == 9 or 0:
        nb4 = random.choice(usable_nums)
    usable_nums.remove(nb4)

    nb5 = random.choice(usable_nums)
    usable_nums.remove(nb5)

    nb6 = random.choice(usable_nums)
    usable_nums.remove(nb6)

    #nb7 = random.choice(usable_nums)
    #while nb7 == 0:
        #nb7 = random.choice(usable_nums)
    #usable_nums.remove(nb7)

    nb8 = random.choice(usable_nums)
    usable_nums.remove(nb8)

    nb9 = random.choice(usable_nums)
    usable_nums.remove(nb9)

    nb10 = random.choice(usable_nums)
    usable_nums.remove(nb10)

    


    nb7 = int(nb7) * 1000

    nb1 = int(nb1) * 100
    nb4 = int(nb4) * 100
    nb8 = int(nb8) * 100

    nb2 = int(nb2) * 10
    nb5 = int(nb5) * 10
    nb9 = int(nb9) * 10


    #print(nb1)
    #print(nb2)
    #print(nb3)
    #print(nb4)
    #print(nb5)
    #print(nb6)
    #print(nb7)
    #print(nb8)
    #print(nb9)
    #print(nb10)

    nb = int(nb1) + int(nb2) + int(nb3)
    nbb = int(nb4) + int(nb5) + int(nb6)
    nbbb = int(nb7) + int(nb8) + int(nb9) + int(nb10)

    #print(nb)
    #print(nbb)
    #print(nbbb)

    if int(nb) + int(nbb) == int(nbbb):
        #final_result.append(nbbb)
        #appended = True
        print(nbbb)

    usable_nums = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    usable_nums.remove("1")

    #if appended == True:
        #print(final_result)
        #appended = False





