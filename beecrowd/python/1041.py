# -*- coding: utf-8 -*-

'''
Coleta 2 valores reais na mesma linha, separados por espaços.
Identifica o quadrante respectivo dos pontos:
Se x e y forem positivos, são do primeiro quadrante. Imprime na tela.
Se x é negativo e y positivo, são do segundo quadrante. Imprime na tela.
Se x e y forem negativos, são do terceiro quadrante. Imprime na tela.
Se x for positivo e y negativo, são do quarto quadrante. Imprime na tela.
Se x for 0 e y for diferente de 0, está no eixo y. Imprime na tela.
Se x for diferente de 0 e y for 0, está no eixo x. Imprime na tela.
Se não for nenhum dos casos acima, está na origem. Imprime na tela.
'''

x, y = input().split()  # Coleta a entrada completa e separa por espaços
x = float(x)  # Coleta o valor de x, converte em real
y = float(y)  # Coleta o valor de y, converte em real

if(x > 0 and y > 0):  # Verifica se é do primeiro quadrante
    print('Q1')  # É do primeiro quadrante, imprime na tela
elif(x < 0 and y > 0):  # Verifica se é do segundo quadrante
    print('Q2')  # É do segundo quadrante, imprime na tela
elif(x < 0 and y < 0):  # Verifica se é do teceiro quadrante
    print('Q3')  # É do primeiro teceiro, imprime na tela
elif(x > 0 and y < 0):  # Verifica se é do quarto quadrante
    print('Q4')  # É do quarto quadrante, imprime na tela
elif(x == 0 and y != 0):  # Verifica se é do eixo y
    print('Eixo Y')  # É do eixo y, imprime na tela
elif(x != 0 and y == 0):  # Verifica se é do eixo x
    print('Eixo X')  # É do eixo x, imprime na tela
else:  # Se não for os de cima, é da origem
    print('Origem')  # Imprime na tela