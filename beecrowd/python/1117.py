# -*- coding: utf-8 -*-

'''
Entrada + Desenvolvimento + Saída:
 (1) Inicia uma constante NO_SCORE com valor -1 para representar notas não preenchidas ainda.
 (2) Inicia p1 e p2 com valores NO_SCORE.
 (3) Cria um loop while que repete enquanto p1 e p2 forem NO_SCORE. Nessas condições, o while repete:
 (4) Coleta uma nota, em uma linha, converte em real, pelo float() e atribui para a variável p.
 (5) Se a nota estiver no intervalo [0, 10], atribui o valor de p para p1, caso ela for NO_SCORE, senão atribui para
 p2.
 (6) Se a nota não estiver no intervalo [0, 10], imprime nota invalida.
 (7) Tendo obtido as duas notas, o while para de repetir, e então imprime, após o loop, o valor da média com duas casas decimais
'''

NO_SCORE = -1
p1 = NO_SCORE  # Inicia variável da p1 com valor -1
p2 = NO_SCORE  # Inicia variável da p2 com valor -1

while p1 == NO_SCORE or p2 == NO_SCORE:  # Inicia um loop que repete o bloco de código enquanto uma nota for -1
    
    p = float(input())  # Coleta uma nota, em real
    if p >= 0  and p <= 10:  # Verifica se esta entre [0, 10]
        if p1 == NO_SCORE:  # Se não há p1
            p1 = p  # Atribui o valor p em p1
        else:  # Se há p1
            p2 = p  # Atribui o valor p em p2
    else:  # Senão for uma nota dentro do intervalo
        print('nota invalida')  # Imprime que é inválida
print('media = {:.2f}'.format((p1 + p2) / 2))  # Imprime resultado da média
