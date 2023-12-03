def cyclic_left_shift(data, shift):
    return [lst[shift % len(lst):] + lst[:shift % len(lst)] if lst else [] for lst in data]


@pytest.mark.parametrize("data, shift, expected", [
    ([[1, 2, 3], [1, 2, 3]], 1, [[2, 3, 1], [2, 3, 1]]),
    ([[], []], 1, [[], []]),
    ([[1, 2, 3], [1, 2, 3]], 0, [[1, 2, 3], [1, 2, 3]]),
    ([[1, 2, 3], [1, 2, 3]], -1, [[3, 1, 2], [3, 1, 2]]),
    ([[1, 2, 3], [1, 2, 3]], 3, [[1, 2, 3], [1, 2, 3]]),
    ([[1, 2, 3], [4, 5, 6]], -3, [[1, 2, 3], [4, 5, 6]]),
    ([[1, 2, 3], [4, 5, 6]], -4, [[3, 1, 2], [6, 4, 5]])
])
def test_cyclic_left_shift(data, shift, expected):
    assert cyclic_left_shift(data, shift) == expected
