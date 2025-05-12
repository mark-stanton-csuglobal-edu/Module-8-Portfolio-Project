# Class Definition - ItemToPurchase
class ItemToPurchase:
    def __init__(self, name = 'none', description = 'none', price = 0.00, quantity = 0):
        self.name = name
        self.description = description
        self.price = float(price)
        self.quantity = int(quantity)
    # Method - Print Item Cost
    def print_item_cost(self):
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${self.price * self.quantity:.2f}")

    # Method - Print Item Description
    def print_item_description(self):
        print(f"{self.name} - {self.description}")

# Class Definition - ShoppingCart
class ShoppingCart:
    def __init__(self, customer_name = 'none', current_date = 'January 1, 2020'):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    # Method - Add Item
    def add_item(self, item):
        self.cart_items.append(item)

    # Method - Remove Item
    def remove_item(self, name):
        found = False
        for item in self.cart_items:
            if item.name.lower() == name.lower():
                self.cart_items.remove(item)
                found = True
        if not found:
            print('Item not found in cart. Nothing removed.')

    # Method - Modify Item
    def modify_item(self, name, price = None, quantity = None, description = None):
        found = False
        for item in self.cart_items:
            if item.name.lower() == name.lower():
                if description is not None:
                    item.description = description
                if quantity is not None:
                    item.quantity = int(quantity)
                if price is not None:
                    item.price = float(price)
                found = True
        if not found:
            print('Item not found in cart. Nothing modified.')

    # Method - Get the Number of Items in Cart
    def get_num_items_in_cart(self):
        total_quantity = sum([item.quantity for item in self.cart_items])
        return total_quantity

    # Method - Get the Total Cost of the Cart
    def get_cost_of_cart(self):
        cart_cost = f"{sum(item.price * item.quantity for item in self.cart_items): .2f}"
        return cart_cost

    # Method - Print the Total Cost of the Cart
    def print_total(self):
        if not self.cart_items:
            print('SHOPPING CART IS EMPTY')
        else:
            print(self.customer_name + "'s Shopping Cart - " + self.current_date)
            print('Number of Items: ' + str(self.get_num_items_in_cart()))
            # Print the description, quantity, and price, and total for just that item
            for item in self.cart_items:
                print(item.name + ' ' + str(item.quantity) + ' @ $' + f"{item.price: .2f}" + ' = $' + f"{(item.quantity * item.price): .2f}")
            # Print the total for all items in cart
            print('Total: $' + str(self.get_cost_of_cart()))

    # Method - Print the descriptions for All Items in the Cart
    def print_description(self):
        print(self.customer_name + "'s Shopping Cart - " + self.current_date)
        print('Item Descriptions')
        for item in self.cart_items:
            #print(item.name + ' - ' + item.description)
            item.print_item_description()

def print_menu(cart):
    option = ''
    while option != 'q':
        print('MENU')
        print('a - Add item to cart')
        print('r - Remove item from cart')
        print('c - Change item')
        print('d - Output item descriptions')
        print('o - Output shopping cart')
        print('q - Quit')
        option = input('Choose an option: ').lower()
        # Add Item
        if option == 'a':
            name = input('Enter item name: ')
            description = input('Enter the item description: ')
            price = float(input('Enter the item price: '))
            quantity = int(input('Enter the item quantity: '))
            item = ItemToPurchase(name, description, price, quantity)
            cart.add_item(item)
        # Remove Item
        elif option == 'r':
            name = input('Enter the name of the item to remove: ')
            cart.remove_item(name)
        # Modify Item
        elif option == 'c':
            name = input('Enter the name of the item to modify: ')
            whatToChange = input('What would you like to modify? description, quantity, or price? ')
            # Modify Description
            if whatToChange  == 'description':
                newDescription = input('Enter the new description: ')
                cart.modify_item(name, description = newDescription)
            # Modify Quantity
            elif whatToChange  == 'quantity':
                newQuantity = int(input('Enter the new quantity: '))
                cart.modify_item(name, quantity = newQuantity)
            # Modify Price
            elif whatToChange  == 'price':
                newPrice = float(input('Enter the new price: '))
                cart.modify_item(name, price = newPrice)
        # Print Description
        elif option == 'd':
            cart.print_description()
        # Print Total
        elif option == 'o':
            cart.print_total()
        # Quit
        elif option == 'q':
            return
        # Invalid Input
        else:
            print('Invalid input. Please try again.')

# Main Code
def main():
# In the main section of your code, prompt the user for a customer's name and today's date. Output the name and date. Create an object of type ShoppingCart.
    customer_name = input('Enter the customer name: ')
    current_date = input('Enter the current date: ')

    print("Customer name: " + customer_name)
    print("Today's date: " + current_date)

    cart = ShoppingCart(customer_name, current_date)
    print_menu(cart)

main()

