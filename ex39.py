basic=int(input("enter basic your salary:"))

if (basic<=10000):
    da=basic*0.8
    hra=basic*0.2

elif (basic<=20000):
    da=basic*0.9
    hra=basic*0.25
else:
    da = basic * 0.95
    hra = basic * 0.3

gross=basic+hra +da

print("gross salary of empoly=",gross)
