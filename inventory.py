import time

import random

global item_id
item_id = 2



global products
products = [["1","chips",15,"solid","20g",12]]



    
#menu for navigation
def start():
    print("")
    print("Welcome to Inventory Manager")
    print("Enter 1 to view items")
    print("Enter 2 to add an item")
    print("Enter 3 to remove an item")
    print("Enter 4 to update an item")
    print("Enter 5 to search an item")
    print("Enter 6 to exit")
    
    
    choice = int(input("Enter your choice: "))
    
    if choice == 1:
        print_items()
    elif choice == 2:
        add()
    elif choice == 3:
        remove()
    elif choice == 4:
        update()
    elif choice == 5:
        search()
    elif choice == 6:
        print("Thank you for using Inventory Manager")
        
        
        

    
    
        
        
        
def search():
    #code to search item
    print("Enter item name to search: ")
    item_name = input("")
    for i in range(len(products)):
        if products[i][1] == item_name:
            print("Item found:")
            print(products[i])
            time.sleep(1)
            start()
            
            
    print("Item not found")
    input("Press enter to continue...")
    start()
        
        
        
def update():
    #code to update item
    print("Enter item name to update: ")
    item_name = input("")
    for i in range(len(products)):
        if products[i][1] == item_name:
            print("Enter new details of",item_name)
            products[i][0] = make_id()
            products[i][1] = input("Enter new name: ")
            products[i][2] = int(input("Enter new quantity: "))
            products[i][3] = input("Enter new type: ")
            products[i][4] = int(input("Enter new weight: "))
            products[i][5] = float(input("Enter new price: "))
            print("Item updated successfully")
            input("Press enter to continue...")
            start()
    print("Item not found")
    input("Press enter to continue...")
    start()
        

def check_unique():
        for product in products:
            if product[0] == item_id:
                print("Item ID already exists, please enter a unique ID")
                input("Press enter to continue...")
                add()
        print("Item number accepted")     

 
    

def add():
    #code to add item
    global item_id 
    check_unique()
    global item_name 
    item_name = input("Enter item name: ")
    global item_quantity 
    item_quantity = int(input("Enter item quantity: "))
    global item_type 
    item_type = input("Enter item type: ")
    global item_weight
    item_weight = float(input("Enter item weight: "))
    global item_price 
    item_price = float(input("Enter item price: "))
    
    products.append([item_id,item_name,item_quantity,item_type,item_weight,item_price])
    item_id += 1
    print("Item added successfully")
    input("Press enter to continue...")
    start()
    

def remove():
    #code to remove item
    print("Enter item name to remove: ")
    remove = input("")
    def search_1 (arr, target):
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if (arr[i][j] == target):
                    del(products[i])
                    print(f"Item {target} removed successfully")
                    input("Press enter to continue...")
                    start()
        print("Item not found")
    
    # Driver code
    arr = products
    target = remove
    
    search_1(arr, target)
    
    



def print_items():
    #code to print all items
    print("All items:")
    
    for i in products:
        for j in products:
            print(products[i][j], end="|")
    input("Press enter to continue...")
    start()
    
    
    
    
    
   
        




start()       


        