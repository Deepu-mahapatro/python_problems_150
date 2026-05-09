#suing normal method 
p=int(input("enter p value"))
t=int(input("enter t value"))
r=int(input("enter r value"))
A=p*(1+(r/100))**t
CI=A-p
print(CI)


#using function
def compound(p,t,r):
    return p*(1+(r/100))**t
A=compound(4,3,1)
CI=A-p
print(CI)


#using built in pow
p=4
t=3
r=1
A=p*pow(1+(r/100),t)
CI=A-p
print(CI)

