#include <iostream>
#include <string>
#include <sstream>

using namespace std;

int main() {

    int n; 
    cin >> n;

    stringstream newWord;
    for(int i = 0; i < n; i++) {
        string encrypted; 
        cin >> encrypted;

        int offset; 
        cin >> offset;
        
        newWord.str("");
        for(char& c : encrypted) {
            int rest = ((int)c - offset - 65 + 26) % 26;
            char newChar = rest + 65;
            newWord << newChar;
        }
        cout << newWord.str() << endl;
    }
}