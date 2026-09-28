from menu import menu


# ========== CALCULATION FUNCTIONS ==========

def calculate_subtotal(ordered_items):
    """
    Calculate the subtotal from all ordered items
    Returns: subtotal amount
    """
    subtotal = 0
    for item, quantity in ordered_items.items():
        subtotal += menu[item] * quantity
    return subtotal


def apply_discount(subtotal):
    """
    Apply realistic discount based on order subtotal
    Returns: discount percentage and discount amount
    """
    discount_percent = 0

    # Discount logic: encourage larger orders
    if subtotal >= 50:
        discount_percent = 15  # 15% off for orders >= ₱50
    elif subtotal >= 35:
        discount_percent = 10  # 10% off for orders >= ₱35
    elif subtotal >= 20:
        discount_percent = 5  # 5% off for orders >= ₱20

    discount_amount = subtotal * (discount_percent / 100)
    return discount_percent, discount_amount


def calculate_total(subtotal, discount_amount):
    """
    Calculate final total with tax (12% sales tax)
    Returns: final total amount
    """
    tax_rate = 0.12
    taxable_amount = subtotal - discount_amount
    tax = taxable_amount * tax_rate
    total = taxable_amount + tax
    return total