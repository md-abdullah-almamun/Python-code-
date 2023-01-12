num=int(input("enter any number factor number="))
print("all factors of" ,num ,"are=")
for i in range(1,num+1,1):
    if(num%i==0):
        print(i)
