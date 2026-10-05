from app.pricing import calculate_subtotal, calculate_discount, calculate_final_price

def test_calculate_subtotal():
    assert calculate_subtotal(100, 3) == 300

def test_calculate_discount():
    assert calculate_discount(500, 10) == 50

def test_calculate_final_price():
    assert calculate_final_price(100, 2, 10) == 180

def test_discount_rejects_negative_percentage():

    import pytest
    with pytest.raises(ValueError):
        calculate_discount(500, -10)

def test_discount_rejects_percentage_above_100():

    import pytest
    with pytest.raises(ValueError):
        calculate_discount(500, 120)
