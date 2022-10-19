class Solution {
public:
    int countPrimes(int n) {
        vector<bool> isprime(n+228, true);
        isprime[0] = isprime[1] = false;
        for (int i = 0; i < n; i++) {
            if (not isprime[i] or 1LL * i * i > n) {
                continue;
            }
            for (int j = i*i; j < n; j += i) {
                isprime[j] = false;
            }
        }
        int ans = 0;
        for (int i = 0; i < n; i++) {
            ans += isprime[i];
        }
        return ans;
    }
};