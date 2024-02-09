#include <bits/stdc++.h>
#include <math.h>
 
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


int s1;
 
void setup(){
    ios::sync_with_stdio(false);
    cin.tie(0);
}



int64_t solve() {

    cin >> s1;

    llu result = pow(2, s1) - 1;

    cout << std::to_string(result) << endl;

    return 0;
}
 
int main() {
    setup();
    solve();
    return 0;
}