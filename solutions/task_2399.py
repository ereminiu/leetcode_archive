class Solution:
    def checkDistances(self, s: str, distance) -> bool:
        fin, fout = 26 * [-1], 26 * [-1]
        for i in range(len(s)):
            c = s[i]
            idx = ord(c)-ord('a')
            if fin[idx] == -1:
                fin[idx] = i
            else:
                fout[idx] = i
        for i in range(len(distance)):
            if fin[i] == fout[i] and fin[i] == -1:
                continue
            if fout[i]-fin[i]-1 != distance[i]:
                return False
        return True