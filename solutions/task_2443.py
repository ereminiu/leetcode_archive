class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        def rev(x):
            ret = 0
            while x > 0:
                ret *= 10
                ret += x % 10
                x //= 10
            return ret
        
        if num == 0:
            return True
        
        for x in range(num):
            if x + rev(x) == num:
                return True
        return False