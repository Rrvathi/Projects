# ----------- Product class -------------
class Product:
    def __init__(self, id, name, price):
        self.id = id
        self.name = name
        self.price = price

    def __str__(self):
        return f"{self.id}. {self.name} - ₹{self.price}"


# ----------- CartItem class -------------
class CartItem:
    def __init__(self, product, qty=1):
        self.product = product
        self.qty = qty

    def increase(self, n=1):
        self.qty += n

    def decrease(self, n=1):
        self.qty = max(0, self.qty - n)

    def subtotal(self):
        return self.product.price * self.qty


# ----------- ShoppingCart class ----------
class ShoppingCart:
    def __init__(self):
        self.items = {}   # product_id -> CartItem

    def add(self, product, qty=1):
        if product.id in self.items:
            self.items[product.id].increase(qty)
        else:
            self.items[product.id] = CartItem(product, qty)
        print(f"Added {qty} x {product.name} to cart.")

    def remove(self, product_id):
        if product_id in self.items:
            del self.items[product_id]
            print("Item removed from cart.")
        else:
            print("Product not found in cart.")

    def view_cart(self):
        if not self.items:
            print("Cart is empty.")
            return

        print("\n------- Your Cart -------")
        for item in self.items.values():
            print(f"{item.product.name} x {item.qty} = ₹{item.subtotal()}")
        print("-------------------------")

    def total(self):
        return sum(item.subtotal() for item in self.items.values())


# ----------- Main Program ---------------
products = [
    Product(1, "Watch", 20000),
    Product(2, "Jeans", 2000),
    Product(3, "Cap", 300),
    Product(4, "Goggles", 1500)
]

cart = ShoppingCart()

# Add products
cart.add(products[0], 2)
cart.add(products[1], 1)

# View cart
cart.view_cart()

# Print total
print("Total Amount: ₹", cart.total())
