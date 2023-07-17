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
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n; 
    cin >> n;
    while(n--) {
        int c;
        cin >> c;
        llu kgs = (pow(2, c) / 12) / 1000;
        cout << kgs << " kg\n";
    }

    return 0;
}