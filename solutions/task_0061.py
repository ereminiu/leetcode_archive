# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import deque

class Solution:
    def rotateRight(self, head, k: int):
        n = 0
        a = []
        dq = deque()
        while head != None:
            a.append(head.val)
            dq.append(head.val)
            head = head.next
            n += 1
        dq.rotate((0 if n == 0 else k%n))
        ret = []
        while dq:
            ret.append(ListNode(dq.popleft()))
            if len(ret) > 1:
                ret[len(ret)-2].next = ret[-1]
        if not ret:
            return None
        return ret[0]