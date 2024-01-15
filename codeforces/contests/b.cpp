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
    int n, ans = 0; cin >> n;
    string a, b;
    cin >> a >> b;

    for(int i = 0; i < n; i++) {
        if(a[i] != b[i]) {
            for(int j = i + 1; j < n; j++) {
                if(a[i] != a[j] && a[j] != b[j]) {
                    swap(a[i], a[j]);
                    ans++;
                }
            }
            if(a[i] != b[i]) {
                a[i] = b[i];
                ans++;
            }
        }
    
        if(a == b) return ans;
    }

    return ans;
}
 
int main() {
	setup();

    int t; cin >> t;

    for(int i = 0; i < t; i++) {
        cout << solve() << "\n";
    }
	
	return 0;
}