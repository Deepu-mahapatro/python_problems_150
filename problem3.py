#using recursion
def fact(n):
    if n<0:
        return "factorial is negative in number"
    return 1 if n<=1 else n*fact(n-1)
print(fact(5))


#using module method
import math as m
print(m.factorial(5))


#using iterative method 
n=int(input("enetr a number"))
if n<0:
    print("factorial is negative")
else :
    f=1
    for i in range(1,n+1):
        f*=i
    print(f)


