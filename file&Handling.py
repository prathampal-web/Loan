######### create file
# f=open("Dem.txt","r")
# print("file name is =",f.name)
# print("file mode is =",f.mode)
# print("file closed  =",f.closed)
# f.close()


######## file object method
###readable and writeable
# f=open("Dem.txt","r")
# print(f.readable())
# # print(f.writable())
# f.close()

###### check file exist or not using isfile()
# import os
# x=os.path.isfile("Demo.txt")
# print(x)

########### write data in a file use 2 method 1.write() 2. writelines()
# f=open("Dem.txt","w")
# f.write("this is cadd \n centre")
# f.close()

## writelines()
# f=open("Dem.txt","w")
# l=["this is cadd centre\n"," i m pratham\n","how are you"]
# f.writelines(l)
# f.close()

########### read data use 3 methods read() readline()  readlines()
# f=open("Dem.txt","r")
# # data=f.read()
# # data=f.read(6)
# data=f.readlines()
# print(data)
# f.close()

####single inharitance
# class A:
#     def name(self):
#         print('this is code ')

# class b(A):
#     def demo(self):
#         print('how is run')
         
# object=b()
# object.name()
# object.demo()

####### multiple interitance
# class fun:
#     def let(self):
#         print('this is class fun')
# class lek(fun):
#     def var(self):
#         print(30+20)
# class we(lek):
#     def ff(self):
#         print('this is we')
# object=we()
# object.let()
# object.var()
# object.ff()



###### syntex multilevel

# class A:
#      def function():
#           
# class B(A):
#      def function1():
#           
# class C(B):
#      def function2():
 
# ### create object
# ob=C()
# ob.function()
# ob.function1()
# ob.function2()

####### hiererchical
# class A:
#      def function():
#          
# class B(A):
#      def function1():
#           
# class C(A):
#      def function2():
#          
# #### create 
# ob=B()
# ob.function()
# ob.function1()

# ob.function()
# ob.function2()      


############# Access public member Modifier
# class A:
#     def abc(self): 
#         print('hello pratham')
# class B:
#     def xyz(self):
#         print('the function')
# object=A()
# object.abc()

# object=B()
# object.xyz()

############# Access private member Modifier
# class name:
#     def __abc(self):
#         print('hello')
#     def par(self):
#         print('run')
#         self.__abc()
# object=name()
# object.par()

############# Access protector member Modifier
# class we:
#     def _demo(self):
#         print('this output is testing')
# class see(we):
#     def _no(self):
#         print('hello')
#         object=we()
#         object._demo()
# object=see()
# object._no()


# class vehicle:
#     def __init__(self,name,color,price):
#         self.name=name
#         self.color=color
#         self.price=price
#     def getdetail(self):
#         print("name is =",self.name)
#         print("color is =",self.color)    
#         print("price is =",self.price)    
           
# v=vehicle("Truck","red",790000) 
# v.getdetail()  


# class vehicle:
#     def __init__(self,name,color,price):
#         self.name=name
#         self.color=color
#         self.price=price
#     def getdetail(self):
#         print("name is =",self.name)
#         print("color is =",self.color)    
#         print("price is =",self.price)  
#     def maxspeed(self):
#         print("maximum speed is 100")         
#     def gear(self):
#         print("gear is 5")    
# v=vehicle("truck","brown",90000)
# v.getdetail()
# v.maxspeed()
# v.gear()        


########### constructorwith inheritanc and polymorphism

# class vehicle:
#     def __init__(self,name,color,price):
#         self.name=name
#         self.color=color
#         self.price=price
#     def getdetail(self):
#         print("name is =",self.name)
#         print("color is =",self.color)    
#         print("price is =",self.price)  
#     def maxspeed(self):
#         print("maximum speed is 100")         
#     def gear(self):
#         print("gear is 5")
# class car(vehicle):
#     def maxspeed(self):
#         print("maximum speed is 150")         
#     def gear(self):
#         print("gear is 7")
# v=vehicle("truck","brown",90000)
# v.getdetail()
# v.maxspeed()
# v.gear()   
# print("car detail  \n")
# v=car("thar","black",70000)
# v.getdetail()
# v.maxspeed()
# v.gear()  