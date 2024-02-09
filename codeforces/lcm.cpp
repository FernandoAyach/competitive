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
    int l, r; cin >> l >> r;

    if(2 * l <= r) {
        cout << l << " " << 2 * l << "\n";
        return 0;
    }

    cout << "-1 -1\n";

    return 0;
}
 
int main() {
    //freopen("../input.txt","r",stdin); 
    //freopen("../output.txt","w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while(t--) solve();
    return 0;
}