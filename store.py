import products  # importiere deine Product-Klasse


class Store:
    def __init__(self, products_list):
        self.products = products_list

    def add_product(self, product):
        """Add a new product to the store"""
        self.products.append(product)

    def remove_product(self, product):
        """Remove a product from the store"""
        if product in self.products:
            self.products.remove(product)

    def get_total_quantity(self):
        """Return the total quantity of all active products"""
        total = 0
        for p in self.products:
            if p.is_active():
                total += p.get_quantity()
        return total

    def get_all_products(self):
        """Return all active products"""
        return [p for p in self.products if p.is_active()]

    def order(self, shopping_list):
        """
        shopping_list = [(product, quantity), (product, quantity)]
        Buys all products and returns total price.
        """
        total_cost = 0
        for item in shopping_list:
            product, quantity = item
            total_cost += product.buy(quantity)
        return total_cost


# === TEST SECTION ===
def main():
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = Store(product_list)

    active_products = best_buy.get_all_products()
    print("Total quantity in store:", best_buy.get_total_quantity())

    total_price = best_buy.order([(active_products[0], 1), (active_products[1], 2)])
    print(f"Order cost: {total_price} dollars.")


if __name__ == "__main__":
    main()