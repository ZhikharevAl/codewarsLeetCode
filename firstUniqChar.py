def firstUniqChar(s) -> int:
    """
    :type s: str
    :rtype: int
    """
    for i in s:
        if s.count(i) == 1:
            return s.index(i)
    return -1


print(firstUniqChar("loveleetcode"))
