from app.pricing import calculate_final_price

def calculate_payment_amount(price, quantity, discount_percent=0):
    return calculate_final_price(price, quantity, discount_percent)

def process_payment(price, quantity, discount_percent=0):
    amount = calculate_payment_amount(price, quantity, discount_percent)
    if amount <= 0:
        return False
    return True
