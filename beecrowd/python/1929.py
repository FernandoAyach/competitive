# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta os 4 valores, na mesma linha, separados por espaços, pelo input().split() e atribui
 para as variáveis n1, n2, n3 e n4.
 (2) Converte cada uma para inteiro e atualiza a variável respectiva.

Desenvolvimento + Saída:
 (1) Com a disposição de 4 valores, é possível formar os seguintes triângulos:
 Triângulo n1 n2 n3
 Triângulo n1 n3 n4
 Triângulo n2 n3 n4
 Triângulo n1 n2 n4
 Se, em um desses casos, a soma de 2 lados sempre for maior que o valor do terceiro,
 pode haver formação de triângulo.
 (2) Imprime S na tela.
 (3) Caso contrário, não pode have formação.
 (4) Imprime N na tela.
'''

# Coleta os 4 valores, na mesma linha, separados por espaços
n1, n2, n3, n4 = input().split()

# Converte o primeiro valor para inteiro
n1 = int(n1)

# Converte o segundo valor para inteiro
n2 = int(n2)

# Converte o terceiro valor para inteiro
n3 = int(n3)

# Converte o quarto valor para inteiro
n4 = int(n4)

# Dados os seguintes triângulos, se um deles tiver que a soma de dois lados sempre
# é maior que o terceiro, pode haver formação de triângulo

if (n1 < n2 + n3 and n2 < n1 + n3 and n3 < n2 + n1) or \
(n1 < n3 + n4 and n3 < n1 + n4 and n4 < n1 + n3) or \
(n2 < n3 + n4 and n3 < n2 + n4 and n4 < n2 + n3) or \
(n1 < n2 + n4 and n2 < n1 + n4 and n4 < n1 + n2):
    print('S')  # Mostra que é possível haver triângulo
else:  # Caso contrário
    print('N')  # Mostra que não é possível haver triângulo