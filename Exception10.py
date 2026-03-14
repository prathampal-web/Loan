############ handl this type of error
# a=int(input("enter nmbr"))
# b=int(input("enter nmbr"))
# try:
#     c=a/b
# except ZeroDivisionError as a:
#     print(a)
#     print("devide by zero not possible")
# else:        
#   print(c)


######multple exception
# num1=40
# num2=2
# try:
#     div=num1/num2
#     print(div)
# except ZeroDivisionError:
#     print('devide by zero in not possible')
# except NameError:
#     print('variable name is wrong')    
# except(NameError,ZeroDivisionError) as obj:
#     print(obj)
   
# class fiveDivisionError(Exception):
#     pass
# try:
#     n1=int(input('enter value'))
#     n2=int(input('enter value'))
#     if n2==5:
#         raise fiveDivisionError('cannot divide by five')
#     div=n1/n2
#     print('division is:',div)
# except(fiveDivisionError,ZeroDivisionError) as var:
#     print(var)

############## wiwth list
# a=['python','mysql','wordpress','computer']
# try:
#     for i in range(5):
#         print('the index of element from the array is',i,a[i])
# except:
#     print('index out of range')
