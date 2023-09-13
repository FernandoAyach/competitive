#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <string>
#include <sstream>
#include <set>

using namespace std;

#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second

const int INF = 1000000007;
const int MAX = 2e5+7;

typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef pair<int, int> pii;

bool isAlmostPrime(int n) {
    int f = 0, aux = n;

    for(int i = 2; i * i <= n; i++) {
        if(aux % i == 0) {
            f++;
            while(aux % i == 0) aux /= i;
        }
    }

    if(aux > 1) f++;

    return f == 2;
}

int64_t solve() {
    int n, a = 0; cin >> n;

    FOR(i, 1, n + 1) {
        if(isAlmostPrime(i)) {
            a++;
        }
    }
    return a;
}

int main() {
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    cout << solve() << "\n";

    return 0;
}