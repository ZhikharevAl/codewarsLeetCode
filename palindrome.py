def isPalindrome(x: int) -> bool:
    return str(x) == str(x)[::-1]


result = isPalindrome(122)
