#FIND SMALLEST NUMBER IN THE ARRAY 
arr=[1,2,3,4,5]
smallest=arr[0]
n=len(arr)
for i in range(1,n):
    if arr[i]<smallest:
        smallest=arr[i]
print("smallest:",smallest)


#USING SORT METHOD 
arr=[5,4,2,7,1,5]
arr.sort()
result=arr[0]
print("smallest:",result)


#USING MIN() METHOD
arr=[1,2,3,4,5]
result=min(arr)
print("smallest:",result)
