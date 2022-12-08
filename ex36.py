amnt=int(input("enter the any number="))
note500=note100=note50=note20=note10=note5=0
if amnt>=500:
        note500 = amnt / 500
        amnt-=note500*500
elif amnt>=100:
       note100=amnt/100
       amnt-=note100
elif amnt>=50:
       note50=amnt/50
       amnt-=note50
elif amnt>=20:
       note20=amnt/20
       amnt-=note20

elif amnt>=10:
       note10=amnt/100
       amnt-=note10


print("500\t=\t",note500)
print("100\t=\t",note100)
print("50\t=\t",note50)
print("20\t=\t",note20)
print("10\t=\t",note10)



