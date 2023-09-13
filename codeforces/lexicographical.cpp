#include <bits/stdc++.h>
 
using namespace std;
 
#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second
 
typedef long long ll;
typedef unsigned long long llu;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<pii> vpi;
const ll MAX = 1e5+7;
 
void init(){
	#ifndef ONLINE_JUDGE
	freopen("input.txt","r",stdin); 
	freopen("output.txt","w",stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

int64_t solve() {
	string s;
	int k, n;
	cin >> s >> k;
	vector<vector<char>> ans(MAX);

	n = s.size();

	FOR(i, 0, n) ans[i % k].PB(s[i]);

	FOR(i, 0, k) sort(all(ans[i]));

	FOR(j, 0, n / k + 1) FOR(i, 0, k) 
		j < ans[i].size() ? cout << ans[i][j] : cout << "\n";

	return 0;
}
 
int main() {
	init();
	solve();
	return 0;
}