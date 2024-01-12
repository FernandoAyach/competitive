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
vi mem(MAX, -1);

int change(int m) {
	if(mem[m] != -1) return mem[m];
	if(!m) return 0;

	int ans = INF;

	for(int i = 0; i < n; i++) {
		if(m - coins[i] >= 0) {
			ans = min(ans, 1 + change(m - coins[i]));
		}
	}

	mem[m] = ans;
	
	return ans;
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