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
 
void setup(){
    #ifndef ONLINE_JUDGE
    freopen("../../input.txt","r",stdin); 
    freopen("../../output.txt","w", stdout);
    #endif
    ios::sync_with_stdio(false);
    cin.tie(0);
}

int d(int x, int y) {
    return (x * x) + (y * y);
}

int64_t solve() {
    int n; cin >> n;
    vi num(n);
    vi pa, im;

    FOR(i, 0, n) {
       int number; cin >> number;
       if(number & 1) im.push_back(number);
       else pa.push_back(number);
    }

    sort(all(pa));
    sort(all(im));

    FOR(i, 0, im.size()) {
        cout << im[i] << " \n"[i == n - 1];
    }

    FOR(i, 0, pa.size()) {
        cout << pa[i] << " \n"[i == pa.size() - 1];
    }

    return 0;

}
 
int main() {
    //setup();
    ios::sync_with_stdio(false);
    cin.tie(0);
    solve();
    return 0;
}