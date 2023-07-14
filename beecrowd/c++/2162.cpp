#include <iostream>
#include <vector>

using namespace std;

bool verifyPattern(int n, const vector<int>& heights, bool oddPattern) {
    for (int i = 1; i < n - 1; i++) {
        if ((oddPattern && i % 2 == 0) || (!oddPattern && i % 2 != 0)) {
            if (heights[i] >= heights[i - 1] || heights[i] >= heights[i + 1]) {
                return false;
            }
        } else {
            if (heights[i] <= heights[i - 1] || heights[i] <= heights[i + 1]) {
                return false;
            }
        }
    }
    return true;
}

int main() {
    int n;
    cin >> n;

    vector<int> heights(n);

    for (int i = 0; i < n; i++) {
        cin >> heights[i];
    }

    if (heights[0] > heights[1]) {
        bool isValid = verifyPattern(n, heights, false);
        cout << (isValid ? 1 : 0) << endl;
    } else if (heights[0] < heights[1]) {
        bool isValid = verifyPattern(n, heights, true);
        cout << (isValid ? 1 : 0) << endl;
    } else {
        cout << 0 << endl;
    }

    return 0;
}
