#include <iostream>
#include <vector>
#include <algorithm>
#include <string>
#include <cmath>
#include <iomanip>

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

    ll v, p; cin >> v >> p;
    cout << fixed;
    FOR(i, 1, 9) {
        cout << (int)(ceil((p * v * i) / 10.0)) << " ";
    }
    cout << (int)(ceil((p * v * 9) / 10.0)) << "\n";
    
    return 0;
}