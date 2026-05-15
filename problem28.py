#DIFFERENT WAYS TO FIND LENGHT OF THE LIST

#USING LEN() METHOD
arr=[1,2,3,4,5]
result=len(arr)
print(result)


#USING FOR LOOP METHOD
arr=[1,2,3,4,5]
count=0
for i in arr:
    count+=1
print(count)


#USING WHILE LOOP METHOD
arr=[1,2,3,4,5]
count=0
i=0
while i<len(arr):
    count+=1
    i+=1
print(count)


#USING SUM() METHOD
arr=[1,2,3,4,5]
result=sum(1 for i in arr)
print(result)


#USING RECURSION METHOD
def find_len(arr):
    if arr==[]:
        return 0
    return 1 + find_len(arr[1:])
arr=[1,2,3,4,5]
print(find_len(arr))