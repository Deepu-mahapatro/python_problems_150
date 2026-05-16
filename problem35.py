#BREAK THE LIST INTO CHUNKS WITH A SIZE N

#USING SLICING + LIST COMPREHENSION METHOD 
num=[1,2,3,4,5,6,7,8,9]
n=3
result=[num[i:i+n] for i in range(0,len(num),n)]
print(result)


#USING FOR LOOP METHOD
num=[1,2,3,4,5,6,7,8,9]
n=len(num)
k=3
chunks=[]
for i in range(0,n,k):
    chunk=num[i:i+k]
    chunks.append(chunk)
print(chunks)