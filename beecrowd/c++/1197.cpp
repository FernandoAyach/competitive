#include <bits/stdc++.h>

using namespace std;

#define FOR(i, n) for (int i = 1; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second

typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef pair<int, int> pii;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int v, t;
    while(cin >> v >> t) {
        if(t == 0) {
            cout << 0 << "\n";
            continue;
        }
        double a = (double)v / (double)t;
        cout << 2 * (t * t) * a << "\n";
    }

    return 0;
}