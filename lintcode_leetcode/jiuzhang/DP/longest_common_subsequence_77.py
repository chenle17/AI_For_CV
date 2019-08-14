'''
Given two strings, find the longest common subsequence (LCS).

Your code should return the length of LCS.

Example
Example 1:
	Input:  "ABCD" and "EDCA"
	Output:  1

	Explanation:
	LCS is 'A' or  'D' or 'C'


Example 2:
	Input: "ABCD" and "EACB"
	Output:  2

	Explanation:
	LCS is "AC"
Clarification
What's the definition of Longest Common Subsequence?

https://en.wikipedia.org/wiki/Longest_common_subsequence_problem
http://baike.baidu.com/view/2020307.htm


'''
class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """

    def longestCommonSubsequence(self, A, B):
        # write your code here
        if not A or not B:
            return 0

        m, n = len(A), len(B)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
                if A[i - 1] == B[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                    # dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + 1)

        return dp[m][n]