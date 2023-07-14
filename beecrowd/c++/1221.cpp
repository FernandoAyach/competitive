#include <iostream>

using namespace std;

bool isPrime(unsigned int number) {

    for(int i = 2; i * i <= number; i++) {
        if(number % i == 0) return false;
    }
    return true;
}

int main() {
    int n;
    cin >> n;
    
    unsigned int number;

    while(n--) {
        cin >> number;

        if(isPrime(number)) cout << "Prime" << endl;
        else cout << "Not Prime" << endl;
    }
}