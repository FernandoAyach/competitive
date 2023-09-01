#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>

using namespace std;

#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second

#define INF 1000000007
#define MAX 1000007
#define SIZE 30

typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef pair<int, int> pii;

vi c(SIZE);
vi s(MAX);

int n;

int64_t solve(int A) {
    s[0] = 0;

    FOR(i, 1, A + 1) {
        s[i] = INF;
        FOR(j, 0, n) {
            if(c[j] <= i) s[i] = min(s[i], 1 + s[i - c[j]]);
        }
    }

    return s[A];
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int t, m; 
    cin >> t;

    while(t--) {
        cin >> n >> m;
        FOR(i, 0, n) cin >> c[i];
        cout << solve(m) << "\n";
    }
    
    return 0;
}