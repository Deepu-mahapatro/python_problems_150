#FIND SECOND LARGEST ELEMENT IN AN ARRAY 
arr=[1,2,3,4,5]
largest=arr[0]
n=len(arr)
second=-1
for i in range(1,n):
    if arr[i]>largest:
        second=largest
        largest=arr[i]
    elif arr[i]>second and arr[i]!=largest:   #CHECK IS THIS IS THE SECOND LARGEST NUMBER
        second=arr[i]
print("second largest:",second)


#USING SORT METHOD
arr=[1,2,3,4,5]
arr.sort(reverse=True)
result=arr[1]
print("second largest:",result)
