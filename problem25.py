# TO CLEAR THE LIST USING DIFFERENT WAYS 

#USING CLEAR METHOD
arr=[1,2,3,4,5]
arr.clear()
print(arr)


#USING EMPTY LIST ASSIGNMENT
arr=[1,2,3,4,5]
arr=[]
print(arr)


#USING LOOP METHOD
arr=[1,2,3,4,5]
n=len(arr)
while arr:
    arr.pop()
print(arr)


#USING DEL KEYWORD
arr=[1,2,3,4,5]
del arr[:]
print(arr)


#USING SLICING METHOD
arr=[1,2,3,4,5]
arr[:]=[]
print(arr)