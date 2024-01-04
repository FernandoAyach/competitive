#include <iostream>
#include <vector>
#include <algorithm>

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
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    vector<int> levels;
    levels.reserve(4);
    
    FOR(i, 0, 4) {
        int level;
        cin >> level;
        levels.emplace_back(level);
    }
    
    int t1, t2 = 0;
    t1 = levels[3] + levels[0];
    t2 = levels[1] + levels[2];

    cout << abs(t1 - t2) << "\n";
    return 0;
}