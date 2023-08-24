#include <iostream>
#include <algorithm>

using namespace std;

int sumDigits(int n) {
    int sum = 0;

    while(n >= 1) { //log10 n
        sum += n % 10;
        n /= 10;
    }
    return sum;
}

int main() {
    int s, a, b, c = 0;
    cin >> s >> a >> b;

    for(int i = a; i <= b; i++) {
        if(sumDigits(i) == s) c++;
    }
    cout << c << "\n";
}