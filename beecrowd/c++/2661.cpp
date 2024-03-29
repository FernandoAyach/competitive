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

bool despojado(ll x) {
    int c = 0;

    for(ll i = 2; i * i <= x; i++) {
        if(x % i == 0) {
            x /= i;
            c++;
            while(x % i == 0) {
                return false;
            }
        }
    }
    if(x > 1) c++;

    if(c < 2) return false;

    return true;
}

int64_t solve() {
    ll n, ans = 0; cin >> n;

    for(ll i = 1; i * i <= n; i++) {
        if(n % i == 0) {
            if(despojado(i)) ans++;
            if(i != n / i && despojado(n / i)) ans++;
        }
    }
   
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