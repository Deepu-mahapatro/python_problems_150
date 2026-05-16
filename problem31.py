#ODD NUMBERS IN A LIST

#USING LOOP METHOD
num=[1,2,3,4,5,6,7,8,9]
for i in num:
    if i%2!=0:
        print("odd number")
        break
else:
    print("not a odd number")
    
    
#USING FILTER METHOD() 
num=[1,2,3,4,5,6,7]
result=list(filter(lambda x: x%2!=0,num))
print(result)


#USING LIST COMPREHENSION
num=[1,2,3,4,5,6,7]
result=[x for x in num if x%2!=0]
print(result)


#USING BITWISE OPERATOR
num=[12,3,4,5,6,7,8]
result=[x for x in num if x&1 ==1]
print(result)