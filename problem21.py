#FIND THE LARGEST ELEMENT IN THE ARRAY
list=[1,2,3,4,5]
largest=list[0]
n=len(list)
for i in range(1,n):
    if list[i]>largest:
        largest=list[i]
print("largest:",largest)


# USING SORT() METHOD
arr=[1,2,3,4,5]
arr.sort(reverse=True)
result=arr[0]
print("largest:",result)


#USING MAX() METHOD
arr=[1,2,3,4,5]
result=max(arr)
print("largest:",result)


#USING REDUCE() METHOD
from functools import reduce
arr=[1,2,3,4,5]
result=reduce(lambda x,y:x if x>y else y,arr)
print("largest:",result)