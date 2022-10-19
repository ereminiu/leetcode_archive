class Solution {
public:
    vector<int> findAnagrams(string s, string p) {
        if (int(s.size()) < int(p.size())) {
            return {};
        }
        vector<int> cur(30);
        vector<int> shouldBe(30);
        for (int i = 0; i < int(p.size()); i++) {
            cur[s[i]-'a'] += 1;
            shouldBe[p[i]-'a'] += 1;
        }
        vector<int> ans;
        if (cur == shouldBe) {
            ans.push_back(0);
        }
        int lnp = int(p.size());
        for (int i = lnp; i < int(s.size()); i++) {
            cur[s[i-lnp]-'a'] -= 1;
            cur[s[i]-'a'] += 1;
            if (cur == shouldBe) {
                ans.push_back(i-lnp+1);
            }
        }
        return ans;
    }
};