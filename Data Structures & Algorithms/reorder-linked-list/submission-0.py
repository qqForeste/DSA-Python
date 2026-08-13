# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        middle = slow.next
        slow.next = None
        prev = None

        while middle:
            temp = middle.next
            middle.next = prev
            prev = middle
            middle = temp
        
        h1, h2 = head, prev

        while h2:
            t1, t2 = h1.next, h2.next
            h1.next = h2
            h2.next = t1
            h1, h2 = t1, t2

        