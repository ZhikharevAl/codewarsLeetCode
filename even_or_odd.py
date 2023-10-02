def even_or_odd(number):
    # return "Even" if number % 2 == 0 else "Odd"
    return ["Even", "Odd"][number % 2]


def test_even_or_odd():
    assert even_or_odd(2) == "Even"
    assert even_or_odd(3) == "Odd"
