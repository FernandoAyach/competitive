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
	string strip; cin >> strip;

	int l = 0, r = n - 1;

	while(l < r && (strip[l] == 'W' || strip[r] == 'W')) {
		if(strip[l] == 'W') l++;
		if(strip[r] == 'W') r--;
	}
    
    return r - l + 1;
}
 
int main() {
	setup();

	int t; cin >> t;
	while(t--) cout << solve() << "\n";
    
	return 0;
}