#include <bits/stdc++.h>
 
using namespace std;
 
#define FOR(i, w, n) for (int i = w; i < (int)n; i++)
#define all(x) x.begin(), x.end()
#define rall(x) x.rbegin(), x.rend()
 
typedef long long ll;
typedef unsigned long long llu;
typedef pair<int, int> pii;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<pii> vpi;

const ll INF = 1e9+7;
const ll MAX = 1e5+7;
 
void setup(){
	#ifndef ONLINE_JUDGE
	freopen("../input.txt","r",stdin); 
	freopen("../output.txt","w", stdout);  
	#endif
	ios::sync_with_stdio(false);
	cin.tie(0);
}

int n, m;

int seg[MAX * 4];
int base[MAX];

void build(int pos, int ini, int fim) {
    if(ini == fim) { // chegou num leaf node
        seg[pos] = base[ini]; // coloca o valor do vetor la
        return;
    }

    int m = (ini + fim) / 2; // qeubra no meio
    int e = 2 * pos + 1, d = 2 * pos + 2; // pega esquerda e direita
    build(e, ini, m); // constroi pra esquerda
    build(d, m + 1, fim); // constroi pra direita

    seg[pos] = min(seg[e], seg[d]); // insere o minimo do node
}

int query(int pos, int ini, int fim, int p, int q) {
    if(q < ini || p > fim) return INT_MAX;  // ini, fim totalmente fora de p, q
    if(p <= ini && fim <= q) return seg[pos]; // totalmente dentro

    // parcialmente dentro

    int m = (ini + fim) / 2; // quebra no meio
    int e = 2 * pos + 1, d = 2 * pos + 2; // pega direita e esquerda

    return min( // retorna o minimo do lado direito e do lado esquerdo
        query(e, ini, m, p, q), // minimo esquerdo
        query(d, m + 1, fim, p, q) // minimo direito
    );
}

void update(int pos, int ini, int fim, int id, int val) {
    if(id < ini || id > fim ) return; // id fora do intervalo
    if(ini == fim) { // achou
        seg[pos] = val; // atualiza
        return;
    }
    // está parcialmente contido

    int m = (ini + fim) / 2; // pega o meio
    int e = 2 * pos + 1, d = 2 * pos + 2; // pega as pos de esq e dir
    update(e, ini, m, id, val); // atualiza no lado esquerdo
    update(d, m + 1, fim, id, val); // atualiza no lado direito

    seg[pos] = min(seg[e], seg[d]); // atualiza o minimo atual
}

int64_t solve() {
    cin >> n >> m;

    for(int i = 0; i < n; i++) cin >> base[i];

    build(0, 0, n - 1);

    for(int i = 0; i < m; i++) {
        int o, a, b; cin >> o >> a >> b;

        if(o == 1) update(0, 0, n - 1, a, b);
        else cout << query(0, 0, n - 1, a, b - 1) << "\n";
    }

    return 0;
}
 
int main() {
	setup();
	solve();
	return 0;
}