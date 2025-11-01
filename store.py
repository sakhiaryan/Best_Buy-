from products import Product


class Store:
    """
    A store that holds multiple products and can place orders.
    """

    def __init__(self, products):
        """
        Initialize store with a list of Product instances.
        :param products: list of Product
        """
        if not isinstance(products, list):
            raise ValueError("products must be a list.")
        for p in products:
            if not isinstance(p, Product):
                raise ValueError("All items in products must be Product instances.")
        self.products = list(products)

    def add_product(self, product):
        """
        Add a product to the store.
        :param product: Product
        """
        if not isinstance(product, Product):
            raise ValueError("Can only add Product instances.")
        self.products.append(product)

    def remove_product(self, product):
        """
        Remove a product from the store.
        :param product: Product
        """
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """
        :return: total quantity of all products (sum of quantities)
        """
        return sum(p.get_quantity() for p in self.products)

    def get_all_products(self):
        """
        :return: list of active products
        """
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list):
        """
        Place an order.
        :param shopping_list: list of (Product, quantity)
        :return: total price (float)
        """
        if not isinstance(shopping_list, list) or not shopping_list:
            raise ValueError("shopping_list must be a non-empty list of (Product, quantity).")

        # Validate all lines first (no partial orders)
        for item in shopping_list:
            if not (isinstance(item, tuple) and len(item) == 2):
                raise ValueError("Each shopping item must be a (Product, quantity) tuple.")
            product, qty = item
            if not isinstance(product, Product):
                raise ValueError("First element of each tuple must be a Product.")
            if int(qty) <= 0:
                raise ValueError("Quantity in shopping list must be > 0.")
            if not product.is_active():
                raise Exception(f"Product is inactive: {product.name}")
            if product.get_quantity() < int(qty):
                raise Exception(f"Not enough stock for {product.name}. Requested {qty}, available {product.get_quantity()}.")

        # Perform buys (all validated)
        total = 0.0
        for product, qty in shopping_list:
            total += product.buy(int(qty))

        return total