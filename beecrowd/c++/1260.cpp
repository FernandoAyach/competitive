#include <iostream>
#include <string>
#include <map>
#include <iomanip>

using namespace std;

int main() {
    int n;
    cin >> n;
    cin.ignore();

    string name;
    getline(cin, name);

    while(n--) {
        map<string, int> trees;
        double total = 0;

        while(getline(cin, name) && !name.empty()) {
            trees[name]++;
            total++;
        }

        cout << setprecision(4) << fixed;
        for(auto& t : trees) {
            double percentage = t.second / total;
            cout << t.first << " " << percentage * 100.0 << endl;
        }
        
        if(n) cout << endl;
    }
}