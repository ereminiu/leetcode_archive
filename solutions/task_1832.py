from collections import Counter 

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        counter = Counter()
        for c in sentence:
            counter[c] += 1
        for i in range(26):
            c = chr(ord('a')+i)
            if not counter[c]:
                return False 
        return True