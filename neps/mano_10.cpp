#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>

using namespace std;

#define FOR(i, n) for (int i = 1; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second

#define INF 1000000000
#define MAX 1007

typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef pair<int, int> pii;

int n, m;
vi coins(MAX);
vi s(MAX);

int64_t solve(int A) {
    s[0] = 0;
    
    FOR(i, A + 1) {
        s[i] = INF;
        FOR(j, n) {
            if(coins[j] <= i) s[i] = min(s[i], 1 + s[i - coins[j]]);
        }
    }

    return s[A];
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    cin >> n >> m;

    FOR(i, n) cin >> coins[i];
    
    cout << (solve(m) < 10 ? "S\n" : "N\n");
   
    return 0;
}