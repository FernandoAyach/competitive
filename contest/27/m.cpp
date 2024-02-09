#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    int n;
    cin >> n;

    vector<string> nomes; 

    for (int i = 0; i < n; i++) {
        string nome;
        cin >> nome;
        nomes.push_back(nome);
    }

    sort(nomes.begin(), nomes.end());

    for (const string& nome : nomes) {
        cout << nome << endl;
    }

    return 0;
}