'''
Easy.203. Remove Linked List Elements
Given the head of a linked list and an integer val, 
remove all the nodes of the linked list that has Node.val == val, and return the new head.
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        ans = ListNode(0, head)
        temp = ans
        while temp:
            while temp.next and temp.next.val == val:
                temp.next = temp.next.next
            temp = temp.next

        return ans.next