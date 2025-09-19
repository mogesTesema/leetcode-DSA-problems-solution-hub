class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Step 1: Find the total length
        length = 0
        cur = head
        while cur:
            length += 1
            cur = cur.next
        
        # Step 2: If we need to remove the head
        if n == length:
            return head.next
        
        # Step 3: Traverse again to find the (length - n - 1)-th node
        cur = head
        for _ in range(length - n - 1):
            cur = cur.next
        
        # Step 4: Remove nth node from end
        if cur.next:
            cur.next = cur.next.next
        
        return head

