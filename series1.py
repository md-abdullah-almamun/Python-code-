#1+2+3+........+n
number=int(input("Enter the last number"))
sum=0

for num in range(1,number+1,1):
    sum=sum+num
print(sum)

print("###############################################################")

#1*1+2*2+3*3+...............n*n


n=int(input("Enter the last number"))
sum=0

for num in range(1, n+1, 1):
    sum = sum+num*num

print(sum)

