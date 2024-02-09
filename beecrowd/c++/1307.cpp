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

int toDecimal(string s) {
    int ans = 0, p = s.size() - 1;
    for(int i = 0; i < s.size(); i++) {
        int n = s[i] - '0';
        ans += n * pow(2, p);
        p--;
    }
    return ans;
}

int64_t solve(int n) {
    string s1, s2; cin >> s1 >> s2;
    int b1 = toDecimal(s1), b2 = toDecimal(s2);

    if(gcd(b1, b2) != 1) cout << "Pair #" << n << ": All you need is love!" << "\n";
    else cout << "Pair #" << n << ": Love is not all you need!" << "\n";

    return 0;
}
 
int main() {
	setup();

    int t; cin >> t;
    for(int i = 0; i < t; i++) {
        solve(i + 1);
    }
	
	return 0;
}