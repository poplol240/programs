"""
n = int(input("Please enter a number: "))

if n % 2 == 0:
    print("This number is even.")
elif not n % 2 == 0:
    print("This number is odd.")

first_n = int(input("Plese enter a number: "))
second_n = int (input("Plese enter another number: "))

if first_n % second_n == 0:
    print("first_n is divisable by second_n")
elif not first_n % second_n == 0:
    print("First_n is not divisable by second_n")



n = range(1,10)
for i in n:
    if i < 5:
        print(i, end= " ,")




num = int(input("Please choose a number to divide: "))

listRange = list(range(1,num+1))

divisorList = []

for number in listRange:
    if num % number == 0:
        divisorList.append(number)

print(divisorList)
"""






