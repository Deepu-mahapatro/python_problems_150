#using max method
a=int(input("enter a number"))
b=int(input("enetr b number"))
c=max(a,b)
print(c)


#using ternary opeartor
a=7
b=6
print(a if a>b else b)


# another ternary method 
a=int(input("enetr a number "))
b=int(input("enter b numebr"))
c=a if a>b else b
print(c)


#using if else statemnt 
a=int(input("enter a number"))
b=int(input("enter b number"))
if a>b:
    print("a is larger then b")
else:
    print("b is larger then a ")
    

#using sort method 
a=7
b=5
nums=[a,b]
c=nums.sort()
print(nums[-1])