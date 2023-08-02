'''
Convert number to reversed array of digits
Given a random non-negative number, you have to return the digits of this number within an array in reverse order.
'''


def digitize(n):
    return [int(i) for i in str(n)[::-1]]

print(digitize(35231))