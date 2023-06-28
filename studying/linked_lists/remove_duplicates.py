# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start = node = head
 
        #ensures that we always have two nodes left for comparison
        while node and node.next: 
            #two-pointer technique to compare val of current and next node
            if node.val == node.next.val:
                new_next = node.next.next
                node.next = new_next
            else:
                node = node.next
    
        return start