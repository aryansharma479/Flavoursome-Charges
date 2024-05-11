import Grocery
import Chinese
import Pizza
import Menu
import Sweets
import time
import Mysql
import Del_sql

def menu():
        print("************MAIN MENU**************")
        time.sleep(1)
        print()
        print("""
                 PRESS E IF YOU WANT TO ADD YOUR ITEMS ON MYSQL-PYTHON CONNECTOR
                """)
        
        ch= input("""
                      A: Visit Grocery Station 
                      B: Visit Chinese Food Corner
                      C: Visit Pizza Station
                      D: Visit Sweets Corner
                      E: Directly Enter Items Using Mysql Connector
                      F: Directly Delete Items From Mysql Database
                      G: Exit
                      Please enter your choice: """).upper()
        if ch== "A" :
                Grocery.GroceryScreen()
        elif ch== "B" :
                Chinese.chinesefood()
        elif ch== "C" :
                Pizza.pizza()
        elif ch=="D":
                Sweets.sweetscorner()
        elif ch=="E":
                Mysql.mysql_items()
        elif ch=="F":
                Del_sql.Delete()
        elif ch=="G":
                exit()
        else:
            print("You must only select either A,B,C,D,E,F or G")
            print("Please try again")
            Menu.menu()
        
