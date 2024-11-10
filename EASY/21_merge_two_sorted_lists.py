"""
    you are given the heads of two sorted linked lists list1 and list2.
    Merge the two lists into one sorted list. The list should be made by splicing together the nodes of the first two lists.
    Return the head of the merged linked list.

    Example 1:
        Input: list1 = [1,2,4], list2 = [1,3,4]
        Output: [1,1,2,3,4,4]
    Example 2:
        Input: list1 = [], list2 = []
        Output: []
    Example 3:
        Input: list1 = [], list2 = [0]
        Output: [0]
    Constraints:
        The number of nodes in both lists is in the range [0, 50].
        -100 <= Node.val <= 100
        Both list1 and list2 are sorted in non-decreasing order.
"""

# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 
        

def call_mergeTwoLists(list1, list2):
    l1_start = l1_node = ListNode()
    l2_start = l2_node = ListNode()
    
    for i in list1:
        current = ListNode(i)
        l1_node.next = current
        l1_node = l1_node.next
        
    for i in list2:
        current = ListNode(i)
        l2_node.next = current
        l2_node = l2_node.next 
        
    Solution().mergeTwoLists(l1_start.next, l2_start.next)
    
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        start = node = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                node.next = ListNode(list2.val)
                node = node.next
                list2 = list2.next
            else:
                node.next = ListNode(list1.val)
                node = node.next
                list1 = list1.next
        if list1:
            node.next = list1
        if list2:
            node.next = list2
        return start.next
        # while start:
        #     print(start.val)
        #     start = start.next
        
    
call_mergeTwoLists(list1 = [1,2,4], list2 = [1,3,4])