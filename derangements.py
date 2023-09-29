import math

def derangements(n):
    if n == 0:
        return 1
    if n == 1:
        return 0
    return (n - 1) * (derangements(n - 1) + derangements(n - 2))

result = derangements(n)
