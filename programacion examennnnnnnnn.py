class User:
    def _init_(self, name, last_name, email, password):
        self.name = name
        self.last_name = last_name
        self.email = email
        self.password = password
        
class UserManager:
    def _init_(self):
        self.users = []

    def register_user(self, name, last_name, email, password):
        for user in self.users:
            if user.email == email:
                return False
        new_user = User(name, last_name, email, password)
        self.users.append(new_user)
        return True

    def login(self, email, password):
        for user in self.users:
            if user.email == email and user.password == password:
                return user
        return None

class Product:
    def _init_(self, product_id, name, price):
        self.id = product_id
        self.name = name
        self.price = price

    def _str_(self):
        return f"{self.id}. {self.name} - ${self.price}"

class Cart:
    def _init_(self):
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def show_cart(self):
        if not self.items:
            print("Cart is empty")
            return

        total = 0
        for product, quantity in self.items:
            subtotal = product.price * quantity
            total += subtotal
            print(f"{product.name} x{quantity} = ${subtotal}")
        print(f"Total: ${total}")

    def clear_cart(self):
        self.items.clear()

def main_menu():
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")
    
def store_menu():
    print("\n1. View products")
    print("2. Add product to cart")
    print("3. View cart")
    print("4. Clear cart")
    print("5. Logout")

user_manager = UserManager()

products = [
    Product(1, "Keyboard", 25),
    Product(2, "Mouse", 15),
    Product(3, "Monitor", 200)
]

while True:
    main_menu()
    option = input("Choose an option: ")

    if option == "1":
        name = input("Name: ")
        last = input("Last name: ")
        email = input("Email: ")
        password = input("Password: ")

        if user_manager.register_user(name, last, email, password):
            print("User registered successfully")
        else:
            print("Email already exists")

    elif option == "2":
        email = input("Email: ")
        password = input("Password: ")

        user = user_manager.login(email, password)
        if user:
            print(f"Welcome {user.name}")
            cart = Cart()

            while True:
                store_menu()
                choice = input("Choose: ")

                if choice == "1":
                    for p in products:
                        print(p)

                elif choice == "2":
                    product_id = int(input("Product ID: "))
                    quantity = int(input("Quantity: "))

                    for p in products:
                        if p.id == product_id:
                            cart.add_product(p, quantity)
                            print("Product added")
                            break

                elif choice == "3":
                    cart.show_cart()

                elif choice == "4":
                    cart.clear_cart()
                    print("Cart cleared")

                elif choice == "5":
                    print("Logged out")
                    break

        else:
            print("Invalid credentials")

    elif option == "3":
        print("Goodbye")
        break

    else:
        print("Invalid option")