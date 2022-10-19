# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1, l2):
        a = []
        while l1 != None:
            a.append(l1.val)
            l1 = l1.next
        x = 0
        for i in range(len(a)-1, -1, -1):
            x *= 10
            x += a[i]
        b = []
        while l2 != None:
            b.append(l2.val)
            l2 = l2.next
        y = 0
        for i in range(len(b)-1, -1, -1):
            y *= 10
            y += b[i]
        sum = x+y
        ret = []
        if sum == 0:
            ret.append(0)
        while sum > 0:
            ret.append(sum%10)
            sum //= 10
        Node = ListNode(ret[0])
        FirstNode = Node
        for i in range(1, len(ret)):
            Node.next = ListNode(ret[i])
            Node = Node.next
        return FirstNode