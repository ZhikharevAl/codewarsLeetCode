def income(prices):
    odd_prices = sum(prices[1::2])
    even_prices = sum(prices[::2])
    return odd_prices - even_prices


result = income(prices)
