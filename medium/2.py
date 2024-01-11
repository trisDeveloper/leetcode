# 2. Add Two Numbers
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = tail = None
        n = 0
        while l1 or l2 or n:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            sum_val = (val1 + val2 + n) % 10
            n = (val1 + val2 + n) // 10
            new_node = ListNode(sum_val)
            if not head:
                head = tail = new_node
            else:
                tail.next = new_node
                tail = new_node
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return head
