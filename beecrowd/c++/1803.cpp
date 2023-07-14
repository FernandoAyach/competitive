#include <iostream>
#include <array>
#include <sstream>

using namespace std;

int main() {
    array<string, 4> matring;
    stringstream f, l, word;
    string row;

    for(int i = 0; i < 4; i++) {
        cin >> matring[i];
        row = matring[i];
        f << row[0];
        l << row[row.size() - 1];
    }

    int fInt, lInt, number, code;
    fInt = stoi(f.str());
    lInt = stoi(l.str());    

    for(int j = 1; j < row.size() - 1; j++) {
        stringstream letter;
        for(int i = 0; i < 4; i++) {
            letter << matring[i][j];
        }
         
        number = stoi(letter.str());
        code = (fInt * number + lInt) % 257;
        word << (char) code;
    }
    cout << word.str() << endl;
}