def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """

        count = 0
        letter_counts = {}

        for char in s:
            if char in letter_counts:
                letter_counts[char] += 1
            else:
                letter_counts[char] = 1

        for char in letter_counts:
            if letter_counts[char] % 2 == 0:
                count += letter_counts[char]
            else:
                count += letter_counts[char] - 1

        if count == len(s):
            return count
        else:
            return count + 1
