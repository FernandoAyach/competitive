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
    vpi coor(4);
    vi d(4);

    for(int i = 0; i < 4; i++) {
        int a, b; cin >> a >> b;
        coor[i].first = a;
        coor[i].second = b;
    }

    for(int i = 0; i < 4; i++) {
        for(int j = 0; j < 4; j++) {
            if(i == j) continue;
            if(coor[i].first != coor[j].first && coor[i].second != coor[j].second) continue;
            int d = 
            (coor[i].first - coor[j].first) * (coor[i].first - coor[j].first) + 
            (coor[i].second - coor[j].second) * (coor[i].second - coor[j].second);
            return d;
        }
    }
    return 0;
}
 
int main() {
	setup();

    int t; cin >> t;

    for(int i = 0; i < t; i++) {
        cout << solve() << "\n";
    }
	
	return 0;
}