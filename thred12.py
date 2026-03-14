# from threading import Thread
# def disp():
#     print("this is threading running")
# t=Thread(target=disp)
# t.start()   


# from threading import Thread
# def disp(a,e):
#     print("this is threading running",a)
#     print("name is ",a+e)
# t=Thread(target=disp,args=(29,5))
# t.start()    

### single thread
# from time import sleep
# class a:
#     def run(self):
#         for i in range(5):
#             print('pratham')
#             sleep(1)
# class b:
#     def run(self):
#         for i in range(5):
#             print('hello')
#             sleep(1)
# object1=a()
# object2=b()
# object1.run()
# object2.run()

########### multithread
# from time import sleep
# from threading import Thread
# class a(Thread):
#     def run(self):
#         for i in range(5):
#             print('pratham')
#             sleep(1)
# class b(Thread):
#     def run(self):
#         for i in range(5):
#             print('hello')
#             sleep(1)
# object1=a()
# object2=b()
# object1.start()
# object2.start()
# object1.join()
# object2.join()
# print("main thread")            
