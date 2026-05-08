# adding of two numbers 
a=int(input("enter a number"))
b=int(input("enter b number"))
c=a+b
print(c)

#using function
def add(a,b):
    return a+b
result=add(55,63)
print(result)


#using lambda function
a=lambda x,y:x+y
print(a(34,56))


#using operator module
import operator as op
print(op.add(23,56))


#using sum method 
print(sum([535,646]))