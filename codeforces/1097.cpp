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
    int n; cin >> n;
    vi rot(n);
    for(int i = 0; i < n; i++) cin >> rot[i];

    for(int mask = 0; mask < (1 << n); mask++) {
        int sum = 0;
        
        for(int i = 0; i < n; i++) {
            if(mask & (1 << i)) sum += rot[i];
            else sum -= rot[i];
            sum %= 360;
        }
        sum = abs(sum);

        if(sum == 0 || sum == 360) {
            cout << "YES\n";
            return 0;
        }
    }

    cout << "NO\n";
    return 0;
}
 
int main() {
	setup();
	solve();
	return 0;
}