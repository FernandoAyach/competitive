#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <string>
#include <sstream>
#include <set>

using namespace std;

#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second

#define INF 1000000007
const int SIZE =  2e5+7;

typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef pair<int, int> pii;

int n, m;
vector<pii> graph[SIZE];

vi dijkstra(int s){
    vi dist(n, INF);
    set<pii> q;

    dist[s] = 0;
    q.insert({0, s});

    while(!q.empty()){
        auto [d, u] = *q.begin();
        q.erase(q.begin());

        if(d > dist[u]) continue;

        for(auto& [c, v] : graph[u]) {
            if(dist[u] + c < dist[v]) {
                dist[v] = dist[u] + c;
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
        int a, b, p;
        cin >> a >> b >> p;
        --a; --b;
        graph[a].push_back({p, b});
        graph[b].push_back({p, a});
    }

    vi di = dijkstra(0);
    vi df = dijkstra(n - 1);

    int ans = INF;
    FOR(i, 0, x) {
        int f; cin >> f;
        --f;
        ans = min(ans, di[f] + df[f]);
    }

    return ans;
}

int main() {
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    cout << solve() << "\n";

    return 0;
}