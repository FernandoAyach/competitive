# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Le o número de casos de teste, converte em inteiro, pelo int() e atribui para n.
 (2) Inicia um contador para o número de casos cases, com valor inicial 1.
 (3) Cria um loop for de intervalo [0, n). A cada repetição:
     (4) Le as idades, na mesma linha, separadas por espaço, pelo input().split() e atribui para ages.
     (5) Obtem o números de membros da equipe a partir da indexação ages[0], converte para inteiro e atribui
     para members_number.
     (6) Calcula a posição da mediana das idades (soma 1 por conta do vetor começar em 0) e atribui para captain_position.
     (7) Imprime a idade do capitão pela indexação ages[captain_position]. Além disso, nessa mesma impressão, insere o número
     de caso respectivo cases.
     (8) Incrementa cases em 1 e atualiza a variável.
'''

n = int(input())  # Coleta o número de casos de teste

cases = 1  # Contador de casos

for i in range(n):  # Cria um loop que repete n vezes
    ages = input().split()  # Coleta as idades, na mesma linha, separadas por espaços

    members_number = int(ages[0])  # Le o número de membros do time

    captain_position = (members_number // 2) + 1  # Calcula a posição da mediana das idades
    print('Case {}: {}'.format(cases, ages[captain_position]))  # Imprime na tela a idade do capitão, com o contador de casos
    cases += 1  # Incrementa para o próximo caso
