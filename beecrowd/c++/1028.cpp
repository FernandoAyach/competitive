#include <iostream>

using namespace std;

int mdc(int f1, int f2) {
    while(f1 % f2 != 0) {
        int aux = f2;
        f2 = f1 % f2;
        f1 = aux;
    }
    return f2;
}

int main() {
    int n, f1, f2;
    cin >> n;
    while(n--) {
        cin >> f1 >> f2;
        cout << mdc(f1, f2) << endl;
    }
}