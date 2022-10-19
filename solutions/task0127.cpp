class Solution {
public:
#define len(a) (int)(a).size()
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        if (find(wordList.begin(), wordList.end(), endWord) == wordList.end()) {
            return 0;
        }
        int n = len(wordList);
        int inf = int(1e9+228);
        map<string, int> d;
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
        return (d[endWord] == inf ? 0 : d[endWord]);
    }
};