########### create class with variable
# class demo:
#     var=10
# object =demo()
# print(object.var)


################# create class with function
# class dem():
#     a=10
#     def sum(self):
#         print(20+30)
#    
# object=dem()
# print(object.a)
# object.sum()


# class dex():
#     a=int(input('enter value'))
#     b=int(input('enter value'))
#     def let(self):
#         print(34*2)                       
# object=dex()
# print(object.a+object.b)
# print(object.b)
# object.let()


############# create class with multiple function
# class well():
#     a=100
#     def show(self):
#         self.c=self.a*self.a
#         print(self.c)
#     def show1(self):
#         self.c=self.a+self.a
#         print(self.c)    
# object=well()
# object.show()
# object.show1()


######user input value
# class well():
#     a=int(input('enter value'))
#     b=int(input('enter value'))
#     def sh(self):
#         self.c=self.a+self.b
#         print(self.c)
#     def se1(self):
#         self.c=self.a*self.b
#         print(self.c)
# object=well()
# object.sh()
# object.se1()


# class dex:
#     a=10
#     b=3
#     def des(self):
#         self.c=self.a*self.b
#         print(self.c)
#     def des1(self, a,b):
#         print(a+b)
#         print('welcome to moradabad')
# object=dex()
# object.des()
# object.des1(120,30)    


########## create class with user input
# class demo:
#     pass
# ob=demo()
# ob.n=int(input("enter nmber"))
# ob.name=input("entr name")
# print(ob.n)
# print("name is ",ob.name)


# program 
# class add():
#     def ss(self,a,b):
#         self.a=a
#         self.b=b
#         self.c=a+b
#         print(self.c)
# object=add()
# a=int(input('enteer'))
# b=int(input('enteer'))
# object.ss(a,b)
        
        
        
############# Constructor mathod
# class demo:
#     def __init__(self,a,b):
#         self.a=a
#         self.b=b                                  
#         self.c=self.a+self.b
#         print(self.c)
#         for i in range(6):
#             print(i)
# object=demo(2,3)


############# pandas
# class school:
#     def input(self):
#         self.name=input('enter name')
#         self.age=int(input('enter age'))
#         self.post=input('enter post')
#     def display(self):
#         print('your name is ',self.name)
#         print('your name is ',self.age)
#         print('your name is ',self.post)
# object=school()
# object.input()
# object.display()

        
# class info:
#     def input(self):
#         self.name=input('enter name')
#         self.post=input('enter post')
#         self.age=int(input('enter age'))
#     def out(self):
#         print('your name is',self.name)
#         print('your post is',self.post)
#         print('your age is',self.age)
# size = int(input('kitne log ka data chahiye: '))

# for i in range(size):
#     print([i+1],size)
#     ob=info()
#     ob.input()
#     ob.out()


################ program student default
# class schoolform:
#     def show(self):
#         print('your name is ',self.name)
#         print('your roll is ',self.roll)
#         print('your age is ',self.age)
        
# object1=schoolform()
# object1.name=input('enter name')
# object1.roll=input('enter roll')
# object1.age=input('enter age')
# object1.show()

# object=schoolform()
# object.name='pratham' 
# object.roll='42'
# object.age='21'
# object.show()

# class student():
#     count=0
#     def __init__(self):
#         self.name=input('enter name')
#         self.roll=int(input('enter no'))
#         student.count +=1
#     def dis(self):
#         print('name',self.name)
#         print('roll',self.roll)
# object=student()
# object.dis()
# object1=student()
# object1.dis()
# print(student.count)


# class network:
#     def __init__(self):
#         self.age=23
#         self.name='pratham'
#         self.post='web dev'
#         # self.age=int(input("enter age"))
#         # self.name=input("enter name")
#         # self.post=input("enter post")
#     def display(self):
#         print('name',self.name)
#         print('age',self.age)
#         print('post',self.post)
# object=network()
# object.display()


# class form:
#     count=0
#     def __init__(self):
#         self.name=input('enter name')
#         self.age=int(input('enter age'))
#         form.count +=1
#     def dis(self):
#         print('name is ',self.name)
#         print('age is ',self.age)
# object=form()
# object.dis()
# print(form.count)