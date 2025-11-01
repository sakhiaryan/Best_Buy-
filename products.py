class Product:
    """
    Represents a product in the store inventory.
    Holds name, price, quantity, and active status.
    """

    def __init__(self, name, price, quantity):
        """
        Create a product.
        :param name: non-empty string
        :param price: non-negative float/int
        :param quantity: non-negative int
        """
        if not name or not isinstance(name, str):
            raise ValueError("Product name must be a non-empty string.")
        if price is None or price < 0:
            raise ValueError("Price cannot be negative.")
        if quantity is None or quantity < 0:
            raise ValueError("Quantity cannot be negative.")

        self.name = name
        self.price = float(price)
        self.quantity = int(quantity)
        self.active = True

    # -------- getters / setters --------
    def get_quantity(self):
        """Return current quantity (int)."""
        return self.quantity

    def set_quantity(self, quantity):
        """
        Set quantity; deactivates the product when it reaches 0.
        :param quantity: non-negative int
        """
        if quantity is None or quantity < 0:
            raise ValueError("Quantity cannot be negative.")
        self.quantity = int(quantity)
        if self.quantity == 0:
            self.deactivate()
        elif not self.active:
            # if quantity restored above 0, ensure active again
            self.activate()

    # -------- active state --------
    def is_active(self):
        """Return True if product is active, else False."""
        return self.active

    def activate(self):
        """Activate the product."""
        self.active = True

    def deactivate(self):
        """Deactivate the product."""
        self.active = False

    # -------- UI helpers --------
    def show(self):
        """Print a user-friendly line describing the product."""
        status = "ACTIVE" if self.active else "INACTIVE"
        print(f"{self.name}, Price: {self.price}, Quantity: {self.quantity} [{status}]")

    # -------- business logic --------
    def buy(self, quantity):
        """
        Buy a certain quantity of this product.
        Uses getters/setters to keep encapsulation.
        :param quantity: int > 0
        :return: total price (float)
        """
        if not self.is_active():
            raise Exception(f"Cannot buy inactive product: {self.name}")
        if quantity is None or int(quantity) <= 0:
            raise ValueError("Quantity to buy must be greater than 0.")

        quantity = int(quantity)
        current = self.get_quantity()
        if quantity > current:
            raise Exception(f"Not enough stock for {self.name}. Requested {quantity}, available {current}.")

        total_price = self.price * quantity
        self.set_quantity(current - quantity)
        return total_price

    # -------- nice repr --------
    def __repr__(self):
        return f"Product(name={self.name!r}, price={self.price}, quantity={self.quantity}, active={self.active})"