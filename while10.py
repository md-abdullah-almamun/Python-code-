##program to count number of digits in an integer
num=int(input("enter any number="))

count=0

while(num>0):
    count=count+1
    num=num//10

print("the number of digits in the number are=",count)

