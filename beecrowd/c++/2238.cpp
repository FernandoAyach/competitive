#include <iostream>

using namespace std;

typedef unsigned long long llu;
 
int main() {
    const llu MAX = 9999999999999999;
    int divisor, notDivisor, multiple, notMultiple;
    cin >> divisor >> notDivisor >> multiple >> notMultiple;

    for(llu i = 1; i * i <= MAX; i++) {
        if(multiple % i == 0 && notMultiple % i != 0 &&
        i % divisor == 0 && i % notDivisor != 0 
        ) {
            cout << i << endl;
            return 0;
        }
    }

    cout << -1 << endl;
    return 0;
}