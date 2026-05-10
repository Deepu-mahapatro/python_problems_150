# Nth multiple of a number in Fibonacci Series”

# It means:

# Find the Nth Fibonacci number that is divisible by a given number.
# Simple Example

# Take:

# Number = 3
# N = 4

# Now write Fibonacci series:

# 0 1 1 2 3 5 8 13 21 34 55 89 144 ...
# Find Multiples of 3

# Check which Fibonacci numbers are divisible by 3:

# 0   → divisible by 3
# 3   → divisible by 3
# 21  → divisible by 3
# 144 → divisible by 3
# 987 → divisible by 3
# ...
# Count Them
# 1st multiple → 0
# 2nd multiple → 3
# 3rd multiple → 21
# 4th multiple → 144

# So:

# 4th multiple of 3 in Fibonacci series = 144


#using recursion method
def fib(n):
    if n<=1:
        return n
    else:
        return fib(n-1)+fib(n-2)
n=int(input("enter multiple number"))  # this gives multiple nth exact ans what we want
k=int(input("enter k divisor "))       # divisible number to get series
#initially
i=0  #index loop
count=0  #count multiples of n
while count<n:
    value=fib(i)
    if value%k==0:
        count+=1
        result=value
    i+=1
print(result)
