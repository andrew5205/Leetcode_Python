
# 21. Merge Two Sorted Lists

# Merge two sorted linked lists and return it as a new sorted list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4




# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, a, b):
        # if a and b exist 
        if a and b:
            if a.val > b.val:
                a, b = b, a
            #  recursion
            a.next = self.mergeTwoLists(a.next, b)
        # if one or both list is empty, just return remaining 
        return a or b
    
    
class Solution2:
    def mergeTwoLists(self, l1, l2):
        if l1 is None: return l2
        if l2 is None: return l1
        if l1 is None or l2 is None: return None
        
        head = ListNode(0)
        # pointer current, pointing at head
        current = head
        
        while l1 and l2:
            if l1.val > l2.val:
                current.val = l2
                # move to next element 
                l2 = l2.next
                
            else:
                current.next = l1
                # move to next element 
                l1 = l1.next
            
            current = current.next
        # if one of the list is empty, point to the rest of the none empty list 
        current.next = l1 or l2
        # return all from head node
        return head.next
    