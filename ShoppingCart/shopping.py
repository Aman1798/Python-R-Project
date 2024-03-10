import json

# Define the base class Product
class Product:
    def __init__(self, name, price, quantity, identifier, brand):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.identifier = identifier
        self.brand = brand

    # Convert the product to a JSON-formatted string
    def to_json(self):
        product_json = {
            "name": self.name,
            "price": self.price,
            "quantity": self.quantity,
            "identifier": self.identifier,
            "brand": self.brand
        }
        return json.dumps(product_json)

# Define a subclass Clothing with additional attributes
class Clothing(Product):
    def __init__(self, name, price, quantity, identifier, brand, size, material):
        super().__init__(name, price, quantity, identifier, brand)
        self.size = size
        self.material = material

    # Override the to_json method to include additional attributes
    def to_json(self):
        clothing_json = super().to_json()
        clothing_json = json.loads(clothing_json)
        clothing_json["size"] = self.size
        clothing_json["material"] = self.material
        return json.dumps(clothing_json)

# Define a subclass Food with additional attributes
class Food(Product):
    def __init__(self, name, price, quantity, identifier, brand, expiry_date, gluten_free, suitable_for_vegans):
        super().__init__(name, price, quantity, identifier, brand)
        self.expiry_date = expiry_date
        self.gluten_free = gluten_free
        self.suitable_for_vegans = suitable_for_vegans

    # Override the to_json method to include additional attributes
    def to_json(self):
        food_json = super().to_json()
        food_json = json.loads(food_json)
        food_json["expiry_date"] = self.expiry_date
        food_json["gluten_free"] = self.gluten_free
        food_json["suitable_for_vegans"] = self.suitable_for_vegans
        return json.dumps(food_json)

# Define a subclass Electronics with additional attributes
class Electronics(Product):
    def __init__(self, name, price, quantity, identifier, brand, power_source, weight):
        super().__init__(name, price, quantity, identifier, brand)
        self.power_source = power_source
        self.weight = weight

    # Override the to_json method to include additional attributes
    def to_json(self):
        electronics_json = super().to_json()
        electronics_json = json.loads(electronics_json)
        electronics_json["power_source"] = self.power_source
        electronics_json["weight"] = self.weight
        return json.dumps(electronics_json)

# Define the ShoppingCart class to manage products in a shopping cart
class ShoppingCart:
    def __init__(self):
        self.cart = []

    # Add a product to the cart
    def add_product(self, product):
        self.cart.append(product)

    # Remove a product from the cart
    def remove_product(self, product_identifier):
        self.cart = [p for p in self.cart if p.identifier != product_identifier]

    # Get the contents of the cart and sort them alphabetically by product name
    def get_contents(self):
        sorted_cart = sorted(self.cart, key=lambda p: p.name)
        return sorted_cart

    # Change the quantity of a product in the cart
    def change_product_quantity(self, product_identifier, quantity):
        for product in self.cart:
            if product.identifier == product_identifier:
                product.quantity = quantity

# Start the program
print('The program has started.\n')
print('Insert your next command (H for help):\n')
terminated = False

# Create an instance of the ShoppingCart class to represent the shopping cart
shopping_cart = ShoppingCart()

# Main program loop
while not terminated:
    command = str(input("Type your next command: "))
    
    # Handle adding a product to the cart   
    if command == 'A' or command == 'a':
        print("Adding a new product:")
        product_type = input("Insert its type (Clothing, Food, or Electronics): ")
        name = str(input("Insert its name: "))
        price = float(input("Insert its price (£): "))
        quantity = int(input("Insert its quantity: "))
        brand = str(input("Insert its brand: "))
        identifier = str(input("Insert its EAN code: "))
        
        if product_type == 'Clothing' or product_type == 'clothing':
            size = input("Insert its size: ")
            material = input("Insert its material: ")
            product = Clothing(name, price, quantity, identifier, brand, size, material)
        elif product_type == 'Food' or product_type == 'food':
            expiry_date = input("Insert expiry date: ")
            gluten_free = input("Is it gluten-free (True/False): ").lower() == 'true'
            suitable_for_vegans = input("Is it suitable for vegans (True/False): ").lower() == 'true'
            product = Food(name, price, quantity, identifier, brand, expiry_date, gluten_free, suitable_for_vegans)
        elif product_type == 'Electronics' or product_type == 'electronics':
            power_source = input("Insert power source (Battery, Electricity, or Solar): ")
            weight = float(input("Insert weight (in grams): "))
            product = Electronics(name, price, quantity, identifier, brand, power_source, weight)
        else:
            print("Invalid product type.")
            continue

        shopping_cart.add_product(product)
        print(f"The product {product.name} has been added to the cart.")
        print(f"The cart contains {len(shopping_cart.cart)} products.")
    
    # Handle removing a product from the cart
    elif command == 'R' or command == 'r':
        identifier = input("Insert EAN code to remove product: ")
        shopping_cart.remove_product(identifier)        
        print(f"The product with EAN code {identifier} has been removed from the cart.")
        print(f"The cart contains {len(shopping_cart.cart)} products.")
    
    # Handle printing a summary of the cart
    elif command == 'S' or command == 's':
        print("This is the total of the expenses:")
        total_expenses = 0
        for idx, product in enumerate(shopping_cart.get_contents(), start=1):
            product_total = product.price * product.quantity
            total_expenses += product_total            
            if product.quantity > 1:
                print(f"{idx} - {product.quantity} * {product.name} = £{product_total:.2f}")
            else:
                print(f"{idx} - {product.name} = £{product_total:.2f}")

        print(f"Total = £{total_expenses:.2f}")
    
    # Handle changing the quantity of a product
    elif command == 'Q' or command == 'q':        
        identifier = input("Insert product identifier to change quantity: ")
        quantity = int(input("Insert new quantity: "))
        shopping_cart.change_product_quantity(identifier, quantity)
    
    # Handle exporting the cart in JSON format
    elif command == 'E' or command == 'e':        
        cart_contents = [product.to_json() for product in shopping_cart.cart]
        cart_json = json.dumps(cart_contents, indent=7)
        
        # Remove backslashes from the JSON string
        cart_json = cart_json.replace("\\", "")
        
        print(cart_json)
    
    elif command == 'T' or command == 't':
        terminated = True
        print('Goodbye. ')
    
    # Print the list of supported commands 
    elif command == 'H' or command == 'h':               
        print('''The program supports the following commands:
  [A] - Add a new product to the cart
  [R] - Remove a product from the cart
  [S] - Print a summary of the cart
  [Q] - Change the quantity of a product
  [E] - Export a JSON version of the cart
  [T] - Terminate the program
  [H] - List the supported commands''')
    
    else:
        print('Command not recognized. Please try again.')



'''

References:-
https://www.geeksforgeeks.org/
        
'''