#include <iostream>
#include <string>
#include <algorithm>
#include <vector>

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

bool isPoligram(string poligram, int length, int n) {
    string root = poligram.substr(0, length);
    sort(root.begin(), root.end());

    for(int i = length; i + length <= n; i += length) {
        string compare = poligram.substr(i, length);
        sort(compare.begin(), compare.end());

        if(root != compare) return false;
    }
    return true;
}

int main() {
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n;
    cin >> n;
    cin.ignore();

    string poligram;
    getline(cin, poligram);

    for(int i = 1; i + i <= n; i++) { // Tamanho da substring
        if(n % i != 0) continue;

        if(isPoligram(poligram, i, n)) {
            cout << poligram.substr(0, i);
            return 0;
        }
    }
    
    cout << "*\n";
    return 0;
}