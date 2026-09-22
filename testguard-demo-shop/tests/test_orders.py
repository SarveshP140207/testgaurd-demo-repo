from app.orders import create_order

def test_create_order():
    order = create_order(100, 2)
    assert order["status"] == "confirmed"

def test_create_discounted_order():
    order = create_order(100, 2, 10)
    assert order["status"] == "confirmed"

def test_failed_order():
    order = create_order(0, 1)
    assert order["status"] == "failed"
