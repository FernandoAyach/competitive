# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta 4 valores na mesma linha, separado por espaços, pelo input().split() e
 atribui para as variáveis p1, c1, p2 e c2.
 (2) Converte cada variável para inteiro, pelo int(), e atualiza a respectiva variável.

Desenvolvimento + Saída:
 (1) Se o produto de p1 e c1 for igual ao produto de p2 e c2, está equilibrada. Imprime 0 na tela.
 (2) Se o produto de p1 e c1 for maior ao produto de p2 e c2, está tendendo para esquerda. Imprime -1 na tela.
 (3) Senão, está tendendo para direita. Imprime 1 na tela.
'''
# Coleta 4 valores na mesma linha, separado por espaços
p1, c1, p2, c2 = input().split() 
p1 = int(p1)  # Converte p1 em inteiro
c1 = int(c1)  # Converte c1 em inteiro
p2 = int(p2)  # Converte p2 em inteiro
c2 = int(c2)  # Converte c2 em inteiro

# Se a balança estiver equilibrada
if p1*c1 == p2*c2:
    # Imprime 0
    print(0)
# Se estiver tendendo para esquerda
elif p1*c1 > p2*c2:
    # Imprime -1
    print(-1)
# Senão
else:
    # Imprime 1
    print(1)