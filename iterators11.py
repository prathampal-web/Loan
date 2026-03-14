# ######### iterator function
# n=['pratham','u','m','k']
# it=iter(n)
# print(it.__next__())

######### Generator function
# def genfunction():
#     yield 10+80
# it=genfunction()
# # for i in it:
# #     print(i)  
# print(it.__next__())

########## CLoser
# def out():
#     print('pratham')
#     def let():
#         print('start')
#     let()
# out()

#############no retun no parameter
# def out():
#     a=10
#     b=a+20
#     print(b)
#     def inner():
#         a=10
#         b=20
#         c=a*b
#         print(c)
#     inner()
# out()

# def out():
#     a=10
#     b=40
#     C=a+b
#     def inner():
#         print(C)
#     return inner
    
# x=out()
# x()

#### decorator
# def deco(fun):
#     print('this is pro')
#     def wrap():
#         print('hello')
#         fun()
#     return wrap()
# @ deco
# def fun():
#     print('good afternoon')