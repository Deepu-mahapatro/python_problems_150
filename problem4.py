# p=int(input("enter a number"))
# t=int(input("enter a number "))
# r=int(input("enter rate "))
# s=(p*t*r)/100
# print(s)


#using function
# def simple(p,t,r):
#     return (p*t*r)/100
# s=simple(8,6,8)
# print(s)


#using lamda function
result=lambda p,t,r:(p*t*r)/100
print(result(8,6,8))