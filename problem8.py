# prime numbers with divisible by 1
#and it self only 
start=int(input("enter a number"))
end=int(input("enter another number"))
for i in range(start,end+1):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)