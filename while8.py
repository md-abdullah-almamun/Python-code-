##program to find sum of odd numbers from 1 to n

num=int(input("enter any number="))
sum=0
i=1

while(i<=num):
    if(i%2!=0):
        sum=sum+i
        print("this is total all odd number sum= ",sum)

    i=i+1
