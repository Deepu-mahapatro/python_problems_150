#ROTATION OF ARRAY CONCEPT

#USING LOOP METHOD
arr=[1,2,3,4,5]
n=len(arr)
first=arr[0]
for i in range(n-1):
    arr[i]=arr[i+1]
arr[-1]=first
print(arr)


#USING SLICING METHOD
arr=[1,2,3,4,5]
k=2
#LEFT ROTATION
result=arr[k:]+arr[:k]
print(result)
#RIGHT ROTATION
ans=arr[-k:]+arr[:-k]
print(ans)


#USING REVERSE() METHOD
arr=[1,2,3,4,5,6,7]
n=len(arr)
k=2
arr.reverse()
#LEFT ROTATION
result=list(reversed(arr[:k]))+list(reversed(arr[k:]))
#RIGHT ROTATION
ans=list(reversed(arr[:-k]))+list(reversed(arr[-k:]))
print(result)
print(ans)



#USING POP() $ APPEND() METHOD
arr=[1,2,3,4,5,6,7]
#LEFT ROTATION
first=arr.pop(0)
arr.append(first)
print(arr)
#RIGHT ROTATION
last=arr.pop()
arr.insert(0,last)
print(arr)