#USING TEMPORARY VARIABLE METHOD
arr=[1,2,3,4,5]
temp=arr[1]
arr[1]=arr[3]
arr[3]=temp
print(arr)


#USING PYTHON TUPLE SWAPPING
arr=[1,2,3,4,5]
arr[1],arr[3]=arr[3],arr[1]
print(arr)


#USING FUNCTION METHOD
def func(arr,i,j):
    arr[i],arr[j]=arr[j],arr[i]
    return arr
print(func([1,2,3,4,5],arr[0],arr[2]))


#USING ARITHMETIC OPERATIONS
arr=[1,2,3,4,5]
arr[1]=arr[1]+arr[3]
arr[3]=arr[1]-arr[3]
arr[1]=arr[1]-arr[3]
print(arr)


#USING XOR OPERATION
arr=[1,2,3,4,5]
arr[1]=arr[1]^arr[3]
arr[3]=arr[1]^arr[3]
arr[1]=arr[1]^arr[3]
print(arr)

