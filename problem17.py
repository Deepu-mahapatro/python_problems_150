#USING SUM METHOD
list=[1,2,3,4,5]
result=sum(list)
print(result)


#USING FOR LOOP
list=[1,2,3,4,5]
total=0
for i in list:
    total+=i
print(total)


#USING RECURSION METHOD
def total(arr,n):
    if n==0:
        return 0
    return arr[n-1]+total(arr,n-1)
arr=[1,2,3,4,5]
print(total(arr,len(arr)))


#USING REDUCE METHOD
from functools import reduce
arr=[1,2,3,4,5]
result=reduce(lambda x,y:x+y,arr)
print(result)


#USING WHILE LOOP METHOD 
arr=[1,2,3,4,5]
total=0
i=0
n=len(arr)
while i<n:
    total+=arr[i]
    i+=1
print(total)