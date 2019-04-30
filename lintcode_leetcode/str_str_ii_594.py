class Solution:
    """
    @param: source: A source string
    @param: target: A target string
    @return: An integer as index
    """
    '''
    考点：

        hash
        kmp
    题解：
    
        采用字符串哈希，字符串哈希时需要将字符串映射为数字，
        hash_target = (hash_target * 26 + ord(target[i]) - ord('a')) % mod 
        此处哈希函数，提供了字符串转化数字的关系式。
        对于需要匹配的子串对应一个值，然后再遍历主串，当前位置为i，
        则用i的哈希值减去i-m部分的哈希值，求出中间m个长度的子串的哈希值，
        如果与要匹配串相同，由于哈希本身不安全，需要截取出来m长度的子串再进行匹配，
        完全相同即可。
        注意负数取模时，需要通过+mod，将负数变为正数。
        kmp是线性的字符串匹配算法，同样可以实现。
    '''
    def strStr2(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        base_num = 1000000

        len_s = len(source)
        len_t = len(target)

        if len_t == 0:
            return 0

        weight_num = 1
        for _ in range(len_t):
            weight_num = weight_num * 31 % base_num

        target_hash = 0
        for i in range(len_t):
            target_hash = (target_hash * 31 + ord(target[i])) % base_num# ord()：字符转int

        source_hash = 0
        # 便利从source第一个字符到最后一个字符
        for i in range(len_s):

            source_hash = (source_hash * 31 + ord(source[i])) % base_num

            if i < len_t - 1:
                continue
            elif i > len_t - 1:# 第len_t + 1次循环开始去首
                source_hash = (source_hash
                               - ord(source[i - len_t]) * weight_num % base_num
                               + base_num
                               ) % base_num
            if source_hash != target_hash:
                continue
            if source[i - len_t + 1:i + 1] == target:
                return i - len_t + 1
        return -1

    def strStr2_2(self, source, target):
        # write your code here
        if source is None or target is None:
            return -1

        m = len(source)
        n = len(target)
        if n == 0:
            return 0

        base_num = 1234567

        weight_num = 1
        for _ in range(n):
            weight_num = weight_num * 31 % base_num

        target_hash = 0
        for i in range(n):
            target_hash = (target_hash * 31 + ord(target[i])) % base_num

        source_hash = 0
        for i in range(m):
            source_hash = (source_hash * 31 + ord(source[i])) % base_num

            if i > n - 1:
                source_hash = (source_hash
                               - ord(source[i - n]) * weight_num % base_num
                               + base_num) % base_num

            if target_hash == source_hash and source[i - n + 1:i + 1] == target:
                return i - n + 1

        return -1



