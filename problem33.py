#REMOVE MULTIPLE ELEMENTS FORMA LIST

#USING LIST COMPREHENSION
num=[1,2,3,4,5,6,7,8]
remove=[2,5,6]
result=[x for x in num if x not in remove]
print(result)


#USING FILTER FUNCTION()
num=[1,2,3,4,5,6,7,8]
remove=[2,4,6]
result=list(filter(lambda x : x not in remove,num))
print(result)


#USING FOR LOOP METHOD
num=[1,2,3,4,5,6,7,8]
remove=[2,4,6]
result=[]
for i in num:
    if i not in remove:
        result.append(i)
print(result)


#USING REMOVE() METHOD
num=[1,2,3,4,5,6,7,8]
remove=[2,4,6]
for i in remove:
    while i in num:
        num.remove(i)
print(num)