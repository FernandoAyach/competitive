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

int getNumberOfFactors(ll n) {
    int t = 0;

    for(ll i = 2; i * i <= n; i++) {
        if(n % i == 0) {
            t++;
            while(n % i == 0) {
                n /= i;
            }
        }
    }

    if(n > 1) t++;
    return t;
}

int getNumberOfDespojados(int n) {
    return ((1ll << n) - n - 1);
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    ll x, n; cin >> x;
    
    n = getNumberOfFactors(x);

    cout << getNumberOfDespojados(n) << "\n";

    return 0;
}