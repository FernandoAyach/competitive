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
const ll MAX = 1e3+7;
 
void setup(){
	#ifndef ONLINE_JUDGE
	freopen("../input.txt","r",stdin); 
	freopen("../output.txt","w", stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

int n, m;
vi coins(MAX);
vi mem(MAX, INF);

int change(int m) {
    mem[0] = 0;

    for(int i = 1; i <= m; i++) {
        for(int j = 0; j < n; j++) {
            if(i - coins[j] >= 0)
                mem[i] = min(mem[i], 1 + mem[i - coins[j]]);
        }
    }

    return mem[m];
}

int64_t solve() {
	cin >> n >> m;
	
	for(int i = 0; i < n; i++) cin >> coins[i];
	
	if(change(m) < 10) cout << "S\n";
	else cout << "N\n";

	return 0;
}
 
int main() {
	setup();
	solve();
	return 0;
}