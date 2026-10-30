# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev, cur = None, head 
        while cur:
            tmp = cur.next #storing the current.next node
            cur.next = prev  # changing the nodes 
            ## updating for the next pass 

            prev = cur # update  rev none to the currnet node because cur.next = prev 
            cur = tmp
        return prev