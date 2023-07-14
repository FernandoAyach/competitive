#include <iostream>

using namespace std;
 
int main() {
    int n;
    while(cin >> n && n != 0) {
        
        for(int i = 1; i * i <= n; i++) {
            cout << i * i;
            if ((i + 1) * (i + 1) <= n) cout << " ";
        }
        cout << endl;
    }
 
    return 0;
}