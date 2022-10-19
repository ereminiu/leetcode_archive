class Solution:
    def largestInteger(self, num: int) -> int:
        parity = []
        odd = []
        even = []
        while num > 0:
            if (num%10) % 2 == 0:
                parity.append(0)
                even.append(num%10)
            else:
                parity.append(1)
                odd.append(num%10)
            num //= 10
        p = 0; q = 0
        ans = 0
        parity = parity[::-1]
        even.sort(reverse=True)
        odd.sort(reverse=True)
        for i in range(len(parity)):
            ans *= 10
            if parity[i] == 0:
                ans += even[p]
                p += 1
            else:
                ans += odd[q]
                q += 1
        return ans