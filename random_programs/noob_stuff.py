n = int(input("Enter a year: "))

if n % 100:
    if n % 400:
        print("It is a leap year.☺")
elif n % 4:
    print("It is a leap year.☺")
else:
    print("It is a normal year.")