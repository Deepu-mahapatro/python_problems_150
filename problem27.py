# DIFFERENT WAYS TO CHECK WHETHER AN ELEMENT IS EXIST OR NOT

#USING IN OPERATOR
arr=[1,2,3,4,5]
print(3 in arr)


#USING LOOP METHOD
arr=[1,2,3,4,5]
key=3
n=len(arr)
for i in range(n):
    if key==arr[i]:
        print("present in list")
        break
else:
    print("not present in list")


#USING NOT IN METHOD
arr=[1,2,3,4,5]
print(30 not in arr)


#USING INDEX METHOD AND COUNT METHOD
arr=[1,2,3,4,5]
if 3 in arr:
    print("value is present")
if arr.count(3)>0:
    print("found")


#USING ANY METHOD
arr=[1,2,3,4,5]
print(any(x==3 for x in arr))
      