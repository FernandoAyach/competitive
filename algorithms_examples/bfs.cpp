#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <string>
#include <sstream>
#include <set>
#include <bitset>
#include <queue>
 
using namespace std;
 
#define FOR(i, n) for (int i = 0; i < (int)n; i++)
#define PRINT(v, n) for (int i = 0; i < (int)n; i++) cout << v[i] << " \n"[i==n-1]
 
#define PB push_back
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
 
typedef long long ll;
typedef vector<int> vi;
 
const ll MOD = 1e8;
const int INF = 0x3f3f3f3f;
const char nl = '\n';
const char sep = ' ';
 
const string YES = "YES";
const string NO = "NO";
 
const int MAX = 1e5+7;
vi graph[MAX];
int dist[MAX], par[MAX];
bitset<MAX> vis;
 
int64_t solve() {
  int n, m; cin >>n >> m;
  FOR(i, n) dist[i] = -1;
  FOR(i, m){
    int a, b; cin >>a >> b;
    --a; --b;
    graph[a].PB(b);
    graph[b].PB(a);
  }
 
  queue<int> q;
  q.push(0);
  dist[0] = 0;
  vis[0]=1;
  while(!q.empty()){
    int u = q.front(); q.pop();
    for(auto& v : graph[u]){
      if(!vis[v]){
        vis[v]=1;
        q.push(v);
        dist[v] = dist[u]+1;
        par[v]=u;
      }
    }
  }
 
  if(dist[n-1] == -1){
    cout << "IMPOSSIBLE\n";
    return 0;
  }
 
  cout << dist[n-1]+1 << '\n';
  vi path;
  int x = n-1;
  while(x!=0){
    path.PB(x);
    x = par[x];
  }
  path.PB(x);
 
  reverse(all(path));
  FOR(i, path.size())
    cout << path[i]+1 << " \n"[i+1==path.size()];
 
  return 0;
}
 
int main() {
  ios::sync_with_stdio(false);
  cin.tie(0);
 
  solve();
  
  return 0;
}