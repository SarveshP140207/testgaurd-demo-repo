from app.calculator import multiply

def calculate_subtotal(price, quantity):
    return multiply(price, quantity)

def calculate_discount(subtotal, discount_percent):
    return subtotal * (discount_percent / 100)

def calculate_final_price(price, quantity, discount_percent=0):
    subtotal = calculate_subtotal(price, quantity)
    discount = calculate_discount(subtotal, discount_percent)
    return subtotal - discount
