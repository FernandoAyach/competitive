#include <iostream>
#include <array>

using namespace std;

void On3solution() {
    cout << "O(n3)solution \n";

    array<int, 8> array = {-1, 2, 4, -3, 5, 2, -5, 2};
    int n = 8;
    int best = 0;

    for (int a = 0; a < n; a++) {  // ponto de inicio
        for (int b = a; b < n; b++) {  // a partir do ponto de inicio ate o final
            int sum = 0;
            for (int k = a; k <= b; k++) { // Limite (permite arrays menores que n)
                sum += array[k];
            }
            best = max(best,sum);
        }
    }
    cout << best << "\n\n";
}

void On2solution() {
    cout << "O(n2)solution \n";
    array<int, 8> array = {-1, 2, 4, -3, 5, 2, -5, 2};
    int n = 8;
    int best = 0;

    for (int a = 0; a < n; a++) {  // Ponto de partida
        int sum = 0;
        for (int b = a; b < n; b++) {  // A partir do ponto de partida até n
            sum += array[b]; // Simula o limite do loop, a cada soma é como se fosse k++
            best = max(best,sum);
        }
    }
    cout << best << "\n\n";
}

void Onsolution() {

    //Kadane's algorithm
    
    cout << "O(n)solution \n";

    array<int, 8> array = {-1, -4, -4, -3, -5, -2, -5, -2};
    int n = 8;
    int best = INT_MIN, sum = 0;

    for (int k = 0; k < n; k++) { // Percorre o loop
        // O código abaixo verifica, elemento por elemento
        // Se vale a pena iniciar a soma com o número atual (array),
        // Caso for maior que a soma até então
        // Ou continuar somando o número na soma atual, que é a maior.
        sum = max(array[k], sum + array[k]);
        best = max(best, sum);  // No final, verifica a melhor soma.
    }
    cout << best << "\n\n";
}

int main() {
   On3solution();
   On2solution();
   Onsolution();
}
