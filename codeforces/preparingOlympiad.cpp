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
 
void setup(){
    #ifndef ONLINE_JUDGE
    freopen("../input.txt","r",stdin); 
    freopen("../output.txt","w", stdout);
    #endif
    ios::sync_with_stdio(false);
    cin.tie(0);
}

int64_t solve() {
    int n, l, r, x, ans = 0; cin >> n >> l >> r >> x;
    vi v(n);

    FOR(i, 0, n) cin >> v[i];
        
    for(int mask = 0; mask < (1 << n); mask++) {
        vi chosen;
        int mi = INF, ma = 0, t = 0;
        for(int i = 0; i < n; i++) {
            if(mask & (1 << i)) {
                if(v[i] > ma) ma = v[i];
                if(v[i] < mi) mi = v[i]; 
                t += v[i];
            }
        }
        
        if(l <= t && t <= r && ma - mi >= x) {
            ans++;
        }
    }

    return ans;
}
 
int main() {
    setup();
    cout << solve() << "\n";
    return 0;
}