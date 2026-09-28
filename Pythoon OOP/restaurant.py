"""
Python OOP Version - Restaurant Class
Encapsulates all ordering system functionality into a Restaurant class
"""

class Restaurant:
    """
    A class to represent a fast food restaurant ordering system

    Attributes:
        menu (dict): Dictionary of menu items and prices
        name (str): Name of the restaurant
        address (str): Address of the restaurant
    """

    def __init__(self, name="TIKMAN TAYO - PINOY STREET FOOD HEAVEN"):
        """
        Initialize the Restaurant with menu and name

        Args:
            name (str): Name of the restaurant
        """
        self.name = name
        self.menu = {
            "Balut (Pcs)": 15.00,
            "Penoy (Pcs)": 12.00,
            "Isaw - Grilled Intestines (Stick)": 18.00,
            "Kwek-Kwek - Quail Eggs (Pcs)": 8.00,
            "Fishball (10 pcs)": 25.00,
            "Taho - Sweet Beancurd (Glass)": 10.00,
            "Tokwa't Baboy (Serving)": 30.00,
            "Pork BBQ Skewer (Stick)": 20.00,
            "Lumpia - Spring Roll (Pcs)": 12.00,
            "Betamax - Coagulated Blood (Stick)": 18.00
        }

    def display_menu(self):
        """Display the full menu with prices in a formatted table"""
        print("\n" + "="*50)
        print("      🇵🇭 TIKMAN TAYO - PINOY STREET FOOD 🇵🇭")
        print("="*50)
        print("\n" + "-"*50)
        print("MENU ITEMS")
        print("-"*50)

        for index, (item, price) in enumerate(self.menu.items(), 1):
            print(f"{index:2d}. {item:<30} ₱{price:>6.2f}")

        print("-"*50 + "\n")

    def get_menu_item(self):
        """
        Get valid menu item from user with error handling

        Returns:
            str: Valid menu item name
        """
        while True:
            try:
                print("Available items:")
                for index, item in enumerate(self.menu.keys(), 1):
                    print(f"  {index}. {item}")

                choice = input("\nEnter item name or number (1-10): ").strip()

                # Check if input is a number
                if choice.isdigit():
                    choice_num = int(choice)
                    if 1 <= choice_num <= len(self.menu):
                        item_name = list(self.menu.keys())[choice_num - 1]
                        print(f"✓ Selected: {item_name}")
                        return item_name
                    else:
                        print("❌ Invalid number. Please enter a number between 1 and 10.\n")

                # Check if input is an item name
                elif choice in self.menu:
                    print(f"✓ Selected: {choice}")
                    return choice

                else:
                    print("❌ Item not found in menu. Please try again.\n")

            except Exception as e:
                print(f"❌ Error: {e}. Please try again.\n")

    def get_quantity(self):
        """
        Get valid quantity from user with error handling

        Returns:
            int: Valid quantity (positive integer)
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

    def get_yes_no_response(self, prompt):
        """
        Get yes/no response from user with error handling

        Args:
            prompt (str): Question to ask the user

        Returns:
            bool: True for yes, False for no
        """
        while True:
            response = input(prompt).strip().lower()

            if response in ['yes', 'y']:
                return True
            elif response in ['no', 'n']:
                return False
            else:
                print("❌ Invalid response. Please enter 'yes' or 'no'.\n")

    def calculate_subtotal(self, ordered_items):
        """
        Calculate the subtotal from all ordered items

        Args:
            ordered_items (dict): Dictionary of ordered items and quantities

        Returns:
            float: Subtotal amount
        """
        subtotal = 0
        for item, quantity in ordered_items.items():
            subtotal += self.menu[item] * quantity
        return subtotal

    def apply_discount(self, subtotal):
        """
        Apply realistic discount based on order subtotal

        Args:
            subtotal (float): The subtotal amount

        Returns:
            tuple: (discount_percent, discount_amount)
        """
        discount_percent = 0

        # Discount logic: encourage larger orders
        if subtotal >= 50:
            discount_percent = 15  # 15% off for orders >= ₱50
        elif subtotal >= 35:
            discount_percent = 10  # 10% off for orders >= ₱35
        elif subtotal >= 20:
            discount_percent = 5   # 5% off for orders >= ₱20

        discount_amount = subtotal * (discount_percent / 100)
        return discount_percent, discount_amount

    def calculate_total(self, subtotal, discount_amount):
        """
        Calculate final total with tax (12% sales tax)

        Args:
            subtotal (float): The subtotal amount
            discount_amount (float): The discount amount

        Returns:
            float: Final total amount
        """
        tax_rate = 0.12
        taxable_amount = subtotal - discount_amount
        tax = taxable_amount * tax_rate
        total = taxable_amount + tax
        return total

    def display_order_summary(self, ordered_items):
        """
        Display items ordered before showing final receipt

        Args:
            ordered_items (dict): Dictionary of ordered items and quantities
        """
        print("\n" + "="*50)
        print("ORDER SUMMARY")
        print("="*50)

        for item, quantity in ordered_items.items():
            price_per_item = self.menu[item]
            total_price = price_per_item * quantity
            print(f"{item:<30} x{quantity:>2} @ ₱{price_per_item:>6.2f} = ₱{total_price:>8.2f}")

        print("="*50 + "\n")

    def display_receipt(self, ordered_items, subtotal, discount, discount_amount, total):
        """
        Display a realistic, professional receipt

        Args:
            ordered_items (dict): Dictionary of ordered items and quantities
            subtotal (float): The subtotal amount
            discount (int): Discount percentage
            discount_amount (float): The discount amount
            total (float): Final total amount
        """
        print("\n" + "="*60)
        print(" "*15 + "🧾 RECEIPT 🧾")
        print("="*60)
        print(" "*8 + "TIKMAN TAYO - PINOY STREET FOOD HEAVEN")
        print(" "*12 + "Authentic Filipino Street Food Since Today")
        print(" "*15 + "Order Date: Monday, September 28, 2026")
        print("="*60)
        print("\nITEM DETAILS:")
        print("-"*60)
        print(f"{'Item':<35} {'Qty':>5} {'Price':>10} {'Total':>9}")
        print("-"*60)

        for item, quantity in ordered_items.items():
            price_per_item = self.menu[item]
            item_total = price_per_item * quantity
            print(f"{item:<35} {quantity:>5} ₱{price_per_item:>9.2f} ₱{item_total:>8.2f}")

        print("-"*60)
        print(f"{'Subtotal':<50} ₱{subtotal:>9.2f}")

        # Display discount if applicable
        if discount > 0:
            print(f"{'Discount (' + str(discount) + '% OFF)':<50} -₱{discount_amount:>8.2f}")

        print("="*60)
        print(f"{'TOTAL AMOUNT DUE':<50} ₱{total:>9.2f}")
        print("="*60)
        print("\n    Thank you for your order! Enjoy your meal! 😊\n")
        print("="*60 + "\n")

    def run_order(self):
        """
        Main method to run the complete ordering process
        """
        ordered_items = {}

        # Display menu
        self.display_menu()

        # Ask if user wants to order
        if not self.get_yes_no_response("Would you like to order? (yes/no): "):
            print("\n👋 Thank you for visiting! Come again soon!\n")
            return

        # Ordering loop - get items until user is done
        while True:
            print("\n" + "-"*50)
            item = self.get_menu_item()
            quantity = self.get_quantity()

            # Add or update item in ordered_items dictionary
            if item in ordered_items:
                ordered_items[item] += quantity
                print(f"✓ Updated: {item} (Total qty: {ordered_items[item]})")
            else:
                ordered_items[item] = quantity
                print(f"✓ Added: {item} to cart")

            # Ask if user wants to order more items
            if not self.get_yes_no_response("\nOrder another item? (yes/no): "):
                break

        # Calculate prices
        subtotal = self.calculate_subtotal(ordered_items)
        discount_percent, discount_amount = self.apply_discount(subtotal)
        total = self.calculate_total(subtotal, discount_amount)

        # Display order summary and receipt
        self.display_order_summary(ordered_items)
        self.display_receipt(ordered_items, subtotal, discount_percent, discount_amount, total)

        # Exit message
        print("👋 Thank you for your order! Please come again!\n")