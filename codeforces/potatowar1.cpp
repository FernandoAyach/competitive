#include <iostream>
#include <vector>
#include <algorithm>
#include <string>

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

int calculateDays(int x1, int y1, int x2, int y2) {
    return ((x1 - x2) / (y2 - y1)) + 1;
}

int main() {
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int x1, y1, x2, y2;
    cin >> x1 >> y1 >> x2 >> y2;

    if(x1 > x2) cout << 0 << "\n";
    else if(x2 >= x1 && y2 >= y1) cout << -1 << "\n";
    else cout << calculateDays(x1, y1, x2, y2) << "\n";

    return 0;
}