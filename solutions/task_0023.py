from heapq import*

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists):
        n = len(lists)
        a = []
        h = []
        # print(n)
        for i in range(n):
            if lists[i] != None:
                heappush(h, (lists[i].val, i))
        # print(h)
        while len(h) > 0:
            val, idx = heappop(h)
            if lists[idx].next != None:
                lists[idx] = lists[idx].next
                heappush(h, (lists[idx].val, idx))
            a.append(ListNode(val))
        for i in range(len(a)-1):
            a[i].next = a[i+1]
        root = None if len(a) == 0 else a[0]
        return root