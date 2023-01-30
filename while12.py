##program to find reverse of a number
num=int(input("Enter any number to find reverse:"))
reverse = 0

while(num!=0):
    reverse=(reverse*10)+(num%10)
    num=num//10

print("reverse=",reverse)






