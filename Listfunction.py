############ user input list
# a=[]
# for i in range(5):
#     x=int(input("enter item"))
#     a.append(x)
# print(a)


# a=[]
# size=int(input("enter size"))
# for i in range(size):
#     x=int(input("enter item"))
#     a.append(x)
# print(a)


# ###reversed
# a=[]
# size=int(input("enter size"))
# for i in range(size):
#     x=input("enter item") 
#     a.append(x)
# print(a)
# for i in reversed(a):
#     print(i)


########## access list element with for loop
# a=["uzma",3,6,9.6] 
# for i in a:
#     print(i)

############# for loop
# a=["uzma",3,6,9.6]
# print(a)
# a.append("cadd centre")
# print(a)

############### remove()
# a=["uzma",'g']
# print(a)
# x=input("enteer item you want to remove")
# a.remove(x)
# print(a)


############# clear()
# a=["uzma",3,6,9.6]
# print(a)
# a.clear()
# print(a)


############ len(),,,,,,,,,,,,,,,,,,,,,,
# a=["uzma",3,6,9.6]
# print(len(a))


###### max() & min()
# a=[7,9,5,4,90]
# b=max(a)
# v=min(a)
# print(b)
# print(v)
 
 
#  input user value and remove,,,,,,,,,,,,,,,,,,,,,,,
# b=[]
# size=int(input('enter size'))
# for i in range(size):
#     x=int(input('enter value'))
#     b.append(x)
#     print(b)
# x=int(input('enter any value'))
# b.remove(x)
# print(b) 


# count()
# a=['Ram','Ram','shyam','Ram','Ram','Ram'],,,,,,,,,,,,,,,,,,
# print(a)
# c=a.count('shyam')
# print(c)

# a=[]
# size=int(input('enter size'))
# for i in range(size):
#     x=(input('enter item'))
#     a.append(x)
#     print(a)
# y=input('enter item you want to count')
# z=a.count(y)
# print(z)


# insert,,,,,,,,,,,,,,,,,
# a=[3,1,8,]
# a.insert(1,'pratham')
# print(a)

# insert,,,,,,,,,,,,,,,,,,
# a=['s','a','d',]
# print(a)
# for i in range(3):
#     x=int(input("enter index nmbr"))
#     y=input('enter value')
#     a.insert(x,y)
# print(a)


######### index,,,,,,,,,,,,,,,,,,
# a=['s',9,2,1,8,3,52,]
# print(a)
# x=a.index(9)
# print(x)

######## sort,,,,,,,,,,,,,,,,,,,,,,,
# a=[9,4,90,2,1]
# b=[9,20,4,90,2,1]
# a.sort(reverse=False)
# b.sort(reverse=True)
# print(a)
# print(b)


######## pop,,,,,,,,,,,,,,,,,,,,,
# a=[9,4,90,2,1]
# print(a)
# a.pop()
# print(a) 


##################practice
# a=[1,2,3,4,5]
# sum=0
# for i in range(5):
#     sum=sum+a[i]
# print("sum of list element is =",sum)    


#############python program to find sum of element of the list,,,,,,,,,,,,,,,,,
# l=[]
# size=int(input('enter size'))
# for i in range(size):
#     x=int(input('enter value'))
#     l.append(x)
# sum=0
# for i in range(size):
#     sum=sum +l[i]
# print('sum of list is =',sum)    


############python prog. to count total number of odd and even in the list,,,,,,,,,,,,,,,,
# l=[]
# size=int(input('enter size'))
# for i in range(size):
#     x=int(input('enter value'))
#     l.append(x)
# even=0
# odd=0
# for i in range(size):
#     if l[i]%2==0:
#        even=even+1
#     else:
#         odd=odd+1
# print('total even=',even,'total odd=',odd)


###########python program to search a number in the list sequencial search Linear search,,,,,,,,,,,
# a=[]
# size=int(input('enter size'))
# for i in range(size):
#     x=int(input('enter value'))
#     a.append(x)
# key=int(input('enter value number to search'))
# flag=0
# for i in range(size):
#     if(a[i]==key):
#         flag=1
#         post=i+1
#         break
# if(flag==1):
#         print('element found at:',post,'positon')
# else:  
#     print('element not found')
       
        
###################program to find max number of the list and min,,,,,,,,,,,,,,,,,,,,,,
# a=[]
# size=int(input('enter size'))
# for i in range(size):
#     x=int(input('enter value'))
#     a.append(x)  
# max=a[0]
# for i in range(size):
#     if(a[i]>max):
#         max=a[i]
# print('max number=',max)


# def max():,,,,,,,,,,,,,,,,,,,
#     n=30
#     if n%2==5:
#         print('no is even')
#     else:
#         print('no id odd')
# max()


################## second,,,,,,,,,,,,,,,,,,,
# def  add():
#     a=90
#     b=100
#     c=a+b
#     print(c)
# a=add()