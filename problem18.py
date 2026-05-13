#USING MAX METHOD
list=[1,2,3,4,5]
result=max(list)
print(result)


#USING FOR LOOP METHOD
list=[1,2,3,4,5]
largest=0
for i in list:
    if i >largest:
        largest=i
print(largest)


#USING SORTING METHOD 
arr=[1,2,3,4,5]
arr.sort()
largest=list[-1]
print(largest)


#USING RECURSION METHOD
def larger(arr,n):
    if n==1:
        return arr[0]
    return max(arr[n-1],larger(arr,n-1))
arr=[1,2,3,4,5]
print(larger(arr,len(arr)))