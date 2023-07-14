# -*- coding: utf-8 -*-

'''
Entrada
 (1) Coleta os valores da portas, na mesma linha, separado por espaços, a partir do input().split() e
 atribui para as variáveis p e r;

Desenvolvimento + Saída:
 (1) Se p estiver para a esquerda, a bolinha irá para C. Imprime C na tela.
 (2) Caso contrário, irá para B ou A.
 (3) Se r estiver para a esquerda, irá para B. Imprime B na tela.
 (4) Caso contrário, irá para A. Imprime A na tela.
'''

# Coleta os valores das portas na mesma linha, separado por espaços
p, r = input().split() 

# Se p estiver para esquerda
if p == '0':
    # Entra em C, imprime na tela
    print('C')
# Senão entra em A ou B
else:
    # Se r estiver para esquerda
    if r == '0':
        # Entra em b, imprime na tela
        print('B')
    # Senão
    else:
        # Entra em a, imprime na tela
        print('A')