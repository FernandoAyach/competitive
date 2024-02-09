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
	freopen("../../../input.txt","r",stdin); 
	freopen("../../../output.txt","w", stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

int64_t solve() {
	int n; cin >> n;

    vi letters(26, 0);

    FOR(i, 0, n) {
        int trace; cin >> trace;

        FOR(j, 0, 26) {
            if(letters[j] == trace) {
                char l =  j + 90;
                cout << l;
                letters[j]++;
            }
        }
    }

    cout << "\n";

    return 0;
}
 
int main() {
	setup();

	int t; cin >> t;
	while(t--) solve();
    
	return 0;
}