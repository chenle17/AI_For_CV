'''
Write a program to find the node at which the intersection of two singly linked lists begins.

Example
Example 1:

Input:
	A:          a1 → a2
	                   ↘
	                     c1 → c2 → c3
	                   ↗
	B:     b1 → b2 → b3
Output: c1
Explanation ：begin to intersect at node c1.
Example 2:

Input:
Intersected at 6
1->2->3->4->5->6->7->8->9->10->11->12->13->null
6->7->8->9->10->11->12->13->null
Output: Intersected at 6
Explanation：begin to intersect at node 6.
Challenge
Your code should preferably run in O(n) time and use only O(1) memory.

Notice
If the two linked lists have no intersection at all, return null.
The linked lists must retain their original structure after the function returns.
You may assume there are no cycles anywhere in the entire linked structure.
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
    @param headA: the first list
    @param headB: the second list
    @return: a ListNode
    """

    def getIntersectionNode(self, headA, headB):
        # write your code here
        if headA is None or headB is None:
            return None

        node_A = headA
        len_A = 1
        while node_A.next:
            len_A += 1
            node_A = node_A.next

        node_B = headB
        len_B = 1
        while node_B.next:
            len_B += 1
            node_B = node_B.next

        if node_A != node_B:
            return None

        while len_A > len_B:
            headA = headA.next
            len_A -= 1
        while len_A < len_B:
            headB = headB.next
            len_B -= 1
        while len_A > 0:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None

        # slow, fast = headA, headA.next
        # while fast and fast.next:
        #     slow = headA.next
        #     fast = headA.next.next
        #     if slow == fast:
        #         return slow.val

        # return None