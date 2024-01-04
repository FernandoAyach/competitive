#include <iostream>
#include <algorithm>

using namespace std;

int printElement(int n, int i, int j) {
    int l, u, d, r;
    d = n - i;
    u = i + 1;
    l = j + 1;
    r = n - j;

    return min({d, u, l, r});
}

int main() {
    int n;
    cin >> n;

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < n; j++) {
            cout << printElement(n, i, j) << " ";
        } 
        cout << "\n";
    }
}