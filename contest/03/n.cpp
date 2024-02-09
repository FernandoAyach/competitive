#include <iostream>
#include <cmath>
#include <iomanip>
using namespace std;

double calcularDistancia(double x1, double y1, double x2, double y2) {
    double deltaX = x2 - x1;
    double deltaY = y2 - y1;
    return sqrt(deltaX * deltaX + deltaY * deltaY);
}

int main() {
    double x1, y1, x2, y2;
    
    cin >> x1 >> y1 >> x2 >> y2;
    double distancia = calcularDistancia(x1, y1, x2, y2);
    cout << fixed << setprecision(3) << distancia << endl;

    return 0;
}