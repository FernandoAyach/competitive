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

const ll INF = 1e9+7;
const ll MAX = 5e5+7;
 
void init(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

int n, m;
vpi graph[MAX];

vi dijkstra(int r) {    
    vi dist(n, INF);
    set<pii> q;
    dist[r] = 0;
    q.insert({0, r});

    while(!q.empty()) {
        auto [d, u] = *(q.begin());
        q.erase(q.begin());

        if(d > dist[u]) continue;

        for(auto& [w, v] : graph[u]) {
            if(dist[u] + w < dist[v]) {
                dist[v] = dist[u] + w;
                q.insert({dist[v], v});
            }
        }
    }
    return dist;
}

int64_t solve() {
	int x;
    cin >> n >> m >> x;

    FOR(i, 0, m) {
        int u, v, w;
        cin >> u >> v >> w;
        --u; --v;

        graph[u].push_back({w, v});
        graph[v].push_back({w, u});
    }

    vi dd = dijkstra(0);
    vi dn = dijkstra(n - 1);
    int best = INF;

    FOR(i, 0, x) {
        int f; cin >> f; --f;
        best = min(best, dd[f] + dn[f]);
    }

    return best;
}
 
int main() {
	init();
	cout << solve() << "\n";
	return 0;
}