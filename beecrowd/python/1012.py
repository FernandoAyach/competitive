# -*- coding: utf-8 -*-

'''
Coleta 3 valores e os converte em real.
Armazena um valor para o PI.
Calcula as áreas da figuras geométricas.
Imprime resultados na tela, com aproximação de 3 casas decimais.
'''

a, b, c = input().split()  # Coleta os 3 valores
a = float(a)  # Converte a em real
b = float(b)  # Converte b em real
c = float(c)  # Converte c em real
pi = 3.14159  # Armazena o valor do PI

triangleArea = a*c / 2  # Calcula a area do triangulo
circleArea = pi*c**2  # Calcula a area do circulo
trapezeArea = ((a + b)*c) / 2  # Calcula a area do trapezio
squareArea = b**2  # Calcula a area do quadrado
rectangleArea = a*b  # Calcula a area do retangulo

print('TRIANGULO: {:.3f}'.format(triangleArea))  # Imprime resultado da area do triangulo na tela, com 3 casas decimais
print('CIRCULO: {:.3f}'.format(circleArea))  # Imprime resultado da area do circulo na tela, com 3 casas decimais
print('TRAPEZIO: {:.3f}'.format(trapezeArea))  # Imprime resultado da area do trapezio na tela, com 3 casas decimais
print('QUADRADO: {:.3f}'.format(squareArea))  # Imprime resultado da area do quadradona tela, com 3 casas decimais
print('RETANGULO: {:.3f}'.format(rectangleArea))  # Imprime resultado da area do retangulo na tela, com 3 casas decimais