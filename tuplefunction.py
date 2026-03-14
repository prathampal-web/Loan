########### getsize of function,,,,,,,,,,,,,
# import sys
# l=[23,65,12,87,566,8,9]
# t=(9,8,7,6,45,6788,23)
# print('size of l=',sys.getsizeof(l))
# print('size od t=',sys.getsizeof(t))

########## convert string into tuple,,,,,,,,,,,,,,
# t1=tuple('world')
# print(t1)

########### convert list into tuple ,,,,,,,,,,,,,,,,,
# list1=[1,2,3,4,5]
# tuple1=tuple(list1)
# print(tuple1) 
 
############changeable tuple,,,,,,,,,,,,,,,,,,,
# x=('p','o','n','g')
# y=list(x)
# y[1]='the start'
# x=tuple(y)
# print(x)

############ check element,,,,,,,,,,,,,,,,,,,
# tuple1=('a','b','a','c','a')
# if 'h' in tuple1:
#     print('yes the element is present in the tuple')
# else:
#     print('no')

############ length function,,,,,,,,,,,,,,,,,,,,,
# t1=(1,2,6,4,3,8,6)
# print(len(t1))

############ count the duplicate elements,,,,,,,,,,,,,
# t1=('A','B','C','A','A','A')
# x=t1.count('A')
# print()

############ find index of any item,,,,,,,,,,,,,,,,
# t1=(21,22,43,22,90,22)
# x=t1.index(22)
# print(x)

############concat tuple,,,,,,,,,,,,,,,,,,
# t1=(1,2,3,4,5,6)
# t2=(7,8,9,10,)
# x=t1+t2
# print(x)

###########split function,,,,,,,,,,,,,,,
# import ast
# x=tuple(input("Enter space-separated word:").split())
# print(x)

######interger input,,,,,,,,,,,,,,,,,,
# A=input("Enter space-separated integer:")
# b=tuple(int(item) for item in A.split())
# print(b)

############ list convert tuple,,,,,,,,,,,,,,,,,,
# l=[]
# for i in range(3):
#     v=input('enter')
#     l.append(v)
# a=tuple(l)
# print(a)

##########remove item into tuple,,,,,,,,,,,,,,,,,,,
# a=(3,2,6,28,)
# del(a)
# print(a)