#include <iostream>
#include <vector>

using namespace std;

#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second

typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef pair<int, int> pii;

int sumAlgarisms(int number) {
    int sum = 0;
    while(number != 0) {
        sum += number % 10;
        number /= 10;
    }
    return sum;
}

int main() {
    //freopen("input.txt", "r", stdin);
    //freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int s, a, b, min, max;
    cin >> s >> a >> b;

    for(int i = a; i <= b; i++) {
        if(sumAlgarisms(i) == s) {
            min = i;
            break;
        }
    }

    for(int i = b; i >= a; i--) {
        if(sumAlgarisms(i) == s) {
            max = i;
            break;
        }
    }

    cout << min << "\n"; 
    cout << max << "\n"; 


    return 0;
}