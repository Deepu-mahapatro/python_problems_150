# REVERSING A LIST IN DIFFERENT WAYS

#USING REVERSE() METHOD
arr=[1,2,3,4,5]
arr.reverse()
print(arr)


#USING SLICING METHOD
arr=[1,2,3,4,5]
result=arr[::-1]
print(result)


#USING REVERSED() METHOD
arr=[1,2,3,4,5]
result=list(reversed(arr))
print(result)


#USING LOOP METHOD
arr=[1,2,3,4,5]
result=[]
n=len(arr)
for i in range(n-1,-1,-1):
    result.append(arr[i])
print(result)


#USING POP() METHOD
arr=[1,2,3,4,5]
result=[]
while arr:
    result.append(arr.pop())
print(result)