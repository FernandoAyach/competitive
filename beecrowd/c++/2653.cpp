#include <iostream>
#include <string>
#include <set>

using namespace std;
 
int main() {
    
    string jewel;
    set<string> jewels;

    while(cin >> jewel) jewels.insert(jewel);
    
    cout << jewels.size() << endl;
 
    return 0;
}