'''
Find the middle node of a linked list.

Example
Example 1:

Input:  1->2->3
Output: 2
Explanation: return the value of the middle node.
Example 2:

Input:  1->2
Output: 1
Explanation: If the length of list is  even return the value of center left one.
Challenge
If the linked list is in a data stream, can you find the middle without iterating the linked list again?

'''
"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""


class Solution:
    """
    @param head: the head of linked list.
    @return: a middle node of the linked list
    """

    def middleNode(self, head):
        # write your code here

        if head is None:
            return

        # 双指针，一块一慢，遍历一次得到中点
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow
'''
一个小练习
将上述代码改为提供接口的模式，即设计一个 class，支持两个函数，一个是 add(node) 加入一个节点，一个是 getMiddle() 求中间的那个节点。
'''
class linked_list:
    def __init__(self, head=None):
        self.head = head
        self.size = 0
        self.end = None
        if head:
            self.size += 1
            while head.next:
                self.size += 1
                head = head.next
            self.end = head


    def add(self, node):
        if self.end:
            self.end.next = node
            self.size += 1
            while node.next:
                self.size += 1
                node = node.next
            self.end = node
        else:
            self.head = node
            self.size += 1
            while node.next:
                self.size += 1
                node = node.next
            self.end = node

    def get_middle(self):
        if not self.end:
            return
        node = self.head
        for _ in range(self.size - 1 // 2):
            node = node.next
        return node
