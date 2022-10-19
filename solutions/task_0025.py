# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head, k: int):
        a = [[head.val]]

        head = head.next
        while head != None:
            if len(a[-1]) == k:
                a[-1] = a[-1][::-1]
                a.append([head.val])
            else:
                a[-1].append(head.val)
            head = head.next
        if len(a[-1]) == k:
            a[-1] = a[-1][::-1]
                
        
        vals = []
        for x in a:
            for y in x:
                vals.append(ListNode(y))
        
        for i in range(1, len(vals)):
            vals[i-1].next = vals[i]
        return vals[0]