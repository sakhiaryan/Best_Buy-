class Product:
    def __init__(self, name: str, price: float, quantity: int):
        if not name:
            raise ValueError("Product name cannot be empty.")
        if price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = price
        self.quantity = quantity
        self.active = True

    def get_quantity(self) -> int:
        return self.quantity

    def set_quantity(self, quantity: int):
        if quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = quantity
        if quantity == 0:
            self.deactivate()

    def is_active(self) -> bool:
        return self.active

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def show(self):
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity}")

    def buy(self, quantity: int) -> float:
        if not self.active:
            raise Exception(f"Cannot buy inactive product: {self.name}")
        if quantity <= 0:
            raise ValueError("Quantity must be greater than 0.")
        if quantity > self.quantity:
            raise Exception(f"Not enough stock for {self.name}.")

        total_price = self.price * quantity
        self.quantity -= quantity

        if self.quantity == 0:
            self.deactivate()

        return total_price


# === TEST SECTION ===
def main():
    bose = Product("Bose QuietComfort Earbuds", price=250, quantity=500)
    mac = Product("MacBook Air M2", price=1450, quantity=100)

    print(bose.buy(50))     # Should print 12500
    print(mac.buy(100))     # Should print 145000
    print(mac.is_active())  # Should print False, because quantity=0

    bose.show()
    mac.show()

    bose.set_quantity(1000)
    bose.show()


if __name__ == "__main__":
    main()