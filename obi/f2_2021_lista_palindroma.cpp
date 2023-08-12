#include <iostream>
#include <vector>

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

/*
Ideia:
Iremos utilizar a estratégia gulosa - consideraremos que sempre podemos ignorar o valores
iguais e seguir em frente, sabendo que, em algum momento, vai dar palindromo se somar os valores 
de fora para dentro, considerando que vale a pena somar sempre o menor com algo para encontrar o maior.

Algoritmo:
Haverão 2 ponteiros, na esquerda e na direita.
Se os ponteiros foram iguais, passa para frente.
Se forem diferentes, verifica o menor e soma com o da "frente".
*/

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    ios::sync_with_stdio(0);
    cin.tie(0);

    int n, value, left, right, counter, sl, sr;
    cin >> n;

    vector<int> list;

    FOR(i, 0, n) {
        cin >> value;
        list.PB(value);
    }

    left = 0;
    right = n - 1;
    counter = 0;

    // Ao inves de criar uma lista nova, vamos trabalhar com 2 variáveis que simulam isso
    // Conforme formos avançando na lista, vamos somando os valores nas variáveis
    // Isso funciona pois sempre vamos pra frente e podemos ignorar o que já passou,
    // pois estamos usando o Algoritmo guloso
    sl = list[left];
    sr = list[right];

    while(left <= right) { // Repete até os ponteiros se inverterem
        if(sl == sr) {  // Se forem iguais
            // Atualiza os ponteiros e os valores
            left++;  
            right--;
            sl = list[left];
            sr = list[right];
        } else if(sl < sr) {  // Se o da esquerda é menor
            left++;  // Atualiza o ponteiro da esquerda
            sl += list[left];  // Atualiza o valor somando com o próximo
            counter++;
            if(left == right) break;  // Se os ponteiros se encontraram, para o loop
        } else {  // Se o da direita é menor
            right--;  // Atualiza o ponteiro da direita
            sr += list[right];  // Atualiza o valor somando com o próximo
            counter++;
            if(left == right) break;  // Se os ponteiros se encontraram, para o loop
        }
    }
    cout << counter << "\n";

    return 0;
}