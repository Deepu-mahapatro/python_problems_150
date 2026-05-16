#REMOVE EMPTY LIST FORM A LIST

#USING LIST COMPREHENSION METHOD
num=[[1,2],[],[3,4],[]]
result=[x for x in num if x]
print(result)


#USING FILTER METHOD
num=[[1,2],[],[3,4]]
result=list(filter(lambda x : x,num))
print(result)


#USING FOR LOOP METHOD
num=[[1,2],[],[3,4]]
result=[]
for i in num:
    if i:
        result.append(i)
print(result)
    