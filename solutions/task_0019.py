# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n: int):
        a = []
        while head != None:
            a.append(ListNode(head.val))
            head = head.next
        del a[len(a)-n]
        for i in range(len(a)-1):
            a[i].next = a[i+1]
        return a[0] if len(a) else None