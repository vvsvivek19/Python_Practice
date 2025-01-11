inventory = {}

# Display Inventory with Improved Formatting
def show_inventory(inventory):
    print("------------------------ Inventory ------------------------")
    print(f"{'Item'.ljust(15)} {'Quantity'.ljust(10)} {'Price'}")
    print("----------------------------------------------------------")
    for item_name in inventory:
        print(f"{item_name.ljust(15)} {str(inventory[item_name]['quantity']).ljust(10)} {inventory[item_name]['price']:.2f}")
    print("----------------------------------------------------------")
    
#function to add items in inventory
def add_item(inventory, item_name, quantity, price):
    item_name = item_name.lower()  # Normalize input
    if quantity < 0 or price < 0:
        print("Quantity or price cannot be negative!!!!!!")
        print("Enter valid details")
        return
    if item_name in inventory:
        print("Item already exists in inventory, updating its details")
        inventory[item_name]['quantity'] = quantity
        inventory[item_name]['price'] = price
    else:
        inventory[item_name] = {}
        inventory[item_name]['quantity'] = quantity
        inventory[item_name]['price'] = price

add_item(inventory,'Apple',10,7.5)
add_item(inventory,'Organes',11,9)
add_item(inventory,'Banana',12,8)

show_inventory(inventory)

# Enhanced Remove Item with Confirmation
def remove_item(inventory, item_name):
    item_name = item_name.lower()
    if item_name in inventory:
        confirm = input(f"Are you sure you want to delete {item_name}? (yes/no): ")
        if confirm.lower() == 'yes':
            del inventory[item_name]
            print(f"Item {item_name} removed.")
        else:
            print("Operation canceled.")
    else:
        print("Item doesn't exist in inventory.")
        
remove_item(inventory, 'Banana')
show_inventory(inventory)
remove_item(inventory, 'Guava')

#Functions to update quantity in inventory
def update_quantity(inventory, item_name, quantity):
    if quantity < 0:
        print("Quantity cannot be negative!!!!!!")
        print("Enter valid detail")
        exit() 
    if item_name in inventory:
        inventory[item_name]['quantity'] = quantity
    else:
        print("Item doesn't exist in inventory")
        
update_quantity(inventory,'Apple',50)
show_inventory(inventory)

#Calculating total value of the inventory
def calculate_total_value(inventory):
    sum = 0
    for item in inventory:
        sum = sum + inventory[item]['quantity'] * inventory[item]['price']
    return sum
total_value = calculate_total_value(inventory)
print(f"Total Inventory Value: ${total_value:.2f}")

def search_item(inventory,item_name):
    print(f"Searching {item_name}........... ")
    if item_name in inventory:
        print(f"{item_name} exists, below are the details")
        print(f"Item: {item_name}, Quantity: {inventory[item_name]['quantity']}, Price: {inventory[item_name]['price']}")
    else:
        print(f"{item_name} doesn't exists!!!!!!")

search_item(inventory,'Apple')
    
