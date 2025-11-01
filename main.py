import products
import store


def print_menu():
    print("\n=== Welcome to Best Buy Store ===")
    print("1. List all products in store")
    print("2. Show total amount in store")
    print("3. Make an order")
    print("4. Quit")


def list_products(store_obj):
    print("\n--- Available Products ---")
    items = store_obj.get_all_products()
    if not items:
        print("No active products.")
        return
    for p in items:
        p.show()


def show_total(store_obj):
    print("\n--- Total Quantity in Store ---")
    print(f"Total items: {store_obj.get_total_quantity()}")


def make_order(store_obj):
    print("\n--- Make an Order ---")
    products_list = store_obj.get_all_products()
    if not products_list:
        print("No active products to order.")
        return

    for i, product in enumerate(products_list, start=1):
        print(f"{i}. {product.name} (Price: {product.price}, Quantity: {product.get_quantity()})")

    shopping_list = []
    while True:
        product_number = input("\nEnter product number (or 'done' to finish): ").strip()
        if product_number.lower() == "done":
            break

        if not product_number.isdigit():
            print("Please enter a valid product number.")
            continue

        idx = int(product_number) - 1
        if idx < 0 or idx >= len(products_list):
            print("Invalid product number.")
            continue

        qty_str = input("Enter quantity: ").strip()
        if not qty_str.isdigit():
            print("Please enter a valid quantity.")
            continue

        qty = int(qty_str)
        shopping_list.append((products_list[idx], qty))

    if not shopping_list:
        print("No items selected.")
        return

    try:
        total_price = store_obj.order(shopping_list)
        print(f"\n✅ Order successful! Total cost: {total_price} dollars.")
    except Exception as e:
        print(f"❌ Order failed: {e}")


def start(store_obj):
    """
    Main UI loop: menu + dispatch to actions.
    """
    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_products(store_obj)
        elif choice == "2":
            show_total(store_obj)
        elif choice == "3":
            make_order(store_obj)
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