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
    int n, ans = 0; cin >> n;

    ans += n;
    ans += 2 * (n / 2);
    ans += 2 * (n / 3); 

    return ans;
}
 
int main() {
    freopen("../input.txt","r",stdin); 
    freopen("../output.txt","w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);

    int t; cin >> t;
    while(t--) cout << solve() << "\n";
    return 0;
}