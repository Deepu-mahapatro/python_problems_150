#using normal matehmatical method
n=int(input("enter a number"))
#take input and store in a variable
num=n
t=0 #total sum=o
l=len(str(n)) #converts int to str to calculate length
while num>0:
    r=num%10 #to calculate last digit
    t+=r**l #to calculate power of digits and add to total sum
    num//=10 #to remove last digit
if t==n:
    print("armstrong")
else:
    print("not an armstrong ")
    
    

#using string conversion method 
n=int(input("enter a number"))
t=0
num=str(n)
l=len(num)
for i in num:
    t+=int(i)**l
if t==n:
    print("armstrong")
else:
    print("not an armstrong")


#recursion method
def armstrong(n,l):
    if n==0:
        return 0
    return pow(n%10,l)+armstrong(n//10,l)
n=int(input("enter n number "))
l=len(str(n))
if armstrong(n,l)==n:
    print("armstrong")
else:
    print("not an armstrong")