# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # given: two sorted linked lists 
        # to do: merge them in a sorted way 
        # so one way we can do is convet both of themin a array and sort them and conver them back to LL O(nlogn) bruteforce way 
        # here we are not using the fact that the lists are srted to our advantage and we are just brute forcing it 
        # we can use teh fact that teh two losts are always sorted to our advantage in terms of time and space 
        # quick question:
        # are the list1 and list 2 sorted i.e 1->2->4 3->4  no 
        # the length also might not be the same 
        # are we allowed to create a new list or should we just modufyt one of teh list1 and list2 
        # we can compare teh values at each point and merge it to a new list 
        # if teh lists are diff lengths onec we reach null just append teh longer list nodes whch are remaining because we compare the last npde and the remaining nodes we are going to keep the order 
        dummy = node = ListNode()
        while list1 and list2:
            if list1.val < list2.val:
                node.next = list1 
                list1= list1.next 
            else:
                node.next = list2
                list2 = list2.next 
            node = node.next 
        node.next = list1 or list2 
        return dummy.next
