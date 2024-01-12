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
const ll MAX = 1e4+7;

void setup() {
	#ifndef ONLINE_JUDGE
	freopen("../../input.txt","r", stdin); 
	freopen("../../output.txt","w", stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

int64_t solve() {
    string cipher, crib; 
    getline(cin, cipher);
    getline(cin, crib);
    int ans = 0, j = 0;

    for(int i = 0; i <= cipher.size() - crib.size(); i++) {
        bool count = true;
        j = i;
        for(auto& c : crib) {
            if(c == cipher[j]) {
                count = false;
                break;
            }
            j++;
        }
        if(count) ans++;
    }
	
	return ans;
}
 
int main() {
	setup();
	cout << solve() << "\n";
	return 0;
}