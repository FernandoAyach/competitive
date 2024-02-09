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

int64_t solve() {
    int n; cin >> n;
    vector<string> w(n);

    FOR(i, 0, n) {
        cin >> w[i];
    }

    sort(w.begin(), w.end());

    for(int i = n - 1; i >= 0; i--) {
        for(int j = 0; j < i; j++) {
            if(w[j].size() > w[j + 1].size()) {
                swap(w[j], w[j + 1]);
            }   
        }
    }

    FOR(i, 0, n) {
        cout << w[i] << endl;
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