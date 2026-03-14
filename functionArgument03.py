############ defualt argument
# def  fun(a,b=30):
#     c=a+b
#     print(c)
# fun(20,12)

############### sequencial argument
# def list(c,d):
#     c=c+d
#     print(c)
# list(10,4)

############### Keyword Arbitrary argument
# def net(principle,rate,time):
#     i=principle*rate,time/100
#     print(i)
# # net(200,10)
# net(time=2,principle=5000,rate=3)

########## lambda function
# a = lambda n: [i for i in range(1,n+1)]
# for i in a(6):
#     print(i) 

# a=lambda n: 'even' if n % 2==0 else 'odd'
# b=int(input('enter number:'))
# print(a(b))

# x=lambda a =int(input('enter number')),b=int(input('enter second number')):a+b
# b=x()
# print(b)

############## Recursion function
# def name():
#     print("my name is = uzma")
#     name()
# name()

# def add(a):
#     if a>20:
#         return 
#     print(a)
#     add(a+1)
# add(1)

#####No return no parameter
# def sum():
#     for i in range(2,22,2):
#         print(i)
# sum()

# def sum():
#     a=30
#     b=20
#     if a>b:
#         print('yes')
#     else:
#         print('no')
# sum()

# def g():
#     a=20
#     b=10
#     c=50
#     if a>b and c<a:
#         print('a is greater')
#     elif b>a and c>b:
#         print(' b is greater')
#     else:
#          print('c is greater')
# g()

################# No return with parameter
# def me(a):
#     print(a)
#     for i in range(2,21,2):
#         print(i)
# a=0        
# me(a)

# def sam(a):
#     if a%2==0:
#         print('even')
#     else:
#         print('odd')
# sam(6)



################# with return no parameter
# def add():
#     a=300
#     b=236
#     c=234
#     if a>b and a>c:
#             print('a is big')
#     elif b>a and b>c:
#             print('b is big')
#     else:
#         # print('c is big')
#      return "c is big"
# print(add())

# def name():
#     a=20
#     b=10
#     return a*b
# print(name())

# ################ with return with parameter
# def fun(w):
#     return w
# for i in range(3,30,3):
#     print(fun(i))

# def fun(a,b):
#     return a,b
# a=int(input('enter value'))
# b=int(input('enter string'))
# print(a+b) 

# def table(n):
#     for i in range(1, 11):
#         print( n + i)
#     return "Done"

# table(3)
