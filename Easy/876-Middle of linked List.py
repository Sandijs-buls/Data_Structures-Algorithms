```python
"""
Problem Number: 876
Problem Title: Middle of Linked List
Difficulty: Easy

Problem Summary:
    Given the head of a singly linked list, return the middle node of the linked list.
    If there are two middle nodes, return the second middle node.

Approach:
    Use the two-pointer (slow and fast) technique. Both pointers start at the head.
    The fast pointer moves two steps at a time while the slow pointer moves one step
    at a time. When the fast pointer reaches the end of the list, the slow pointer
    will be at the middle node.
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:

        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow
```