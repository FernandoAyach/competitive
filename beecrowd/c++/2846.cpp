#include <iostream>

using namespace std;

int main() {
    int n;
    cin >> n;

    int fibonots = 0;
    int previous = 3;
    int current = 5;
    int next = 0;
    while(true) {

        for(int i = previous + 1; i < current; i++) {
            fibonots++;

            if(fibonots == n) {
                cout << i << endl;
                return 0;
            }
        }
    
        next = previous + current;
        previous = current;
        current = next;
    }
}