#include <iostream>
#include <vector>
#include <stack>
#include <string>

using namespace std;

#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
#define PB push_back
#define F first
#define S second

typedef long long ll;
typedef unsigned long long llu;
typedef vector<int> vi;
typedef pair<int, int> pii;

void setup() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);
}

bool matches(char open, char close) {
    return open == '(' && close == ')' || 
        open == '{' && close == '}' ||
        open == '[' && close == ']';
}

bool valid(string s) {
    stack<char> stk;
    
    FOR(i, 0, s.length()) {
        if(s[i] == '(' || s[i] == '{' || s[i] == '[') {
            stk.push(s[i]);
        } else {
            if(stk.empty()) return false;

            if(matches(stk.top(), s[i])) stk.pop();
            else return false;  
        }
    }

    return stk.empty();
}

int main() {
    setup();
    
    string s;
    getline(cin, s);

    if(valid(s)) cout << "Valido\n";
    else cout << "Nao valido\n";
}