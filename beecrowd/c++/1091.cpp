#include <iostream>

using namespace std;

int main() {

    int n, x0, y0;
    
    while(cin >> n) {
        cin >> x0 >> y0;
        while(n--) {
            int x, y;
            cin >> x >> y;

            if(x == x0 || y == y0) cout << "divisa" << endl;
            else if(x > x0 && y > y0) cout << "NE" << endl;
            else if(x > x0 && y < y0) cout << "SE" << endl;
            else if(x < x0 && y < y0) cout << "SO" << endl;
            else cout << "NO" << endl;
        }
    }
}