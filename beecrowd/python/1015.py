# -*- coding: utf-8 -*-

'''
Entrada:
- Coleta x1 e y1, na mesma linha, separado por espaços, a partir do
input().split().
- Converte x1 para número real e atualiza a variável.
- Converte y1 para número real e atualiza a variável.
- Repete todo o processo acima para x2 e y2.

Desenvolvimento:
- Cálcula a distância de dois pontos conforme a fórmula.

Saída:
- Imprime a distância na tela, com quatro casas decimais de aproximação
'''

x1, y1 = input().split()  # Coleta x1 e y1, na mesma linha, separado por espaços
x1 = float(x1)  # Converte x1 para real
y1 = float(y1)  # Converte y1 para real

x2, y2 = input().split()  # Coleta x2 e y2, na mesma linha, separado por espaços
x2 = float(x2)  # Converte x2 para real
y2 = float(y2)  # Converte y2 para real

distance = ((x2 - x1)**2 + (y2 - y1)**2) ** 0.5  # Calcula a distancia de dois pontos

print('{:.4f}'.format(distance))  # Imprime o resultado com 4 casas decimais