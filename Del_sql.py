import mysql.connector
import Grocery
import Chinese
import Pizza
import Sweets
import Menu

def Delete():
    mydb=mysql.connector.connect(host='localhost',user='root',
                                 passwd='admin',database='flavoursome')
    print(mydb)
    cursor=mydb.cursor()
    cursor.execute("Select*From Food")
    myrecords=cursor.fetchall()
    for i in myrecords:
        print(i)
    c='y'
    while c=='y':
        name=input("ENTER NAME TO BE DELETED FROM MYSQL DATA:")
        sql = "DELETE FROM food WHERE Name_of_item = %s"
        name = (name,)
        cursor.execute(sql, name)
        mydb.commit()
        print(cursor.rowcount, "record(s) deleted")
        c=input("Do You Want To Delete More From The Database?(y/n)").lower()
        if c=="n":
            print("""
    A.Grocery Station
    B.Chinese corner
    C.Pizza Station
    D.Sweets Corner
    E.Main Menu
    F.Exit""")
            ch=input(" CHOOSE AMONG A,B,C,D or E :").upper()
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
                print("Try Again")
                Menu.menu()
            if (c!=y):
                 print("WRONG INPUT GIVEN!")
                 Menu.menu()
            if (c!=n):
                print("WRONG INPUT GIVEN!")
                Menu.menu()
