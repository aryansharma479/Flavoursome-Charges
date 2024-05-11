import csv
import time
import datetime
import Chinese
import Pizza
import Menu
import Grocery
import Sweets
import mysql.connector
import pandas as pd
mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='flavoursome') #Connected To Mysql
cursor=mydb.cursor()


def GroceryScreen():
        print(""" WE WELCOME YOU TO OUR GROCERY STATION""")
        print("")
        time.sleep(1)


        print("""                 1. PLEASE FEEL FREE FOR EXCHANGE/ RETURN
                 2. KINDLY CHECK THE GOODS ON DELIVERY NO RESPONSIBILTY AFTERWARDS
                 3.IF YOU ARE NOT SATISFIED WITH US TELL US AND IF YES TELL  OTHERS 
                 CUSTOMER CARE Ph.no.- 9650615424 Or Order Ph.no -011-22137600 """)
        time.sleep(1)
        t_date=datetime.datetime.now() #Mentions Today's Date And Time 
        print("TODAY IS:",t_date)
        data=[] #Empty List
        count=0
        s=0
        s_total=0
        c="y"
        while (c=="y"):
            print("1.To Add Item ")
            print("2.To Delete Item From First")
            print("3.To Delete Item In between ")
            
            ch=int(input("Enter Your Choice :"))
            if (ch==1):
                name=input("Enter Name Of Item:")
                f_mrp=int(input("Enter Fixed Price Of The Item:"))
                qty=int(input("Enter Quantity :"))
                price=int(input("Enter Price Of The Item:"))
                amt=price*qty
                count+=amt
                s_amount=f_mrp-price
                s+=s_amount
                S_total=qty*f_mrp-amt
                s_total+=S_total
                details=(name,f_mrp,qty,price,amt,s,s_total)
                data.append(details)     # Details Added To List-Data
                print(data)                                                                                           #%s Are Place Holders
                query="insert into Food(Name_of_item,Fixed_MRP,Quantity,price,Amount,Saved_Amount,Total_SavedAmt)values(%s,%s,%s,%s,%s,%s,%s)"
                val=(name,f_mrp,qty,price,amt,s,s_total)
                cursor.execute(query,val)  #Execution Takes Place
                mydb.commit()    #Entered Into Database
                print("RECORD HAS BEEN SUCCESSFULLY ENTERED INTO TABLE- FOOD OF DATABASE-> FLAVOURSOME")
            elif (ch==2):
                if (data==[]):
                    print("Queue Empty")
                    
                else:
                    print("DELTED ELEMENT IS:",data[0])
                    data.pop(0) #Element Deleted From 0 Index
                    name=input("ENTER ABOVE NAME OF ITEM TO BE DELETED FROM MYSQL DATA:")
                    sql = "DELETE FROM food WHERE Name_of_item = %s"
                    name = (name,)
                    cursor.execute(sql, name)
                    mydb.commit()
                    print(cursor.rowcount, "record(s) deleted")
            elif (ch==3):
                index=int(input("ENTER THE INDEX OF THE ITEM YOU WANT TO REMOVE(0 index being the 1st item):"))
                print("DELTED ELEMENT IS:",data[index])
                data.pop(index)  #Element Deleted From Mentioned Index By The User
                name=input("ENTER ABOVE NAME OF ITEM TO BE DELETED FROM MYSQL DATA:")
                sql = "DELETE FROM food WHERE Name_of_item = %s"
                name = (name,)
                cursor.execute(sql, name)
                mydb.commit()
                print(cursor.rowcount, "record(s) deleted")
            
            c=input("DO YOU WANT TO GO FURTHER OR NOT (y/n)? 'n' will display The Bill If data Given:")
            if c=="n":
                if (data==[]):
                            print("No Data Given")
                            Menu.menu() #Returns To Main Menu
                elif(data!=[]):
                            df=pd.DataFrame((data),columns=['Name Of Items','Fixed Mrp','Qty','Price','Amount','Saved_Amt','Total Saved Amount'])
                            print(df)
                            print("TOTAL AMOUNT=",count)
                            print("TOTAL SAVED AMOUNT OF CUSTOMER=",s_total)
                            fields=["NAME","FIXED MRP","QUANTITY","PRICE","AMOUNT","SAVED_Amt Per Item","TOTAL SAVED AMOUNT"]
                            filename="GROCERYITEMS.csv"  
                            with open(filename,'w',newline='')as f:
                                csv_w=csv.writer(f,delimiter=',')
                                csv_w.writerow(fields) #Fields Are Added 
                                csv_w.writerows(data)  #Data Is Added
                            print("""
                                        A.Grocery Station
                                        B.Chinese corner
                                        C.Pizza Station
                                        D.Sweets Corner
                                        E.Main Menu
                                        F.Exit""")
                            ch=input(" CHOOSE AMONG A,B,C,D,E or F :").upper()
                            if ch== "A" :
                                Grocery.GroceryScreen()      #Returns To Grocery Screen
                            elif ch== "B" :
                                Chinese.chinesefood()        #Returns To Chinese Corner
                            elif ch== "C" :
                                Pizza.pizza()                #Returns To Pizza   Station
                            elif ch=="D":
                                Sweets.sweetscorner()        #Returns To Sweets  Corner
                            elif ch=="E":
                                Menu.menu()                  #Returns To Main Menu
                            elif ch=="F":
                                exit()                       #EXITS
                            else:
                                    print("TRY AGAIN!")
                                    Menu.menu()

