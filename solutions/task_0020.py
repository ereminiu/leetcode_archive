class Solution:
    def isValid(self, s: str) -> bool:
        def isOpen(c):
            return c == '(' or c == '[' or c == '{'
        
        def match(a, b):
            op = ['(', '[', '{']
            cl = [')', ']', '}']
            for i in range(3):
                if a == op[i] and b == cl[i]:
                    return True
            return False
        
        st = []
        for c in s:
            if isOpen(c):
                st.append(c)
            else:
                if not st or not match(st.pop(), c):
                    return False
        return len(st) == 0