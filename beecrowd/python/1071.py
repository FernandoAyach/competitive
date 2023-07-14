# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Coleta o primeiro número, em uma linha, converte em inteiro, pelo int() e atribui
 para a variável n1.
 (2) Coleta o segundo número, em uma linha, converte em inteiro, pelo int() e atribui
 para a variável n2.
 (3) Para facilitar o uso do loop posteriormente, iremos priorizar o menor valor em n1, portanto,
 caso n2 for menor que n1, troca as variáveis.
 (4) Se n1 for par, obtem o próximo impar somando 1 ao seu valor.
 (5) Senão, for impar, obtem o próximo impar somando 2 ao seu valor.
 (6) Inicia variável de soma 'total'
 (7) Inicia um loop for de intervalo [n1, n2), de passo 2. Em cada repetição:
     (8) Incrementa o valor de i, já é impar, por conta do passo, à variável total.
 (9) Imprime o total na tela
'''

n1 = int(input())  # Coleta o primeiro número inteiro
n2 = int(input())  # Coleta o segundo número inteiro

if n2 < n1:  # Se n2 for maior que n1
    aux = n1  # Armazena valor de n1 em aux
    n1 = n2  # Atribui o valor de n2 para n1
    n2 = aux  # Atribui o valor de aux para n2

if n1 % 2 == 0:  # Se n1 for par
    n1 += 1  # Pega o próximo impar
else:  # Se for impar
    n1 += 2  # Pega o próximo impar

total = 0  # Inicia variável de soma

for i in range(n1, n2, 2):  # Percorre o intervalo [n1, n2) em 2 em 2
    total += i  # Soma i ao total
    
print(total)  # Imprime resultado na tela