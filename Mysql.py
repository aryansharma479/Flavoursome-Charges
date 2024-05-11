import Grocery
import Chinese
import Pizza
import Menu
import Sweets
import Mysql
import csv

def mysql_items():

    import mysql.connector
    mydb=mysql.connector.connect(host='localhost',user='root',passwd='admin',database='flavoursome')
    print(mydb)
    data=[]
    c="y"
    while (c=="y"):
        count=0
        s=0
        s_total=0
        cursor=mydb.cursor()
        n_item=input("ENTER NAME OF ITEM:")
        f_mrp=int(input("Enter Fixed Mrp:"))
        qty=int(input("Quantity Of Item:"))
        price=int(input("Price:"))
        amt=price*qty
        count+=amt
        s_amount=f_mrp-price
        s+=s_amount
        S_total=qty*f_mrp-amt
        s_total+=S_total
        details=(n_item,f_mrp,qty,price,amt,s,s_total)
        data.append(details)
        query="insert into Food(Name_of_item,Fixed_MRP,Quantity,Price,Amount,Saved_Amount,Total_SavedAmt)values(%s,%s,%s,%s,%s,%s,%s)"
        val=(n_item,f_mrp,qty,price,amt,s,s_total)
        cursor.execute(query,val)
        mydb.commit()
        print("RECORD HAS BEEN SUCCESSFULLY ENTERED INTO TABLE- FOOD OF DATABASE-> FLAVOURSOME CHARGES")
        fields=["NAME","FIXED MRP","QUANTITY","PRICE","AMOUNT","SAVED AMOUNT PER ITEM",
                "TOTAL SAVED AMOUNT"]
        filename="RANDOMITEMS.csv"
        with open(filename,'w',newline='')as f:
            csv_w=csv.writer(f,delimiter=',')
            csv_w.writerow(fields)
            csv_w.writerows(data)
        c=input("DO YOU WANT TO GO FURTHER OR NOT (y/n)? 'n' will display The Bill If data Given:")
        if c=='n':
            print("""
                      A.Grocery Station
                      B.Chinese corner
                      C.Pizza Station
                      D.Sweets Corner
                      E.Main Menu
                      F.Exit""")
            ch=input(" CHOOSE AMONG A,B,C,D,E or F:").upper()
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

