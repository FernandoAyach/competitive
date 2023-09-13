#include <bits/stdc++.h>
 
using namespace std;
 
#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second
 
typedef long long ll;
typedef unsigned long long llu;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<pii> vpi;
const ll MAX = 1e4+7;
 
void init(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

vi graph[MAX];
vb vis(MAX, false);
int n, m;
bool ok;

int dfs(int u) {
	vis[u] = true;
	int pecas = 1, pecas_filho = -1;

	for(auto& v : graph[u]) {
		if(!vis[v]) {
			int ret = dfs(v);
			pecas += ret;
			if(pecas_filho == -1) pecas_filho = ret;
			else if(pecas_filho != ret) ok = false;
		}
	}
	return pecas;
}

int64_t solve() {
	cin >> n;
	m = n; n++;

	FOR(i, 0, m) {
		int a, b; cin >> a >> b;
		graph[a].PB(b);
		graph[b].PB(a);
	}
	ok = true;
	dfs(0); 	

	cout << (ok ? "bem\n" : "mal\n");
	return 0;
}
 
int main() {
	init();
	solve();
	return 0;
}