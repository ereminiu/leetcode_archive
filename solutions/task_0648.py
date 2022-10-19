class Solution:
    def replaceWords(self, dictionary, sentence: str) -> str:
        d = set()
        words = list(sentence.split())
        for s in dictionary:
            d.add(s)
        ans = ''
        for w in words:
            pref = ''
            fl = False
            for i in range(len(w)):
                pref += w[i]
                if pref in d:
                    ans += pref + ' '
                    fl = True
                    break
            if not fl:
                ans += w + ' '
        ret = ans[:len(ans)-1]  
        return ret