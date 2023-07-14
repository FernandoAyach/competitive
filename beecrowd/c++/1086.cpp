#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
    unsigned int L, C, l, n;

    while((cin >> L >> C) && L != 0 && C != 0) {
        cin >> l >> n;
        C *= 100;
        L *= 100;

        vector<int> tables;

        for(int i = 0; i < n; i++) {
            int table;
            cin >> table;
            tables.push_back(table * 100);
        }
        sort(tables.begin(), tables.end());

        unsigned int left, right, v, h, aV, aH;
        v = 0;
        h = 0;
        aV = 0;
        aH = 0;
        left = 0;
        right = n - 1;
        
        while(aV < L * C) {

            if(left == right || right < 0) {
                break;
            }

            if(tables[right] == C) {
                aV += tables[right] * l;
                v++;
                right--;
            } else if(tables[right] + tables[left] == C) {
                aV += (tables[right] + tables[left]) * l;
                v += 2;
                right--;
                left++;
            } else {
                right--;
            }
        }

        left = 0;
        right = n - 1;

        while(aH < C * L) {

            if(left == right || right < 0) {
                break;
            }

            if(tables[right] == L) {
                aH += tables[right] * l;
                h++;
                right--;
            } else if(tables[right] + tables[left] == L) {
                aH += (tables[right] + tables[left]) * l;
                h += 2;
                right--;
                left++;
            } else {
                right--;
            }
        }

        bool impossible = (h == 0 && v == 0) || ((aV < L * C) && (aH < L * C));

        if(impossible) {
            cout << "impossivel" << endl;
        } else if(h < v && !(h < L * C)) {
            cout << h << endl;
        } else {
            cout << v << endl;
        }
    }
}