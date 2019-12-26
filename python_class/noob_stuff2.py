"""
import random
import time

n  = int(input("Enter a number: "))

while n >= 0:
   print(n)
    n -= 1
    time.sleep(1)

n = ["1", "2", "3", "4"]
nums = []




while True:
    nb = random.choice(n)
    n.remove(nb)
    nbb = random.choice(n)
    n.remove(nbb)
    nbbb = random.choice(n)

    final_num = int(str(nb) + str(nbb) + str(nbbb))
    if final_num not in nums:
        n = ["1", "2", "3", "4"]
        nums.append(final_num)
        print(nums)

    n = ["1", "2", "3", "4"]




n = input("Please enter a number: ")

nb = int(n) * (int(n) + 1) / 2

print(nb)




num = int(input("Enter a number: "))

while num > 0:
 
    for i in range(2, num):
	    if num % i == 0:
		    break
    else:
	    print(str(num) + " is a prime number")

    num -= 1





n = 1
print("0,")

while n <= 100:
    if n % 3 == 0 and not n % 5 == 0:
        print(str(n) + " Fizz,")
    elif n % 5 == 0 and not n % 3 == 0:
        print(str(n) + " Buzz,")
    elif n % 5 == 0 and n % 3 == 0:
        print(str(n) + " FizzBuzz,")
    else:
        print(str(n) + ",")

    n += 1




def multiplications():
    for nb in range(1,10):
        for nbb in range(1,nb + 1):
            nbbb = nb * nbb
            print(str(nb) + " * " + str(nbb) + " = " + str(nbbb),end="   ", sep=" ")
        print("\n")

multiplications()
"""








