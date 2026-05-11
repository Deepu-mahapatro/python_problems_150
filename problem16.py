#using integer method loop
n=int(input("enter a numbetr"))
rev=0
original=n
while n>0:
    rem=n%10
    rev=rev*10+rem
    n=n//10
if rev==original:
    print("palindrome ")
else:
    print("not a palindrome")


#using slicing method
n = input("Enter a word: ")
reverse = n[::-1]
if n == reverse:
    print("Palindrome")
else:
    print("Not a palindrome")
    
    
#using loop method
n=input("enter a number")
rev=""
for i in n:
    rev=i+rev
if rev==n:
    print("palindrome")
else:
    print("not a palindrome")