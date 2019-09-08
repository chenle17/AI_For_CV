class Solution:
    """
    @param digits: A digital string
    @return: all posible letter combinations
    """
    '''
    电话号码的字母组合
中文English
给一个不包含'0'和'1'的数字字符串，每个数字代表一个字母，请返回其所有可能的字母组合。

下图的手机按键图，就表示了每个数字可以代表的字母。

1	2
ABC	3
DEF
4
GHI	5
JKL	6
MNO
7
PQRS	8
TUV	9
WXYZ
Example
样例 1:

输入: "23"
输出: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
解释: 
'2' 可以是 'a', 'b' 或 'c'
'3' 可以是 'd', 'e' 或 'f'
样例 2:

输入: "5"
输出: ["j", "k", "l"]
Notice
以上的答案是按照词典编撰顺序进行输出的，不过，在做本题时，你也可以任意选择你喜欢的输出顺序。
    
    '''
    def letterCombinations(self, digits):
        # write your code here

        if not digits:
            return []

        keyboard_dict = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno',
                         '7': 'pqrs', '8': 'tuv', '9': 'wxyz'
                         }

        all_str = []
        self.find_str(digits, keyboard_dict, all_str, '')

        return all_str

    def find_str(self, digits, keyboard_dict, all_str, sub_str):
        if not digits:
            all_str.append(sub_str)
            return

        for s in keyboard_dict[digits[0]]:
            sub_str += s
            self.find_str(digits[1:], keyboard_dict, all_str, sub_str)
            sub_str = sub_str[:-1]

