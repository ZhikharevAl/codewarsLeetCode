# Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.


def reverseWords(self, s: str) -> str:
        new_reverse_world = ""
        for i in range(len(s.split(' '))):
            if i != (len(s.split(' ')) - 1):
                new_reverse_world += s.split(' ')[i][::-1] + " "
            else:
                new_reverse_world += s.split(' ')[i][::-1]
        return new_reverse_world
