#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
    int n, m, k, p, i;
    string s;
    string poss[500];

    cin >> n >> m >> k;
    cin >> s;

    for(int i = 0; i < m; i++) {
        cin >> poss[i];
        sort(poss[i].begin(), poss[i].end());
    }
    cin >> p;
    p--;

    int j = m - 1;
    for(int i = n - 1; i >= 0; i--) {
        if(s[i] == '#') {
            s[i] = poss[j][p % k];
            p = p / k;
            j--;
        }
    }
    cout << s << "\n";
}