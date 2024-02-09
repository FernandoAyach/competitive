#include <iostream>

bool verificarIntervalo(double nota, double inicio, double fim) {
    return (nota > inicio && nota < fim);
}

int main() {
    long long N;
    std::cin >> N;

    for (long long i = 0; i < N; ++i) {
        double nota, inicio, fim;
        std::cin >> nota >> inicio >> fim;

        bool resultado = verificarIntervalo(nota, inicio, fim);

        std::cout << (resultado ? "True" : "False") << std::endl;
    }

    return 0;
}