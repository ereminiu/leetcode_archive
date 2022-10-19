# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head):
        a = []
        while head != None:
            a.append(ListNode(head.val))
            head = head.next
        n = len(a)
        del a[n//2]
        for i in range(1, len(a)):
            a[i-1].next = a[i]
        return None if not a else a[0]