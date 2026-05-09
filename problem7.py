#using normal method 
r=int(input("enter radius"))
pi=3.14
area=pi*(r**2)
print(area)


#using math module
import math as m
r=int(input("enter a radius"))
area=m.pi*(r*r)
print(area)

#using function 
def area(r):
    pi=3.14
    return pi*pow(r,2)
r=int(input("enter a radius"))
radius=area(r)
print(radius)


#using numpy 
import numpy as np 
r=int(input("enter a radius"))
area=np.pi*pow(r,2)
print(area)