def isHappy(n):
    """
    :type n: int
    :rtype: bool
    """
    while n > 9:
        n = sum(int(i) ** 2 for i in str(n))
    return n == 1 or n == 7


print(isHappy(7))
