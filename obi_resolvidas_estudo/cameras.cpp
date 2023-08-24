#include <iostream>
#include <algorithm>

using namespace std;

//coluna i e linha j
//i - 1, j; i + 1, j; i, j - 1; i j + 1;
int n, m, k, bloq[40][40], mark[40][40];

void dfs(int i, int j) {
    mark[i][j] = 1;
    //Se a proxima posição estiver no mapa, não tiver sido marcada e não tiver sido bloqueada
    if(i - 1 >= 1 && i - 1 <= m && mark[i - 1][j] == 0 && bloq[i - 1][j] == 0) {
        // Vai até a posição
        dfs(i - 1, j);
    }
    if(i + 1 >= 1 && i + 1 <= m && mark[i + 1][j] == 0 && bloq[i + 1][j] == 0) {
        dfs(i + 1, j);
    }
    if(j - 1 >= 1 && j - 1 <= n && mark[i][j - 1] == 0 && bloq[i][j - 1] == 0) {
        dfs(i, j - 1); 
    }
    if(j + 1 >= 1 && j + 1 <= n && mark[i][j + 1] == 0 && bloq[i][j + 1] == 0) {
        dfs(i, j + 1);
    }
}

int main() {
   
    cin >> n >> m >> k;

    while(k--) {
        int c, l;
        char d;
        cin >> c >> l >> d;
        //Casos bloqueados
        if(d == 'S') {
            for(int i = l; i <= m; i++) {
                bloq[i][c] = 1;
            }
        } else if(d == 'N') {
            for(int i = 1; i <= l; i++) {
                bloq[i][c] = 1;
            }
        } else if(d == 'L') {
            for(int i = c; i <= n; i++) {
                bloq[l][i] = 1;
            }
        } else {
            for(int i = 1; i <= c; i++) {
                bloq[l][i] = 1;
            }
        }
    }

    if(bloq[1][1] == 1) {
        cout << "N\n";
        return 0;
    }

    dfs(1, 1);

    //mark[i][j] == 1, visitei a posição ij
    if(mark[n][m] == 1) cout << "S\n";
    else cout << "N\n";
}

/*
DFS - busca em grafos
Transforma uma grid em grafos
liga duas arestas se elas forem adjacentes
Nesse caso, não iremos ligar arestas que estão sendo observadas por camera
*/