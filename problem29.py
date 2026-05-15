#INTERCHANGE THE FIRST AND LAST ELEMENT IN AN ARRAY

#USING SWAP METHOD AND TUPLE PACKING
arr=[1,2,3,4,5]
arr[0],arr[-1]=arr[-1],arr[0]
print(arr)
srr=[5,4,3,2,1]
(srr[0],srr[-1])=(srr[-1],srr[0])
print(srr)


#USING TEMPORARY VARIABLE
arr=[1,2,3,4,5]
temp=arr[0]
arr[0]=arr[-1]
arr[-1]=temp
print(arr)


#USING POP() AND INSERT() METHOD
arr=[1,2,3,4,5]
first=arr.pop(0)
last=arr.pop(-1)
arr.insert(0,last)
arr.append(first)
print(arr)


#USING SLICING METHOD
arr=[1,2,3,4,5]
result=[arr[-1]]+arr[1:-1]+[arr[0]]  #here arr[-1],arr[0] are 5,1 values
print(result)                        #we need list so we use [] for both 