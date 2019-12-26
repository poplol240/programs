import random

usable_nums = ["0", "2", "3", "4", "5", "6", "7", "8", "9"]
usable_nums1 = ["2", "3", "4", "5", "6", "7", "8"]
usable_nums2 = ["4", "5", "7", "8",]
usable_nums3 = ["3", "4", "5", "6", "8", "9"] 
usable_nums4 = ["2", "3", "4", "5", "6", "7", "9"]
usable_nums5 = ["6", "7", "8", "9"]
good_nums = []
biggest_add = []
smallest_add = []
biggest_num = 0
smallest_num = 1000000
good = False

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

    nb1 = random.choice(usable_nums1)
    usable_nums.remove(nb1)
    

    if int(nb1) == 2:
        nb4 = random.randint(8, 9)
    elif int(nb1) == 3:
        nb4 = random.randint(7, 9)
    elif int(nb1) == 4:
        nb4 = random.randint(6, 9)
    elif int(nb1) == 5:
        nb4 = random.choice(usable_nums5)
    elif int(nb1) == 6:
        nb4 = random.choice(usable_nums2)
    elif int(nb1) == 7:
        nb4 = random.choice(usable_nums3)
    elif int(nb1) == 8:
        nb4 = random.choice(usable_nums4)
    
    usable_nums.remove(str(nb4))

    nb2 = random.choice(usable_nums)
    usable_nums.remove(nb2)

    nb3 = random.choice(usable_nums)
    usable_nums.remove(nb3)

    nb5 = random.choice(usable_nums)
    usable_nums.remove(nb5)

    nb6 = random.choice(usable_nums)
    usable_nums.remove(nb6)

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

    if int(nb) + int(nbb) == int(nbbb) and nbb - 1000 <= 0:
        good_nums.append(nb)
        good_nums.append(nbb)
        good_nums.append(nbbb)
        #print(good_nums)
        good = True

    if int(nbbb) > biggest_num and good == True:
        biggest_num = int(nbbb)
        biggest_add.append(nb)
        biggest_add.append(nbb)
        print("+++++++++++++++++++")
        print(biggest_add)
        print(biggest_num)
    
    
    if int(nbbb) < smallest_num and good == True:
        smallest_num = nbbb
        smallest_add.append(nb)
        smallest_add.append(nbb)
        print("-------------------")
        print(smallest_add)
        print(smallest_num)


    usable_nums = ["0", "2", "3", "4", "5", "6", "7", "8", "9"]
    usable_nums1 = ["2", "3", "4", "5", "6", "7", "8"]
    usable_nums2 = ["4", "5", "7", "8",]
    usable_nums3 = ["3", "4", "5", "6", "8", "9"] 
    usable_nums4 = ["2", "3", "4", "5", "6", "7", "9"]
    usable_nums5 = ["6", "7", "8", "9"]

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

    good = False

    biggest_add = []
    smallest_add = []
