#include <iostream>
#include <vector>
using namespace std;

void sieveOfEratosthenes(int A, int B) {
    vector<bool> isPrime(B + 1, true);
    isPrime[0] = isPrime[1] = false;

    for (int i = 2; i * i <= B; ++i) {
        if (isPrime[i]) {
            for (int j = i * i; j <= B; j += i) {
                isPrime[j] = false;
            }
        }
    }

    for (int i = max(2, A); i <= B; ++i) {
        if (isPrime[i]) {
            cout << i << " ";
        }
    }
    cout << endl;
}

int main() {
    int A, B;
    cin >> A >> B;
    sieveOfEratosthenes(A, B);
    return 0;
}