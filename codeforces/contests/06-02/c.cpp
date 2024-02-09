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
	freopen("../../../input.txt","r",stdin); 
	freopen("../../../output.txt","w", stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

int64_t solve() {
	int n; cin >> n;
	vi a(n);

    FOR(i, 0, n) cin >> a[i];

    int q; cin >> q;

    FOR(i, 0, q) {
        int l, r; cin >> l >> r;
        bool stop = false;

        for(; l - 1 < r; l++) {
            if(a[l - 1] != a[r - 1]) {
                cout << l - 1 << " " << r - 1 << "\n";
                stop = true;
                break;
            }
        }

        if(stop) cout << "-1 -1\n";
        cout << '\n';
    }

    
    return 0;
}
 
int main() {
	setup();

	int t; cin >> t;
	while(t--) solve();
    
	return 0;
}