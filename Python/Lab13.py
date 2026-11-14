inventory=["Notebook","Pen","Eraser","Ruler"]
print("======================================================================")
print("               INVENTORY CONTROL SYSTEM                               ")
print("======================================================================")
while True:
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add item")
    print("3. Remove Items")
    print("4. Sort Inventory")
    print("5. Exit")
    choice=int(input("Enter your choice: "))
    if choice==1:
        print("---Current Inventory--")
        for index,i in enumerate(inventory):
            print(index+1,i)
    elif choice==2:
        item=input("Enter itemm name to add :") 
        print("[SUCCESS] ""Marker"" added to inventory.") 
        inventory.append(item)      
    elif choice==3:
        item=input("Enter item name to remove: ")
        if item in inventory:
            inventory.remove(item)
        else:
            print("item not found")    
        print("[SUCCESS] pen is removed from inventory.")
    elif choice==4:
        inventory.sort()
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        print(inventory)    
    else:
        print("Exit") 
        break   



    