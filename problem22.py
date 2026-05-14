#MULTIPLY ALL ELEMENTS IN AN ARRAY
arr=[1,2,3,4,5]
n=len(arr)
result=2
for i in arr:
    result*=i
print(result)


#USING REDUCE METHOD and mul() METHOD
from functools import reduce
from operator import mul
arr=[1,2,3,4,5]
result=reduce(mul,arr)
print(result)


#USING MATH.PROD() METHOD
import math
arr=[1,2,3,4,5]
result=math.prod(arr)
print(result)


