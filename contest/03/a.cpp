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


int s1;
vector<int> vec(999, -1);
 
void setup(){
    // #ifndef ONLINE_JUDGE
    // freopen("../input.txt","r",stdin); 
    // freopen("../output.txt","w", stdout);
    // #endif
    ios::sync_with_stdio(false);
    cin.tie(0);
}

int fibo(int n){
    if(vec[n] == -1 ){
        vec[n] = fibo(n-1) + fibo(n-2);
    }
    return vec[n];
}


int64_t solve() {

    cin >> s1;

    vec[1] = 1;
    vec[2] = 1;
    vec[3] = 2;

    cout << fibo(s1) << endl;

    return 0;
}
 
int main() {
    setup();
    solve();
    return 0;
}