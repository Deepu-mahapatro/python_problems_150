#USING REVERSE() METHOD
arr=[1,2,3,4,5]
arr.reverse()
print(arr)


#SLICING METHOD 
arr=[1,2,3,4,5]
result=arr[::-1]
print(result)


#USING FOR LOOP METHOD
arr=[1,2,3,4,5]
result=[]
n=len(arr)
for i in range(n-1,-1,-1):
    result.append(arr[i])
print(result)
    