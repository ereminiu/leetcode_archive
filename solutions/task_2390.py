class Solution:
    def removeStars(self, s: str) -> str:
        n = len(s)
        st = []
        for i in range(n):
            st.append(s[i])
            counter = 0
            while st[-1] == '*':
                st.pop()
                counter += 1
            for i in range(counter):
                st.pop()
        ans = ''
        for ss in st:
            ans += ss
        return ans