#include <bits/stdc++.h>
 
using namespace std;
 
#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
 
typedef long long ll;
typedef unsigned long long llu;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<pii> vpi;

const ll INF = 1e9+7;
const ll MAX = 1e5+7;
 
int64_t solve() {
    int n, ma = -1, mi = 61; cin >> n;

    FOR(i, 0, n) {
        int a; cin >> a;
        if(a > ma) ma = a;
        if(a < mi) mi = a;
    }

    return ma - mi;
}
 
int main() {
    //freopen("../../input.txt","r",stdin); 
    //freopen("../../output.txt","w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    cout << solve() << "\n";
    return 0;
}