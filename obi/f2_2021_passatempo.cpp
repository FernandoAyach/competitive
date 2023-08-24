#include <iostream>
#include <algorithm>
#include <string>
#include <map>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, m;
    cin >> n >> m;

    string grid[100][100];
    map<string, int> variables;
    int sLine[100];
    int sCol[100];

    for(int i = 0; i <= n; i++) {
        if(i < n) {
            for(int j = 0; j <= m; j++) {
                if(j < m) {
                    cin >> grid[i][j];
                    variables[grid[i][j]] = INT_MIN;
                } else {
                    cin >> sLine[i];
                }
            }
        } else {
            for(int j = 0; j < m; j++) {
                cin >> sCol[j];  
            }
        }
    }

    for(int i = 0; i < n; i++) {
        for(int j = 0; j < m; j++) {
                
        }  
    }

    for(int j = 0; j < m; j++) {
        for(int i = 0; i < n; i++) {
          
        }
    }
    
    


    return 0;
}