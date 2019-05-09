class Solution:
    """
    @param s: a string
    @return bool: whether you can make s a palindrome by deleting at most one character
    """

    '''
    Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
    
    Example
    Example 1:
    
    Input: s = "aba"
    Output: true
    Explanation: Originally a palindrome.
    Example 2:
    
    Input: s = "abca"
    Output: true
    Explanation: Delete 'b' or 'c'.
    Example 3:
    
    Input: s = "abc"
    Output: false
    Explanation: Deleting any letter can not make it a palindrome.
    Notice
    The string will only contain lowercase characters.
    The maximum length of the string is 50000.
    '''

    def validPalindrome(self, s):
        # Write your code here
        if s is None:
            return False

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                # 终止进入删除一个元素操作
                break
            left += 1
            right -= 1

        if left >= right:
            return True

        # 删左边或者右边一个
        return self.is_palindrome(s[left + 1:right + 1]) or self.is_palindrome(s[left:right])

    def is_palindrome(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True