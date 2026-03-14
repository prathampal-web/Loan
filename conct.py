# import mysql.connector

   
# mydb = mysql.connector.connect(
#         host="localhost",  
#         user="root",
#         password="root", 
#         database="dell_db")
   
# print("successful")

# import mysql.connector
# from mysql.connector import Error

# print("Start")

# try:
#     mydb = mysql.connector.connect(
#         host="127.0.0.1",
#         user="root",
#         password="root",
#         database="dell_db",
#         connection_timeout=5
#     )

#     print("After connect")

#     if mydb.is_connected():
#         print("Connection Successful ✅")

# except Exception as e:
#     print("Error:", e)

# print("End")

# print("hello")

import mysql.connector

print("Start")

try:
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        # database="dell_db"
        database="caddcenter"
        
    )
    cur=mydb.cursor()
    # cur.execute("create database caddcenter") ### create database
    # cur.execute("create table emp(Name varchar(30),Post varchar(30),Salery int(30))")#### create table
    # s="insert into emp(Name,Post,Salery) values(%s,%s,%s)" ## insert data
    # b=("uzma1","teacher",80000),("pratham","student",45000),("pratham1","student",45000)
    # cur.executemany(s,b)
    
    ########## taking input
    
    # name=input("enter name")
    # post=input("enter post")
    # saler=int(input("enter salery"))
    # s="insert into emp(Name,Post,Salery) values(%s,%s,%s)"
    # b=(name,post,saler)
    # cur.execute(s,b)
    
    
    ########### taking input with forloop
    # for i in range(2):
    #      name=input("enter name")
    #      post=input("enter post")
    #      saler=int(input("enter salery"))
    #      s="insert into emp(Name,Post,Salery) values(%s,%s,%s)"
    #      b=(name,post,saler)
    #      cur.execute(s,b)
    #      print("\n ")     
    
    ############## fetch data
    # s="select *from emp"
    # cur.execute(s)
    # r=cur.fetchall()
    # print(r)
    ############## fetch data with for loop
    
    # s="select *from emp"
    # cur.execute(s)
    # r=cur.fetchall()
    # for i in r:
    #     for j in i:
    #         print(j,end="  ")
    #     print("\n")    
    
    
    ############## update data
    # s='update emp set Name="uzma Parveen" where Name="uzma"'
    # cur.execute(s)
    ############## update data
    
    s='delete  from emp where Name="uzma Parveen"'
    cur.execute(s)
    
    print("Connected Successfully ✅")
    mydb.commit()

except Exception as e:
    print("Error:", e)

print("End")




