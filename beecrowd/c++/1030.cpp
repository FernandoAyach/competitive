#include <iostream>
#include <vector>
 
using namespace std;
 
int josephus(int n, int k) {
    if(n == 1) return n;

    return (josephus(n - 1, k) + k - 1) % n + 1;
}

int main() {
    int n, m, j, c, alive, i;
    cin >> n;
    
    c = 1;
    while(n--) {
        cin >> m >> j;
        /*
        i = 1;
        alive = 1;
        while(i <= m) {
            alive = (alive + j) % i;
            i++;
        }
        */

        //cout << "Case " << c << ": " << alive + 1 << endl;
        cout << "Case " << c << ": " << josephus(m, j) << endl;
        c++;
    }
 
    return 0;
}