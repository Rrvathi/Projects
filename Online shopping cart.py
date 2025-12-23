# Online Shopping Cart using Python OOP

class Product:
    def __init__(self, pid, name, price):
        self.pid = pid
        self.name = name
        self.price = price


class ShoppingCart:
    def __init__(self):
        self.cart = {}   # pid -> quantity

    def add_item(self, product, qty):
        if product.pid in self.cart:
            self.cart[product.pid] += qty
        else:
            self.cart[product.pid] = qty
        print("✅ Item added to cart")

    def remove_item(self, pid):
        if pid in self.cart:
            del self.cart[pid]
            print("❌ Item removed from cart")
        else:
            print("Item not found in cart")

    def view_cart(self, products):
        if not self.cart:
            print("🛒 Cart is empty")
            return

        print("\n--- Your Cart ---")
        total = 0
        for pid, qty in self.cart.items():
            product = products[pid]
            cost = product.price * qty
            total += cost
            print(f"{product.name} x {qty} = ₹{cost}")
        print("Total: ₹", total)

    def checkout(self, products):
        self.view_cart(products)
        print("\n🙏 Thank you for shopping!")
        self.cart.clear()


class Shop:
    def __init__(self):
        self.products = {
            1: Product(1, "Mobile", 15000),
            2: Product(2, "Laptop", 50000),
            3: Product(3, "Headphones", 2000)
        }
        self.cart = ShoppingCart()

    def show_products(self):
        print("\n--- Available Products ---")
        for p in self.products.values():
            print(f"{p.pid}. {p.name} - ₹{p.price}")

    def start(self):
        while True:
            print("\n1. View Products")
            print("2. Add to Cart")
            print("3. Remove from Cart")
            print("4. View Cart")
            print("5. Checkout")
            print("6. Exit")

            try:
                choice = int(input("Enter choice: "))
            except ValueError:
                print("Invalid input")
                continue

            if choice == 1:
                self.show_products()

            elif choice == 2:
                pid = int(input("Enter Product ID: "))
                qty = int(input("Enter Quantity: "))
                if pid in self.products and qty > 0:
                    self.cart.add_item(self.products[pid], qty)
                else:
                    print("Invalid product or quantity")

            elif choice == 3:
                pid = int(input("Enter Product ID to remove: "))
                self.cart.remove_item(pid)

            elif choice == 4:
                self.cart.view_cart(self.products)

            elif choice == 5:
                self.cart.checkout(self.products)
                break

            elif choice == 6:
                print("Exited")
                break

            else:
                print("Invalid choice")


# Run Application
if __name__ == "__main__":
    shop = Shop()
    shop.start()