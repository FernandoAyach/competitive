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
    int n, ans = 0, diff = 0, r; cin >> n;
    string s1, s2, s3; cin >> s1 >> s2;

    FOR(i, 0 , n) {
        if(s1[i] != s2[i]) diff++;
    }

    ans = diff / 2;

    if(diff % 2 == 1) ans++;

    return ans;
}
 
int main() {
	setup();

    int t; cin >> t;
    while(t--)  cout << solve() << "\n";
	return 0;
}