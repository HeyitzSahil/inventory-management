def add_item(item, price, stock):
    if item in inventory:
        print(f"Error: Item '{item}' already exists.")
    else:
        inventory[item]={
            'price': price,
            'stock': stock
        }
        print(f"Item '{item}' added successfully.")
    pass

def update_stock(item, quantity):
    if item not in inventory:
        print(f"Error: Item '{item}' not found.")
    else:
        
        if (inventory[item]['stock'] + quantity) < 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            inventory[item]['stock'] += quantity
            print(f"Stock for '{item}' updated successfully.")
    pass

def check_availability(item):
    if item not in inventory:
        return "Item not found"
    else:
        return inventory[item]['stock']
    
def sales_report(sales):
    total_sales = 0
    for item in sales:
        if item not in inventory:
            print(f"Error: Item '{item}' not found.")
        elif inventory[item]['stock'] <= 0:
            print(f"Error: Insufficient stock for '{item}'.")
        else:
            total_sales = total_sales + (sales[item] * inventory[item]['price'])
            inventory[item]['stock'] -= sales[item]
    return f"Total revenue: ${total_sales:.2f}"

inventory = {}
add_item("Apple", 0.5, 50)
add_item("Banana", 0.2, 60)
sales = {"Apple": 30, "Banana": 20, "Orange": 10}  
print(sales_report(sales)) 
update_stock("Kiwi", 50)
update_stock("Apple", 20)
print(inventory)