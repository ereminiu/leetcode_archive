class Solution {
public:
#define len(a) (int)(a).size()
    map<string, int> d;
    string beg;
    vector<vector<string>> ans;
    
    void go(string& s, vector<string>& path) {
        if (s == beg) {
            auto ret = path;
            reverse(ret.begin(), ret.end());
            ans.push_back(ret);
            return;
        }
        for (int i = 0; i < len(s); i++) {
            string t = s;
            char old = t[i];
            for (int x = 0; x < 26; x++) {
                char c = 'a'+x;
                t[i] = c;
                if (d[t] == d[s]-1) {
                    path.push_back(t);
                    go(t, path);
                    path.pop_back();
                }
            }
            t[i] = old;
        }
    }
    
    vector<vector<string>> findLadders(string beginWord, string endWord, vector<string>& wordList) {
        if (find(wordList.begin(), wordList.end(), endWord) == wordList.end()) {
            return vector<vector<string>>();
        }
        beg = beginWord;
        int n = len(wordList);
        int inf = int(1e9+228);
        for (const string& s : wordList) {
            d[s] = inf;
        }
        d[beginWord] = 1;
        set<string> st;
        for (string s : wordList) {
            st.insert(s);
        }
        queue<string> q;
        q.push(beginWord);
        while (not q.empty()) {
            string v = q.front();
            q.pop();
            string u = v;
            for (int i = 0; i < len(v); i++) {
                char old = v[i];
                for (int x = 0; x < 26; x++) {
                    char c = 'a'+x;
                    u[i] = c;
                    if (st.count(u) and d[u] > d[v]+1) {
                        d[u] = d[v]+1;
                        q.push(u);
                    }
                }
                u[i] = old;
            }
        }
        vector<string> path = {endWord};
        go(endWord, path);
        return ans;
    }
};