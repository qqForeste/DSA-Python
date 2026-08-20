# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        

        dummy = ListNode()

        curr = dummy
        carry = 0

        while l1 or l2 or carry:
            val1, val2 = l1.val if l1 else 0, l2.val if l2 else 0

            result = val1 + val2 + carry

            digit = result % 10 
            carry = result // 10 # 15 // 10 = 1 15 % 10 = 5

            curr.next = ListNode(digit)
            curr = curr.next

            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        return dummy.next


            