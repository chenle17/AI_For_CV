class Solution:
    """
    @param source:
    @param target:
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here

        # version 1.0
        # if source == None or target == None:
        #     return -1

        # l_s = len(source)
        # l_t = len(target)

        # if l_s < l_t:
        #     return -1

        # for i in range(l_s - l_t + 1):
        #     if source[i:i+l_t] == target:
        #         return i

        # return -1

        # version 1.1
        if source == None or target == None:
            return -1

        l_s = len(source)
        l_t = len(target)

        if l_s < l_t:
            return -1

        for i in range(l_s - l_t + 1):
            j = 0
            while j < l_t:
                if source[i + j] != target[j]:
                    break
                j += 1

            if j == l_t:
                return i

        return -1