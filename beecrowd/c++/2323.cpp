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
const ll MAX = 1e4+7;

void setup() {
	#ifndef ONLINE_JUDGE
	freopen("../../input.txt","r", stdin); 
	freopen("../../output.txt","w", stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

vi graph[MAX];
vb vis(MAX);

int n;
bool balanced = true;

int isBalanced(int u) {
	int f = 0, p = 0, t = 0;
	vis[u] = true;

	for(auto& v : graph[u]) {
		p = f;
		if(!vis[v]) {
			f = isBalanced(v);
			t += f;
		}

		if(p != 0 && p != f) balanced = false;
	}

	return t + 1;
}

int64_t solve() {
	cin >> n;

	for(int i = 0; i < n; i++) {
		int a, b; cin >> a >> b;
		graph[a].push_back(b);
		graph[b].push_back(a);
	}

	isBalanced(0);

	cout << (balanced ? "bem" : "mal") << "\n";
	
	return 0;
}
 
int main() {
	setup();
	solve();
	return 0;
}