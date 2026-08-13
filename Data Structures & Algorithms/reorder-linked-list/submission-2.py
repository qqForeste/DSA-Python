# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        slow = head
        fast = head.next

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        head2 = slow.next
        slow.next = None

        prev = None
        curr = head2
        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
        
        head2 = prev

        curr = None

        while head and head2:
            t1, t2 = head.next, head2.next
            head.next = head2
            head2.next = t1
            head = t1
            head2 = t2
           
        
        


