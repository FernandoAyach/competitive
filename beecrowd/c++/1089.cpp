#include <iostream>
#include <vector>

using namespace std;

bool isPeak(int m, int mp, int mn) {
    return m < mp && m < mn || (m > mp && m > mn); 
}
 
int main() {
    int n;
    cin >> n;
    while(n != 0) {
        vector<int> magnitudes(n);

        for(int i = 0; i < n; i++) {
            cin >> magnitudes[i];
        }

        int peaks = 0;
        for(int i = 0; i < n; i++) {
            if(isPeak(magnitudes[i], magnitudes[(i - 1 + n) % n], magnitudes[(i + 1) % n])) {
                peaks++;
            }
        }
        cout << peaks << endl;
        
        cin >> n;
    }
}