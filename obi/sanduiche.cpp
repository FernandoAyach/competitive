#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>

using namespace std;

#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
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

    int n, m, t;
    cin >> n >> m;

    vector<pii> pairs(m);

    FOR(i, 0, m) {
        int f, s;
        cin >> f >> s;
        pairs[i].F = f;
        pairs[i].S = s;
    }

    if(m == 0) {
        t = pow(2, n) - 1;
    } else {
        t = (pow(2, n) - 1) - (1 + (n - 2 * m));
    }
    

    cout << t << "\n";
    
    return 0;
}

