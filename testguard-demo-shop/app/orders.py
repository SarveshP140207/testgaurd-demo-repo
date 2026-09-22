from app.payment import process_payment

def create_order(price, quantity, discount_percent=0):
    if process_payment(price, quantity, discount_percent):
        return {"status": "confirmed", "quantity": quantity}
    return {"status": "failed", "quantity": quantity}
