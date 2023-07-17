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

llu factorial(int n)
{

    if (n == 0)
        return 1;

    llu result = n;
    FOR(i, n)
    {
        result *= i;
    }
    return result;
}

int main()
{
    ios::sync_with_stdio(0);
    cin.tie(0);

    int m, n;
    while (cin >> m >> n)
    {
        cout << factorial(m) + factorial(n) << "\n";
    }
    return 0;
}