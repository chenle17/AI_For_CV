class Solution:
    """
    @param s: a string which consists of lowercase or uppercase letters
    @return: the length of the longest palindromes that can be built
    """
    def longestPalindrome(self, s):
        # write your code here
        
        #version 1.0
        # length = len(s)
        # str_dict = {}
        # for i in range(length):
        #     str_dict[s[i]] = str_dict.get(s[i], 0) + 1
        # out = 0
        # for k,v in str_dict.items():
        #     if not v & 1 or not out & 1:
        #         out += v
        #     elif out & 1:
        #         out += v - 1
        # return out
        
        #version 1.1
        str_dict = {}
        for i in s:
            str_dict[i] = str_dict.get(i, 0) + 1
        out = 0
        for k,v in str_dict.items():
            if not v & 1 or not out & 1:
                out += v
            elif out & 1:
                out += v - 1
        return out
        
        #version 2.0
        # return len(s) - max(0,sum([s.count(e)%2 for e in set(s)]) -1)
