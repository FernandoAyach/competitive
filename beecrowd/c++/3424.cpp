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

void countAs(int n, string s) {
    int ans = 0, count;

    FOR(i, 0, n) {
        count = 0;
        while(s[i] == 'a') {
            count++;
            i++;
        }
        ans += count >= 2 ? count : 0;
    }
    cout << ans << "\n";
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; cin >> n;
    string s; cin >> s;

    countAs(n, s);
    
    return 0;
}