##program to find sum of even numbers between 1 to n

num=int(input("entet any number="))
sum=0
i=0

while(i<=num):
    if(i%2==0):
        sum=sum+i
        print("this is total sum of even=",sum)
    i=i+1


