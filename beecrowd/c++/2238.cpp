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
const ll MAX = 1e9+7;
 
void setup(){
	#ifndef ONLINE_JUDGE
	freopen("../../input.txt","r",stdin); 
	freopen("../../output.txt","w", stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

set<int> possible;

void getDividers(int c) {
	for(int i = 1; i * i <= c; i++) {
		if(c % i == 0) {
			possible.insert(i);
			if(c / i != i) possible.insert(c / i);
		}
	}
}

int64_t solve() {	
	int a, b, c, d, j;
	cin >> a >> b >> c >> d;

	getDividers(c);

	for(auto& n : possible) { // O(sqrt(n))
		if(n % a == 0 && n % b != 0 && d % n != 0) {
			return n;
		} 
	}
	return -1;
}
 
int main() {
	setup();
	cout << solve() << "\n";
	return 0;
}