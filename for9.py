num=int(input("enter any number="))
sum=0
average=0
for i in range(1, num+1, 1):
     if (i % 2 != 0):
        sum=sum+i
print("Sum of first ", i, "numbers is: ", sum)
average = sum / i
print("Average of ", i, "numbers is: ", average)