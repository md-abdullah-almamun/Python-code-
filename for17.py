fact=1

num=int(input("enter any number to calculate factorial="))

for i in range(1,num+1,1):
    fact=fact*i

    print("Factorial of",num,'=',fact)