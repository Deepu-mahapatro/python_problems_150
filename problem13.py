#using normal method
n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    sum+=i*i
print(sum)


#using formula method
n=int(input("enter a number"))
sum=(n*(n+1)*(2*n+1))//6
print(sum)


#using lambda function method 
square_sum = lambda n: (n * (n + 1) * (2*n + 1)) // 6

n = int(input("Enter a number: "))

print(square_sum(n))