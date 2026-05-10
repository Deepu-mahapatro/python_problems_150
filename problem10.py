# using loops method 
n=int(input("enter a number"))
a=0
b=1
if n<0:
    print("number is not valid")
elif n==0:
    print(a)
elif n==1:
    print(a)
    print(b)
else:
    print(a)
    print(b)
    for i in range(2,n+1):
        c=a+b
        a=b
        b=c
        print(c)
        
        
#using recursion method in sequence 
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter a number"))
for i in range(n):
    print(fib(i),end="")
    
    
#using recursion method 
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("ente a number"))
print(fib(n))
        
        