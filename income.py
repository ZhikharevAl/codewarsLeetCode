def income(prices):
    odd_prices = sum(prices[1::2])
    even_prices = sum(prices[::2])
    return odd_prices - even_prices


result = income(prices)


def test_income():
    assert income([800, 1000, 1100, 1300]) == 400, "Should be 400"
