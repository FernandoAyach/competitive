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
	freopen("../../input.txt","r",stdin); 
	freopen("../../output.txt","w", stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

int64_t solve() {
    ll n, f, a, b; cin >> n >> f >> a >> b;
    vi m(n);

    for(int i = 0; i < n; i++) cin >> m[i];
    
    for(int i = 0; i < n; i++) {
        if(i != 0) {
            if((m[i] - m[i - 1]) * a > b) f -= b; 
            else f -= (m[i] - m[i - 1]) * a;
        } else {
            if((m[i] - i) * a > b) f -= b; 
            else f -= (m[i] - i) * a;
        }
        
        if(f <= 0) {
            cout << "NO\n";
            return 0;
        }
    }
    cout << "YES\n";
    return 0;
}
 
int main() {
	setup();

    int t; cin >> t;

    for(int i = 0; i < t; i++) {
        solve();
    }
	
	return 0;
}