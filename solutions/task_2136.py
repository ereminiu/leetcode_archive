class Solution:
    def earliestFullBloom(self, plantTime, growTime) -> int:
        cur, res = 0, 0
        
        def f(i): 
            return -growTime[i]
        
        order = sorted(range(len(plantTime)), key=f())
        for i in order:
            cur += plantTime[i]
            res = max(res, cur+growTime[i])
        return res