# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Importa o módulo math.
 (2) Define a função is_factorial_bigger.
 (3) Le o número de casos de teste, converte para inteiro e atribui para n.
 (4) Inicia uma lista winners com n posições iniciadas com "".
 (5) Inicia 2 variáveis, uma para contar as vitorias do lucas, lucas_wins, e outra
 para as do pedro, pedro_wins, ambas iniciando com 0.
 (6) Cria um for que repete n vezes. A cada repetição:
     (7) Le uma exponenciação, na mesma linha, separado por "^", pelo input().split("^"),
     e atribui para power.
     (8) Atualiza power com o valor real da exponenciação, em inteiro, int(power[0]) ** int(power[1]).
     (9) Le o fatorial, na mesma linha, separado por "!", pelo input().split("!") e atribui para factorial.
     (10) Atualiza factorial com o coeficientedo fatorial, em inteiro, int(factorial[0]).
     (11) Se is_factorial_bigger(power, factorial) é verdade, incrementa 1 em pedro_wins e armazena o vencedor
     winners[i] = "Pedro".
     (12) Senão, incrementa 1 em lucas_wins e armazena o vencedor winners[i] = "Lucas".
 (13) Se lucas_wins == pedro_wins, imprime "A competicao terminou empatada!"
 (14) Senão se, lucas_wins > pedro_wins, imprime "Campeao: Lucas!".
 (15) Senão, imprime "Campeao: Pedro!".
 (16) Cria um loop for que percorre a lista winners. A cada repetição:
     (17) Imprime "Rodada #{}: {} foi o vencedor".format(i + 1, winners[i])
'''

import math  # Importa o módulo math

def is_factorial_bigger(power, factorial):  # Define a função is_factorial_bigger
    
    """
        Função que retorna se um fatorial é maior que uma exponenciação ou não.
        power: número inteiro correspondente à exponenciação.
        factorial: coeficiente inteiro do fatorial.
        Retorna True quando o fatorial é maior e False se for menor.
    """
    
    if factorial >= 6:  # Se o coeficiente do fatorial for maior ou igual a 6
        if math.log(power) / math.log(factorial / 3) <= factorial:  # Se o fatorial é maior
            return True  # Retorna True
        elif math.log(power) / math.log(factorial / 2) >= factorial:  # Se a potencia é maior
            return False  # Caso contrario, retorna False
    
    result_factorial = factorial  # Variável para calcular o fatorial
    for i in range(2, factorial):  # Percorre de 2 até factorial - 1
        result_factorial *= i  # Multiplica i em result_factorial
    
    if result_factorial > power:  # Se o fatorial for maior que a potencia
        return True  # Retorna True
    return False  # Caso contrario, retorna False
    
n = int(input())  # Número de casos de teste

winners = [""]*n  # Lista de vencedores
lucas_wins = 0  # Rodadas ganhas pelo lucas
pedro_wins = 0  # Rodadas ganhas pelo pedro

for i in range(n):  # Repete n vezes
    
    # Le o número da exponenciação, na mesma linha, separado por "^"
    power = input().split("^")
    power = int(power[0]) ** int(power[1])   # Calcula a exponenciação
    
     # Le o número do fatorial, na mesma linha, separado por "!"
    factorial = input().split("!")
    factorial = int(factorial[0])  # Obtem e converte o número do fatorial em inteiro
    
    if is_factorial_bigger(power, factorial):  # Se o fatorial for maior
        pedro_wins += 1  # Adiciona uma vitoria para o pedro
        winners[i] = "Pedro"
    else:  # Senão
        lucas_wins += 1  # Adiciona uma vitoria para o lucas
        winners[i] = "Lucas"

if lucas_wins == pedro_wins:  # Se empatou
    print("A competicao terminou empatada!")  # Imprime que empatou
elif lucas_wins > pedro_wins:  # Senão, se o lucas ganhou
    print("Campeao: Lucas!")  # Imprime que o lucas ganhou
else:  # Senão
    print("Campeao: Pedro!")  # Imprime que o pedro ganhou

for i in range(len(winners)):  # Percorre os vencedores de cada rodada
    print("Rodada #{}: {} foi o vencedor".format(i + 1, winners[i]))  # Imprime o vencedor, em cada linha.
         