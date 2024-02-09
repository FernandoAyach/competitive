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

int n, c, backup;
vi impostos(MAX);

vpi graph[MAX];
vi dist;
vb vis(MAX, false);
int ans = 0;

vi dijkstra(int r) {
    vi dist(n, INF);
    set<pii> q;
    dist[0] = 0;
    q.insert({0, r});

    while(!q.empty()) {
        auto [p, u] = *(q.begin());
        q.erase(q.begin());

        if(p > dist[u]) continue;

        for(auto& [w, v] : graph[u]) {
            if(w + dist[u] < dist[v]) {
                dist[v] = w + dist[u];
                q.insert({dist[v], v});
            }
        }
    }

    return dist;
}

// Talvez tenha q voltar na cidade se o ouro que estiver ali for grande
// demais para a carroça

// Se encher a carroça, onde colocar o ouro
// qual vai ser a prioridade

void obterDistancia(int u) {

    for(auto [w, v] : graph[u]) {
        if(!vis[v]) {
            c -= impostos[v];
            if(impostos[v] >= c) {
                ans += w + dist[v] * ceil(impostos[v] / c);
                c = backup;
            } else ans += w;
            
            vis[v] = true;
            obterDistancia(v);
        } 
    }
}

int64_t solve() {
    cin >> n >> c;
    backup = c;
    
    FOR(i, 0, n) cin >> impostos[i];

    FOR(i, 0, n - 1) {
        int a, b, w; cin >> a >> b >> w;
        --a; --b;
        graph[a].push_back({w, b});
        graph[b].push_back({w, a});
    }

    dist = dijkstra(0);

    vis[0] = true;
    obterDistancia(0);

    return ans;
}
 
int main() {
    freopen("../../input.txt","r",stdin); 
    freopen("../../output.txt","w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);

    cout << solve() << "\n";
    return 0;
}