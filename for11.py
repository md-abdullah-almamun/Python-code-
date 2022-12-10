num=int(input("enter any number="))
sum=0
avg=0
for i in range(0,num+1,1):
    if(i%2==0):
        sum=sum+i
print("this is total even number=",sum)
avg = sum / i
print("this is sum avg number=",avg)