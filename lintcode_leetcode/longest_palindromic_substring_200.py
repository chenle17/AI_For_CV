class Solution:
    """
    @param s: input string
    @return: the longest palindromic substring
    """

    def longestPalindrome(self, s):
        # write your code here

        if s == None:
            return ""

        longest = ""
        l = len(s)
        for i in range(l):
            ss = self.find_longest_palindrome(s, i, i)
            if len(longest) < len(ss):
                longest = ss
            ss = self.find_longest_palindrome(s, i, i + 1)
            if len(longest) < len(ss):
                longest = ss

        return longest

    def find_longest_palindrome(self, s, start, end):
        while start >= 0 and end < len(s):
            if s[start] == s[end]:
                start -= 1
                end += 1
            else:
                break
        return s[start + 1: end]