struct segtree {
#define ll long long
    vector<ll> f;
    vector<int> lazy;
    int n;
    segtree(vector<int>& a) {
        n = a.size();
        f.resize(4 * n);
        lazy.resize(4 * n, 0);
        build(0, 0, n, a);
    }
    void build(int v, int vl, int vr, vector<int>& a) {
        if (vl == vr - 1) {
            f[v] = a[vl];
            return;
        }
        int mid = (vl + vr) / 2;
        build(2 * v + 1, vl, mid, a);
        build(2 * v + 2, mid, vr, a);
        f[v] = f[2 * v + 1] + f[2 * v + 2];
    }
    void push(int v, int vl, int vr) {
        if (lazy[v] != 0) {
            f[v] += (vr-vl) * lazy[v];
            if (vl != vr - 1) {
                lazy[2 * v + 1] += lazy[v];
                lazy[2 * v + 2] += lazy[v];
            }
            lazy[v] = 0;
        }
    }
    ll get(int v, int vl, int vr, int l, int r) {
        push(v, vl, vr);
        if (l >= vr || vl >= r) {
            return 0;
        }
        if (vl >= l && r >= vr) {
            return f[v];
        }
        int mid = (vl + vr) / 2;
        return get(2 * v + 1, vl, mid, l, r) + get(2 * v + 2, mid, vr, l, r);
    }
    void add(int v, int vl, int vr, int l, int r, int x) {
        push(v, vl, vr);
        if (l >= vr || vl >= r) {
            return;
        }
        if (vl >= l && r >= vr) {
            lazy[v] += x;
            push(v, vl, vr);
            return;
        }
        int mid = (vl + vr) / 2;
        add(2 * v + 1, vl, mid, l, r, x);
        add(2 * v + 2, mid, vr, l, r, x);
        f[v] = f[2 * v + 1] + f[2 * v + 2];
    }
    ll get(int l, int r) {
        return get(0, 0, n, l, r);
    }
    void add(int l, int r, int x) {
        add(0, 0, n, l, r, x);
    }
    void print() {
        for (int i = 0; i < n; i++) {
            cerr << get(i, i+1) << ' ';
        }
        cerr << endl;
    }
};

class Solution {
public:
    string shiftingLetters(string s, vector<vector<int>>& shifts) {
        int n = int(s.size());
        vector<int> empty(n, 0);
        segtree st = segtree(empty);
        for (auto p : shifts) {
            int l=p[0], r=p[1], x=p[2];
            if (x == 0) x = -1;
            st.add(l, r+1, x);
        }
        // st.print();
        int alphaSize = 26;
        string ans(n, 'a');
        for (int i = 0; i < n; i++) {
            int k = (((((s[i]-'a') + st.get(i, i+1)) % alphaSize) + alphaSize) % alphaSize);
            ans[i] = char('a' + k);
        }
        return ans;
    }
};