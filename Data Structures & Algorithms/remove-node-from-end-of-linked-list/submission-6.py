# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if head and not head.next:
            return None
        
        prev, curr, length = head, head.next, 1

        while prev.next:
            prev = prev.next
            length += 1

        if length == 2:
            if n == 1:
                head.next = None
                return head
            elif n == 2:
                head = head.next
                return head
        if n == length:
            head = head.next
            return head
        count = length - n
        prev = head

        for i in range(count - 1):
            prev = prev.next
            curr = curr.next

        prev.next = curr.next
        return head
