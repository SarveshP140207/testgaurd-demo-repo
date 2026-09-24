from app.payment import calculate_payment_amount, process_payment

def test_payment_amount():
    assert calculate_payment_amount(100, 2, 10) == 180

def test_payment_success():
    assert process_payment(100, 2) is True

def test_payment_invalid_amount():
    assert process_payment(0, 1) is False
