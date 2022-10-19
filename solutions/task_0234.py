# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def isPalindrome(self, head) -> bool:
        a = []
        while head != None:
            a.append(head.val)
            head = head.next
        ret = True
        n = len(a)
        for i in range(n//2):
            if a[i] != a[n-i-1]:
                ret = False
        return ret
    