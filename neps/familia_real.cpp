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

int n, m, nGen = 0;
vi graph[MAX];
vb vis(MAX, false);
vi dist(MAX, 0);

void bfs(int u) {
	queue<int> queue;
	vis[u] = true;
	queue.push(u);
	dist[u] = 0;

	while(!queue.empty()) {
		int f = queue.front();
		queue.pop();

		for(auto& v : graph[f]) {
			if(!vis[v]) {
				vis[v] = true;
				dist[v] = dist[f] + 1;
				if(dist[v] > nGen) nGen = dist[v];
				queue.push(v);
			}
		}
	}
}

int64_t solve() {
	cin >> n >> m;
	vi gen(MAX, 0);
	vi came(MAX, 0);

	FOR(i, 1, n + 1) {
		int a; cin >> a;
		graph[a].PB(i);
	}

	bfs(0);

	FOR(i, 1, n + 1) {
		gen[dist[i]]++;
	}

	FOR(i, 0, m) {
		int g; cin >> g;
		came[dist[g]]++;
	}

	cout << fixed << setprecision(2);
	FOR(i, 1, nGen + 1) {
		cout << (came[i] / (float)gen[i]) * 100 << " \n"[i == n];
	}

	return 0;
}
 
int main() {
	init();
	solve();
	return 0;
}