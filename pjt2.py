pjt2.py
menu = {
    "1": {"name": "Cortadito", "price": 250},
    "2": {"name": "Greek Frappé", "price": 300},
    "3": {"name": "Latte", "price": 350},
    "4": {"name": "Cappuccino", "price": 350},
    "5": {"name": "Frappé", "price": 400}
}


def print_menu():
    print("\n*** COFFEE SHOP MENU ***")
    for key, item in menu.items():
        print(f"{key}. {item['name']} - ₹{item['price']:.2f}")
    print("6. View Cart")
    print("0. Checkout & Exit")
    print("********************")


def main():
    cart = []
    total = 0.0

    print("Welcome to Southside Coffee")

    while True:
        print_menu()
        choice = input("Enter your choice: ").strip()

        if choice == "0":
            break

        elif choice == "6":
            if not cart:
                print("\nYour cart is empty.")
            else:
                print("\n--- Your Cart ---")
                for order_item in cart:
                    print(f"{order_item['name']} x{order_item['qty']} - ₹{order_item['subtotal']:.2f}")
                print(f" Your Total : ₹{total:.2f}")

        elif choice in menu:
            selected = menu[choice]

            while True:
                qty_input = input(f"How many {selected['name']}(s)? ")
                if qty_input.isdigit() and int(qty_input) > 0:
                    qty = int(qty_input)
                    break
                print("Please enter a valid positive number.")

            subtotal = selected["price"] * qty
            total += subtotal
            cart.append({
                "name": selected["name"],
                "qty": qty,
                "subtotal": subtotal
            })

            print(f"Added {qty} x {selected['name']} to your cart. (₹{subtotal:.2f})")

        else:
            print("Invalid choice, please try again.")

    print("\n*** RECEIPT ***")
    if not cart:
        print("No items ordered. Goodbye")
    else:
        for order_item in cart:
            print(f"{order_item['name']} x{order_item['qty']} - ₹{order_item['subtotal']:.2f}")
        print("--------------------")
        print(f"TOTAL: ₹{total:.2f}")
        print("Thank you for visiting Southside Coffee. ")


if __name__ == "__main__":
    main()