#include <iostream>
#include <sstream>
#include <cmath>

using namespace std;

string getBinaryLE(unsigned int decimal) {
    stringstream binary;

    while(decimal != 0) { 
        binary << decimal % 2;
        decimal /= 2;
    }
    
    return binary.str();
}

string wrongSum(string& b1, string& b2) {
    stringstream resultLE;

    if(b1.size() > b2.size()) b1.swap(b2);
       
    for(int i = 0; i < b1.size(); i++) {
        if(b1[i] == '0' && b2[i] == '1' || b1[i] == '1' && b2[i] == '0') {
            resultLE << '1';
        } else {
            resultLE << '0';
        }
    }

    for(int i = b1.size(); i < b2.size(); i++) resultLE << b2[i];

    return resultLE.str();
}

unsigned int getDecimal(string& bSum) {
    unsigned int result = 0;

    for(int i = 0; i < bSum.size(); i++) {
        result += (bSum[i] - '0') * (pow(2, i));
    }
    return result;
}

int main() {
    unsigned int d1, d2;

    while(cin >> d1 >> d2) {
        string b1, b2;
        b1 = getBinaryLE(d1);
        b2 = getBinaryLE(d2);

        string bSum = wrongSum(b1, b2);
        unsigned int dSum = getDecimal(bSum);
        
        cout << dSum << endl;
    }
}