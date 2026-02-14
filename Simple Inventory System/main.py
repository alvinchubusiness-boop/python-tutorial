class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)

    def display_info(self):
        print(f"Product: {self.name} | Price: ${self.price:.2f} | Qty: {self.quantity}")

    def update_quantity(self, amount):
        """
        amount > 0  -> restock
        amount < 0  -> sold
        """
        new_qty = self.quantity + amount
        if new_qty < 0:
            raise ValueError(f"Not enough stock for {self.name}. Current qty={self.quantity}")
        self.quantity = new_qty

def add_product(inventory, name, price, quantity):
    inventory.append(Product(name, price, quantity))

def total_inventory_value(inventory):
    return sum(p.price * p.quantity for p in inventory)

def main():
    inventory = []

    add_product(inventory, "Apple", 0.50, 100)
    add_product(inventory, "Milk", 4.99, 20)
    add_product(inventory, "Bread", 2.79, 30)

    print("=== Initial Inventory ===")
    for p in inventory:
        p.display_info()

    print("\n=== Updates ===")
    inventory[0].update_quantity(-10) 
    inventory[1].update_quantity(+5)  
    inventory[2].update_quantity(-3)  

    for p in inventory:
        p.display_info()

    total = total_inventory_value(inventory)
    print(f"\nTotal inventory value: ${total:.2f}")

    return total

main()
