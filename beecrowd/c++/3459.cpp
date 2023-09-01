#include <iostream>
#include <vector>
#include <algorithm>
#include <cstdint>
#include <iomanip>
#include <string>
#include <sstream>

using namespace std;

#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second

#define INF 1000000007
#define MAX 1007
#define SIZE 30

typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef pair<int, int> pii;

inline bool isDigitWithWord(string s, int i, int n) {
    return isdigit(s[i]) && (
        (i >= 1 && isalpha(s[i - 1])) || 
        (i < n - 1 && isalpha(s[i + 1]))
    );
}

inline bool isDelimitador(char c) {
    return c == ' ' || c == '.' || c == ',';
} 

inline bool isDelimitadorBetweenNumbers(string s, int i, int n) {
    return isDelimitador(s[i]) && (
        (i >= 1 && isdigit(s[i - 1])) && 
        (i < n - 1 && isdigit(s[i + 1]))
    );
} 

int toNumber(string s) {
    int ans = 0;
    for(auto& c : s) {
        if(c != '*') {
            ans = ans * 10 + (c - '0');
        }
    }
    return ans;
}

int isNumber(string s) {
    for(auto& c : s) {
        if(c - '0' < 0 || c - '0' > 9) return false;
    }
    return true;
}

int64_t solve() {
    int n, size = 0; cin >> n;
    string s;
    
    FOR(i, 0, n + 1) {
        string line;
        getline(cin, line);

        s += line  + " \n"[i == n];
    }

    size = s.size();

    FOR(i, 0, size) {
        if(isDigitWithWord(s, i, size)) {
            s[i] = 'a';
        } 
    }

    FOR(i, 0, size) {
        if(isDelimitadorBetweenNumbers(s, i, size)) {
            s[i] = '*';
        }
    }

    FOR(i, 0, size) {
        if(isDelimitador(s[i])) {
            s[i] = ' ';
        }
    }
    vi ans(MAX);
    int c = 0;

    stringstream iss(s);
    string word;
    while(iss >> word) {
        if(word.find('*') != std::string::npos || isNumber(word)) {
            ans[c] = toNumber(word);
            c++;
        }
    }
    
    bool found = false;
    
    for(int i = 0; i < c - 1; i++) {
        if(found) break;

        int y = 0;
        int current = ans[i];
        for(int j = 0; j < c; j++) {
            if(ans[j] == current + 1) {
                y++;
                current = ans[j];
            }

            if(y == 2) {
                found = true;
                break;
            }
        }
    }

    cout << (found ? "123" : ":)") << "\n";

    return 0;
}

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    solve();
    
    return 0;
}