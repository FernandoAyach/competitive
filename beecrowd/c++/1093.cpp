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

int calculateDefeats(int ev, int d) {
    int defeats = 0;
    while(ev > 0) {
        ev -= d;
        defeats++;
    }
    return defeats;
}

double calculatePercentage(int d1, int d2, int at) {
    if(at == 3) {
        return (double)d1 / (double)(d1 + d2);
    } else {
        double v1WinRoundChance = (double)(at) / 6;
        double dice = (1 - v1WinRoundChance) / v1WinRoundChance;
        return (1.0 - pow(dice, d1))/(1.0 - pow(dice, d1+d2));
    }
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int ev1, ev2, at, d;
    while(cin >> ev1 >> ev2 >> at >> d && ev1 != 0) {
        int d1, d2;
        d1 = calculateDefeats(ev1, d);
        d2 = calculateDefeats(ev2, d);
        
        double percentage = calculatePercentage(d1, d2, at);
        cout << fixed << setprecision(1) << percentage * 100 << "\n";
    }

    return 0;
}