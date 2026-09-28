from menu import menu


# ========== INPUT VALIDATION FUNCTIONS ==========

def get_menu_item():
    """
    Get valid menu item from user with error handling
    Returns: valid menu item name
    """
    while True:
        try:
            print("Available items:")
            for index, item in enumerate(menu.keys(), 1):
                print(f"  {index}. {item}")

            choice = input("\nEnter item name or number (1-10): ").strip()

            # Check if input is a number
            if choice.isdigit():
                choice_num = int(choice)
                if 1 <= choice_num <= len(menu):
                    item_name = list(menu.keys())[choice_num - 1]
                    print(f"✓ Selected: {item_name}")
                    return item_name
                else:
                    print("❌ Invalid number. Please enter a number between 1 and 10.\n")

            # Check if input is an item name
            elif choice in menu:
                print(f"✓ Selected: {choice}")
                return choice

            else:
                print("❌ Item not found in menu. Please try again.\n")

        except Exception as e:
            print(f"❌ Error: {e}. Please try again.\n")


def get_quantity():
    """
    Get valid quantity from user with error handling
    Returns: valid quantity (positive integer)
    """
    while True:
        try:
            quantity = input("Enter quantity: ").strip()

            if not quantity:
                print("❌ Quantity cannot be empty. Please enter a number.\n")
                continue

            quantity_int = int(quantity)

            if quantity_int > 0:
                print(f"✓ Quantity: {quantity_int}\n")
                return quantity_int
            else:
                print("❌ Quantity must be greater than 0. Please try again.\n")

        except ValueError:
            print("❌ Invalid input. Please enter a valid number.\n")


def get_yes_no_response(prompt):
    """
    Get yes/no response from user with error handling
    Returns: True for yes, False for no
    """
    while True:
        response = input(prompt).strip().lower()

        if response in ['yes', 'y']:
            return True
        elif response in ['no', 'n']:
            return False
        else:
            print("❌ Invalid response. Please enter 'yes' or 'no'.\n")