#PRINT AL EVEN NUMBERS IN A GIVEN RANGE

#USING LOOP METHOD
start=2
end=10
step=2
for i in range(start,end+1,step):
    print(i)



#USING LIST COMPREHENSION
start=2
end=10
result=[i for i in range(start,end+1) if i%2==0]
print(result)


#USING BITWISE OPERATOR
start=2
end=10
for i in range(start,end+1):
    if i & 1==0:
        print(i)
#PRINT ODD NUMBERS GIVEN A RANGE


#USING LOOP METHOD
start=1
end=10
step=2
for i in range(start,end+1,step):
    print(i)


#USING LIST COMPREHENSION
start=2
end=10
result=[i for i in range(start,end+1) if i%2!=0]
print(result)


#USING BITWISE OPERATOR
start=1
end=10
for i in range(start,end+1):
    if i & 1:
        print(i)