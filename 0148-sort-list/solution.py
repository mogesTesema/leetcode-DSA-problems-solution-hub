# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def sort_ListInner(head):  

            if head == None or head.next == None:
                return head
            right = get_mid(head)
            left = head
            temp = right.next
            right.next = None
            right = temp
            left = sort_ListInner(left)
            right = sort_ListInner(right)
            return sort_linked_list(left,right)

        def get_mid(node):
            slow = node
            fast = node.next
            while fast and fast.next:
                slow = slow.next 
                fast = fast.next.next
            return slow

        def sort_linked_list(left,right):
            temp = rootNode = ListNode(0)
            while left and right:
                if left.val < right.val:
                    temp.next = left
                    left = left.next
                else:
                    temp.next = right
                    right = right.next
                temp = temp.next
            if left:
                temp.next = left
            if right: 
                temp.next = right
            return rootNode.next
        
        return sort_ListInner(head)
