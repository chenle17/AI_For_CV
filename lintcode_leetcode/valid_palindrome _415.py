import re


class Solution:
    """
    @param s: A string
    @return: Whether the string is a valid palindrome
    """

    def isPalindrome(self, s):
        # write your code here

        # version 1.0
        # if s is None:
        #     return False

        # #multiple regular matching methods
        # # s = ''.join(re.findall(r'[A-Za-z0-9]', s)).lower() # 1
        # # s = re.sub(r'[^A-Za-z0-9]', '', s).lower() # 2
        # s = ''.join(re.split(r'[^A-Za-z0-9]', s)).lower() # 3

        # if s == s[::-1]:
        #     return True
        # return False

        # version 1.1
        # if s is None:
        #     return False
        #
        # # multiple regular matching methods
        # # s = ''.join(re.findall(r'[A-Za-z0-9]', s)).lower() # 1
        # # s = re.sub(r'[^A-Za-z0-9]', '', s).lower() # 2
        # s = ''.join(re.split(r'[^A-Za-z0-9]', s)).lower()  # 3
        # # s = ''.join(filter(str.isalnum,s)).lower() # 4
        #
        # return s == s[::-1]

        # # version 2.0
        if s == None:
            return False

        end = len(s) - 1
        start = 0

        while start <= end:
            while start < end and not s[start].isalpha() and not s[start].isdigit():
                start += 1
            while end > start and not s[end].isalpha() and not s[end].isdigit():
                end -= 1
            if s[start].lower() != s[end].lower():
                return False
            start += 1
            end -= 1
        return True


