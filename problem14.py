#using normal method
n=int(input("enter a number"))
sum=0
for i in range(1,n+1):
    sum+=i**3
print(sum)


#using formula method
n=int(input("enter a number"))
sum=((n*(n+1))//2)**2
print(sum)


#using lambda function method
cube_sum = lambda n: ((n * (n+1)) // 2) ** 2

n = int(input("Enter a number: "))

print(cube_sum(n))