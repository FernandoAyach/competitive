#include <iostream>
#include <algorithm>
using namespace std;

int calcularMDC(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int N;
    cin >> N;

    for (int i = 0; i < N; ++i) {
        int A, B;
        cin >> A >> B;

        if (A < B) {
            std::swap(A, B);
        }

        int mdc = calcularMDC(A, B);

        cout << mdc << endl;
    }

    return 0;
}