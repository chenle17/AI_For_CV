'''
For a given source string and a target string, you should output the first index(from 0) of target string in source string.

If target does not exist in source, just return -1.

Example
Example 1:
	Input: source = "source" ，target = "target"
	Output: -1

	Explanation:
	If the source does not contain the target content, return - 1.

Example 2:
	Input:source = "abcdabcdefg" ，target = "bcd"
	Output: 1

	Explanation:
	If the source contains the target content, return the location where the target first appeared in the source.

Challenge
O(n2) is acceptable. Can you implement an O(n) algorithm? (hint: KMP)

Clarification
Do I need to implement KMP Algorithm in a real interview?

Not necessary. When you meet this problem in a real interview, the interviewer may just want to test your basic implementation ability. But make sure you confirm with the interviewer first.
'''

class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        if source == None or target == None:
            return -1

        if not target:
            return 0

        len_s = len(source)
        len_t = len(target)
        if len_s < len_t:
            return -1

        for i in range(len_s - len_t + 1):
            flag = True
            for j in range(len_t):
                if source[i + j] != target[j]:
                    flag = False
                    break

            if flag:
                return i
        return -1

    def strStr_(self, source, target):
        # source可以为空“”，不判断source为“”的情况
        if source is None or target is None:
            return -1
        len_s = len(source)
        len_t = len(target)
        # source不需要全部便利，+1是为了字符串长度相等情况
        for i in range(len_s - len_t + 1):
            j = 0
            # 包含len_t为0时的情况
            while (j < len_t):
                # 字符串元素不等时跳出
                if source[i + j] != target[j]:
                    break
                j += 1
            if j == len_t:
                return i
        return -1