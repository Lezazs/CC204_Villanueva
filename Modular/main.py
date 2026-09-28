"""
MODULAR VERSION - FAST FOOD RESTAURANT ORDERING SYSTEM
A comprehensive ordering system for fast food restaurants with professional receipts
Organized into separate modules for better maintainability
"""

from display import display_menu, display_order_summary, display_receipt
from calculations import calculate_subtotal, apply_discount, calculate_total
from validation import get_menu_item, get_quantity, get_yes_no_response


# ========== MAIN ORDERING FUNCTION ==========

def main():
    """
    Main function that controls the entire ordering process
    """
    ordered_items = {}

    # Display menu
    display_menu()

    # Ask if user wants to order
    if not get_yes_no_response("Would you like to order? (yes/no): "):
        print("\n👋 Thank you for visiting! Come again soon!\n")
        return

    # Ordering loop - get items until user is done
    while True:
        print("\n" + "-" * 50)
        item = get_menu_item()
        quantity = get_quantity()

        # Add or update item in ordered_items dictionary
        if item in ordered_items:
            ordered_items[item] += quantity
            print(f"✓ Updated: {item} (Total qty: {ordered_items[item]})")
        else:
            ordered_items[item] = quantity
            print(f"✓ Added: {item} to cart")

        # Ask if user wants to order more items
        if not get_yes_no_response("\nOrder another item? (yes/no): "):
            break

    # Calculate prices
    subtotal = calculate_subtotal(ordered_items)
    discount_percent, discount_amount = apply_discount(subtotal)
    total = calculate_total(subtotal, discount_amount)

    # Display order summary and receipt
    display_order_summary(ordered_items)
    display_receipt(ordered_items, subtotal, discount_percent, discount_amount, total)

    # Exit message
    print("👋 Thank you for your order! Please come again!\n")


# ========== PROGRAM ENTRY POINT ==========

if __name__ == "__main__":
    main()