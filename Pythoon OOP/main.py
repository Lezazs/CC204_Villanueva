"""
PYTHON OOP VERSION - FAST FOOD RESTAURANT ORDERING SYSTEM
A comprehensive ordering system for fast food restaurants with professional receipts
Implemented using Object-Oriented Programming principles
"""

from restaurant import Restaurant


# ========== MAIN ENTRY POINT ==========

if __name__ == "__main__":
    # Create an instance of the Restaurant class
    tikman_tayo = Restaurant()

    # Run the ordering system
    tikman_tayo.run_order()