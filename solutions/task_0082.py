# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def getNextVal(self, node):
        if node.next == None:
            return -228
        return node.next.val
    
    def deleteDuplicates(self, head):
        root = ListNode(0, head)
        prev = root
        while head:
            if head.next and head.val == head.next.val:
                while head.next and head.val == head.next.val:
                    head = head.next
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        return root.next