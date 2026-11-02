# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
 # this is esentually deleting a node problem 
        # # for deleting the node we have to find the n-1 node so that we can chnage the next pointer to next to next 
        # 1->2->3->4 n= 2 
        # 1->2->4 here 2 points to 4 instead of 3 so we need to change 2's next to next.next esentially jumping the node 
        # so the core problem is in finding the n+1 node from end 
        # # we can use fast and slow pointers 
        # 1->2->3->4 
        #       s
        #             f 
        # # we can use fast and slow pointers to find the node 
        # # the gap between the fast and slow increases as we go and once the fast reaches the end we proceed the slow one until teh gap between fast and slow is n 
        # this way we find the node 
        # once we find teh node we can change the pointers 

"""
part 1: finding the nth node from end
part2: changing the pointers of the prev node of the found node 
part3: how do we find the difference 


"""
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        left = dummy 
        right = head 
        while n > 0 and right:
            right = right.next 
            n-=1 
        while right:
            left = left.next 
            right = right.next 
        #delete 
        left.next = left.next.next
        return dummy.next 
       