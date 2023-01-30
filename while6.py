##program to find sum of natural numbers from 1 to n

num=int(input("enter any number="))

sum=0
i=1

while(i<=num):
    sum=sum+i
    print("Sum of first",i,"natural number=",sum)
    i=i+1