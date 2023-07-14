# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta 4 valores na mesma linha, separados por espaços, pelo input().split(). Detalhe que nem todos
 os valores serão úteis para a solução, portanto serão denotados como _ e __, e não serão utilizados. Além disso, atribui
 os valores da data inicial e do mes inicial para init_day e init_month.
 (2) Repete o mesmo processo acima, com a diferença que será coletado o dia final e o mes final, respectivamente atribuidos para
 as variáveis final_day e final_month.
 (3) Converte as datas para inteiro, a partir do int(), e atualiza suas respectivas variáveis.

Desenvolvimento:
 (1) Inicia uma constante APRIL_TOTAL_DAYS definindo os dias do mês de abril.
 (2) Se o init_month é igual ao final_month, o mês é o mesmo, portanto o número de dias será a data inicial
 menos a final. Atribui o valor para a variável total_days.
 (3) Se o init_month é diferente ao final_month, o mês é o diferente, portanto o número de dias será a o número de dias de abril menos
 a data inicial, somado à data final. Atribui o valor para a variável total_days.

Saída:
 (1) Imprime o total de dias na tela com a sintaxe: Entre init_day de init_month e final_day de final_month há total_days dias.
'''

_, init_day, __, init_month = input().split()  # Coleta o dia inicial e o mês inicial, na mesma linha, separados por espaços
init_day = int(init_day)  # Converte o dia inicial para inteiro

_, final_day, __, final_month = input().split()  # Coleta o dia final e o mês final, na mesma linha, separados por espaços
final_day = int(final_day)  # Converte o dia final para inteiro

APRIL_TOTAL_DAYS = 30  # Dias totais de abril

if init_month == final_month:  # Se for no mesmo mês
    total_days = final_day - init_day  # Calculo é final - inicial
    print('Entre', init_day, 'de', init_month,'e', final_day, 'de', init_month,'há', total_days,'dias.')  # Imprime resultado na tela
else:  # Senão, em meses diferentes
    total_days = (APRIL_TOTAL_DAYS - init_day) + final_day  # Calculo é (dias de abril - inicial) + dias de maio
    print('Entre', init_day, 'de', init_month,'e', final_day, 'de', final_month,'há', total_days,'dias.')  # Imprime resultado na tela