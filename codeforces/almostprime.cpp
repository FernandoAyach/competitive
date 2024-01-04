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
	freopen("../input.txt","r",stdin); 
	freopen("../output.txt","w", stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

bool isAlmostPrime(int n) {
    int c = 0;

    for(int i = 2; i * i <= n; i++) {
        if(n % i == 0) {
            c++;
            if(c > 2) return false;
            while(n % i == 0) {
                n /= i;
            }
        }
    }

    if(n > 1) c++;

    if(c != 2) return false;
    return true;
}

int64_t solve() {
    int n, ans = 0; cin >> n;
    for(int i = 1; i <= n; i++) {
        if(isAlmostPrime(i)) ans++;
    }
    return ans;
}
 
int main() {
	setup();
	cout << solve() << "\n";
	return 0;
}