from menu import menu


# ========== DISPLAY FUNCTIONS ==========

def display_menu():
    """
    Display the full menu with prices in a formatted table
    """
    print("\n" + "=" * 50)
    print("      🇵🇭 TIKMAN TAYO - PINOY STREET FOOD 🇵🇭")
    print("=" * 50)
    print("\n" + "-" * 50)
    print("MENU ITEMS")
    print("-" * 50)

    # Use for loop to iterate through menu dictionary
    for index, (item, price) in enumerate(menu.items(), 1):
        print(f"{index:2d}. {item:<30} ₱{price:>6.2f}")

    print("-" * 50 + "\n")


def display_order_summary(ordered_items):
    """
    Display items ordered before showing final receipt
    """
    print("\n" + "=" * 50)
    print("ORDER SUMMARY")
    print("=" * 50)

    for item, quantity in ordered_items.items():
        price_per_item = menu[item]
        total_price = price_per_item * quantity
        print(f"{item:<30} x{quantity:>2} @ ₱{price_per_item:>6.2f} = ₱{total_price:>8.2f}")

    print("=" * 50 + "\n")


def display_receipt(ordered_items, subtotal, discount, discount_amount, total):
    """
    Display a realistic, professional receipt
    """
    print("\n" + "=" * 60)
    print(" " * 15 + "🧾 RECEIPT 🧾")
    print("=" * 60)
    print(" " * 8 + "TIKMAN TAYO - PINOY STREET FOOD HEAVEN")
    print(" " * 12 + "Authentic Filipino Street Food Since Today")
    print(" " * 15 + "Order Date: Monday, September 28, 2026")
    print("=" * 60)
    print("\nITEM DETAILS:")
    print("-" * 60)
    print(f"{'Item':<35} {'Qty':>5} {'Price':>10} {'Total':>9}")
    print("-" * 60)

    # Use for loop to display each ordered item on receipt
    for item, quantity in ordered_items.items():
        price_per_item = menu[item]
        item_total = price_per_item * quantity
        print(f"{item:<35} {quantity:>5} ₱{price_per_item:>9.2f} ₱{item_total:>8.2f}")

    print("-" * 60)
    print(f"{'Subtotal':<50} ₱{subtotal:>9.2f}")

    # Display discount if applicable
    if discount > 0:
        print(f"{'Discount (' + str(discount) + '% OFF)':<50} -₱{discount_amount:>8.2f}")

    print("=" * 60)
    print(f"{'TOTAL AMOUNT DUE':<50} ₱{total:>9.2f}")
    print("=" * 60)
    print("\n    Thank you for your order! Enjoy your meal! 😊\n")
    print("=" * 60 + "\n")