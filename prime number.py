num=int(input("enter any integer number="))

for i in range(2, num):
    if num % i == 0:
        print("Not a Prime number")
        break

else:
    print("this is prime number") 