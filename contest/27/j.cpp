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
const ll MAX = 1e5+7;

int anamariabraga(int n, int p) {
    if(n == 1) return 0;
    
    return (anamariabraga(n - 1, p) + p % n);
}
 
int64_t solve() {
    int n, p;
    while(cin >> n >> p) {
        cout << anamariabraga(n, p) << "\n";
    }
    return 0;
}
 
int main() {
    freopen("../../input.txt","r",stdin); 
    freopen("../../output.txt","w", stdout);
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}