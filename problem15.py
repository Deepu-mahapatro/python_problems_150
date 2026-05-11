# using loop method 
n=int(input("enter a number"))
rev=0
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("the reverse number is :",rev)


#using string slicing method
n=int(input("enter a number"))
h=str(n)
reverse=h[::-1]
print(" the reverse number :",reverse)


#using lambda function method
n=int(input("enter a number"))
h=str(n)
reverse = lambda n: h[::-1]

print(reverse(n))