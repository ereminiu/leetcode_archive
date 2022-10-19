class MyCalendarThree:

    def __init__(self):
        self.opening = []
        self.closing = []
    
    def book(self, start: int, end: int) -> int:
        self.opening.append(start)
        self.closing.append(end)
        self.opening.sort()
        self.closing.sort()
        
        ans = 0
        p = 0
        for i in range(len(self.opening)):
            while self.closing[p] <= self.opening[i]:
                p += 1
            ans = max(ans, i-p+1)
        return ans


# Your MyCalendarThree object will be instantiated and called as such:
# obj = MyCalendarThree()
# param_1 = obj.book()