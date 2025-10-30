import products
import store


def start(store_obj):
    while True:
        print("\n=== Welcome to Best Buy Store ===")
        print("1. List all products in store")
        print("2. Show total amount in store")
        print("3. Make an order")
        print("4. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("\n--- Available Products ---")
            for p in store_obj.get_all_products():
                p.show()

        elif choice == "2":
            print("\n--- Total Quantity in Store ---")
            print(f"Total items: {store_obj.get_total_quantity()}")

        elif choice == "3":
            print("\n--- Make an Order ---")
            products_list = store_obj.get_all_products()

            for i, product in enumerate(products_list, start=1):
                print(f"{i}. {product.name} (Price: {product.price}, Quantity: {product.quantity})")

            shopping_list = []
            while True:
                product_number = input("\nEnter product number (or 'done' to finish): ")
                if product_number.lower() == "done":
                    break

                try:
                    product_index = int(product_number) - 1
                    if product_index < 0 or product_index >= len(products_list):
                        print("Invalid product number.")
                        continue

                    quantity = int(input("Enter quantity: "))
                    product = products_list[product_index]
                    shopping_list.append((product, quantity))
                except ValueError:
                    print("Please enter a valid number.")
                    continue

            if shopping_list:
                try:
                    total_price = store_obj.order(shopping_list)
                    print(f"\n✅ Order successful! Total cost: {total_price} dollars.")
                except Exception as e:
                    print(f"❌ Order failed: {e}")

        elif choice == "4":
            print("\nThank you for visiting Best Buy! 👋")
            break

        else:
            print("Invalid choice. Please try again.")


def main():
    # setup initial stock of inventory
    product_list = [
        products.Product("MacBook Air M2", price=1450, quantity=100),
        products.Product("Bose QuietComfort Earbuds", price=250, quantity=500),
        products.Product("Google Pixel 7", price=500, quantity=250),
    ]

    best_buy = store.Store(product_list)
    start(best_buy)


if __name__ == "__main__":
    main()