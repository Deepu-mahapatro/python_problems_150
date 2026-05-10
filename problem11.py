#using recursion method
n=int(input("engter a number"))
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
print(fib(n))
for i in range(n+2):
    if fib(i)==n:
        print("fibonacci number")
        break
else:
    print("not a fibonacci number")
    
    
#using loops method 
n=int(input("enter a number"))
a=0
b=1
if n<0:
    print("in valid number")
else:
    for i in range(n+2):
        if a==n:
            print("fibonacci number")
            break
        c=a+b
        a=b
        b=c
    else:
        print("not a fibonacci number")