import csv
import time
import datetime
import Grocery
import Pizza
import Chinese
import Sweets
import Menu
import mysql.connector 
import pandas as pd
mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='flavoursome')
cursor=mydb.cursor()

def chinesefood():
        print("\n\n_____WELCOME TO CHINESE CORNER_______\n\n")
        print("")
        time.sleep(1)
        print("")
        t_date=datetime.datetime.now()
        print("TODAY IS:",t_date)
        data=[]
        c="y"
        while (c=="y"):
            print("1.To Add Item ")
            print("2.To Delete Item From First")
            print("3.To Delete Item In between ")
            ch=int(input("Enter Your Choice :"))
            if (ch==1):
                item=int(input("""
                                  1.Drinks
                                  2.Chinese Food Items
                                  CHOOSE 1 or 2 :"""))
                if (item==1):
                        
                        count=0
                        s=0
                        s_total=0
                        name=input("Enter Name Of Drink:")
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
                        data.append(details)
                        query="insert into Food(Name_of_item,Fixed_MRP,Quantity,price,Amount,Saved_Amount,Total_SavedAmt)values(%s,%s,%s,%s,%s,%s,%s)"
                        val=(name,f_mrp,qty,price,amt,s,s_total)
                        cursor.execute(query,val)
                        mydb.commit()
                        print("RECORD HAS BEEN SUCCESSFULLY ENTERED INTO TABLE- FOOD OF DATABASE-> FLAVOURSOME")
                if(item==2):
                        
                        count=0
                        s=0
                        s_total=0
                        
                        name=input("Enter Name Of Chinese Item:")
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
                        data.append(details)
                        query="insert into Food(Name_of_item,Fixed_MRP,Quantity,price,Amount,Saved_Amount,Total_SavedAmt)values(%s,%s,%s,%s,%s,%s,%s)"
                        val=(name,f_mrp,qty,price,amt,s,s_total)
                        cursor.execute(query,val)
                        mydb.commit()
                        print("RECORD HAS BEEN SUCCESSFULLY ENTERED INTO TABLE- FOOD OF DATABASE-> FLAVOURSOME")
                        
            elif (ch==2):
                if (data==[]):
                    print("Queue Empty")
                else:
                    print("DELTED ELEMENT IS:",data[0])
                    data.pop(0)
                    name=input("ENTER ABOVE NAME OF ITEM TO BE DELETED FROM MYSQL DATA:")
                    sql = "DELETE FROM food WHERE Name_of_item = %s"
                    name = (name,)
                    cursor.execute(sql, name)
                    mydb.commit()
                    print(cursor.rowcount, "record(s) deleted")
                    
                    
                    
            elif (ch==3):
                index=int(input("ENTER THE INDEX OF THE ITEM YOU WANT TO REMOVE"))
                print("DELTED ELEMENT IS:",data[index])
                data.pop(index)
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
                            Menu.menu()
                    elif(data!=[]):
                            df=pd.DataFrame((data),columns=['Name Of Items','Fixed Mrp','Qty','Price','Amount','Saved_Amt','Total Saved Amount'])
                            print(df)
                            print("TOTAL AMOUNT=",count)
                            fields=["NAME","FIXED MRP","QUANTITY","PRICE","AMOUNT","SAVED AMOUNT PER ITEM","TOTAL SAVED AMOUNT"]
                            
                            filename="CHINESEITEMS.csv"
                            with open(filename,'w',newline='')as f:
                                csv_w=csv.writer(f,delimiter=',')
                                csv_w.writerow(fields)
                                csv_w.writerows(data)
                            print("""
                                        A.Grocery Station
                                        B.Chinese corner
                                        C.Pizza Station
                                        D.Sweets Corner
                                        E.Main Menu
                                        F.Exit""")
                            ch=input("Choose Among A,B,C,D,E or F :").upper()
                            if ch== "A" :
                                Grocery.GroceryScreen()
                            elif ch== "B" :
                                Chinese.chinesefood()
                            elif ch== "C" :
                                Pizza.pizza()
                            elif ch=="D":
                                Sweets.sweetscorner()
                            elif ch=="E":
                                Menu.menu()
                            elif ch=="F":
                                exit()
                            else:
                                    print("TRY AGAIN")
                                    Menu.menu()

