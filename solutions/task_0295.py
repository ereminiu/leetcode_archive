from heapq import *

class MedianFinder:

    def __init__(self):
        self.top = []
        self.bot = []

    def addNum(self, num: int) -> None:
        heappush(self.bot, -num)
        heappush(self.top, -heappop(self.bot))
        if len(self.top) > len(self.bot):
            heappush(self.bot, -heappop(self.top))

    def findMedian(self) -> float:
        if len(self.bot) != len(self.top):
            return -self.bot[0]
        return (self.top[0]-self.bot[0]) / 2