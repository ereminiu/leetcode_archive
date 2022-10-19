class Solution:
    def countDaysTogether(self, arriveAlice: str, leaveAlice: str, arriveBob: str, leaveBob: str) -> int:
        
        def get(c):
            return ord(c)-ord('0')
        
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        def parse(s):
            m = get(s[0])*10 + get(s[1])
            # print(m)
            ret = 0
            for i in range(m-1):
                ret += days[i]
            ret += get(s[3])*10+get(s[4])
            return ret
        
        la, ra = parse(arriveAlice), parse(leaveAlice)
        lb, rb = parse(arriveBob), parse(leaveBob)
        # print(la, ra, lb, rb)
        intersection = min(ra, rb) - max(la, lb) + 1
        return max(0, intersection)