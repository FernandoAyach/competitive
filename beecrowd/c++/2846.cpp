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

int fib[30];

int numberOfFibonots(int k) {
	int p = distance(fib, upper_bound(fib, fib + 30, k));
	return k - p;
}

int64_t solve() {
	fib[0] = 1;
	fib[1] = 2;
	FOR(i, 2, 30) fib[i] = fib[i - 1] + fib[i - 2];

	int l = 0, r = MAX, m, k;
	cin >> k;

	while(r > l + 1) {
		m = l + (r - l) / 2;
		if(numberOfFibonots(m) >= k) r = m;
		else l = m;
	}
	return r;
}
 
int main() {
	setup();
	cout << solve() << "\n";
	return 0;
}