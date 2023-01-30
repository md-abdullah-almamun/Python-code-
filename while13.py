##program to find sum of digits of a number

num=int(input("enter any number="))

sum=0

while(num!=0):
    sum+=int(num%10)
    num=num/10
print("Sum of digits=",sum)


