# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result_head = ListNode(0)
        result_current = result_head

        flag = False

        while l1 or l2 or flag:
            if result_current is None:
                result_current = ListNode(0)
            if l1 is not None:
                result_current.val += l1.val
                l1 = l1.next
            if l2 is not None:
                result_current.val += l2.val
                l2 = l2.next
            if flag:
                result_current.val += 1
                flag = False
            if result_current.val >= 10:
                result_current.val = result_current.val % 10
                flag = True
            result_current = result_current.next
