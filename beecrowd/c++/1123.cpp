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
const ll MAX = 300;
 
void init(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

int n, m, c, k;

vi dijkstra(int r, vpi graph[]) {
    vi dist(n, INF);
    set<pii> q;
    dist[r] = 0;
    q.insert({0, r});

    while(!q.empty()) {
        auto [d, u] = *q.begin();
        q.erase(q.begin());

        if(d > dist[u]) continue;

        for(auto& [w, v] : graph[u]) {
            if(u < c - 1) {
                if(dist[u] + w < dist[v] && v == u + 1) {
                    dist[v] = dist[u] + w;
                    q.insert({dist[v], v});
                }
            } else {
                if(dist[u] + w < dist[v]) {
                    dist[v] = dist[u] + w;
                    q.insert({dist[v], v});
                }
            }
        }
    }
    return dist;
}

int64_t solve() {
    vpi graph[MAX];

    FOR(i, 0, m) {
        int x, y, z; cin >> x >> y >> z;
        graph[x].PB({z, y});
        graph[y].PB({z, x});
    }

    vi dist = dijkstra(k, graph);

    return dist[c - 1];
}
 
int main() {
	init();

    cin >> n >> m >> c >> k;
    while(n != 0) {
        cout << solve() << "\n";
        cin >> n >> m >> c >> k;
    }
    
	return 0;
}