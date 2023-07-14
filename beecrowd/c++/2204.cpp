#include <iostream>
#include <string>

using namespace std;

int main() {
    int n;
    string f1, f2;
    cin >> n;
   
    while(n--) {
        cin >> f1 >> f2;

        if(f1 != f2) cout << 1 << endl;
        else cout << f1 << endl;
    }
}