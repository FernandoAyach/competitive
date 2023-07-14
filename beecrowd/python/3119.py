# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta o comprimento de fita total, em uma linha, pelo input(), converte em real,
 pelo float(), e atribui à variável full_tape.
 (2) Para evitar problemas com aproximação, a unidade será convertida para cm, ou seja,
 cria-se uma nova variável full_tape_int e atribui o valor de full_tape x 100, convertido em
 inteiro, pelo int(), para retirar o '.0'.

Desenvolvimento:
 (1) Para calcular o máximo de fitas de cada comprimento, utiliza-se de divisões e restos inteiros, ou seja,
 para cada comprimento, divide-se a o comprimento total pelo tamanho correspondente, atribui para uma variável que
 guardará a quantidade de pedaços e, após isso, coleta o resto da divisão e atualiza a variável full_tape_int, que será utilizada
 na divisão seguinte. As variáveis de quantidade são tape_100cm, tape_50cm, tape_20cm, tape_10cm, tape_5cm e tape_1cm.

Saída:
 (1) Imprime a quantidade total de fita
 (2) Imprime, em linhas diferentes, cada quantidade de fita.
'''

full_tape = float(input())  # Coleta a fita total, em real

full_tape_int = int(full_tape * 100)  # Transforma em inteiro (cm)

tape_100cm = full_tape_int // 100  # Calcula a quantidade de fitas de 1m
full_tape_int = full_tape_int % 100  # Atualiza o total após a divisão anterior

tape_50cm = full_tape_int // 50  # Calcula a quantidade de fitas de 0.5m
full_tape_int = full_tape_int % 50  # Atualiza o total após a divisão anterior

tape_20cm = full_tape_int // 20  # Calcula a quantidade de fitas de 0.2m
full_tape_int = full_tape_int % 20  # Atualiza o total após a divisão anterior

tape_10cm = full_tape_int // 10  # Calcula a quantidade de fitas de 0.1m
full_tape_int = full_tape_int % 10 # Atualiza o total após a divisão anterior

tape_5cm = full_tape_int // 5  # Calcula a quantidade de fitas de 0.05m
full_tape_int = full_tape_int % 5  # Atualiza o total após a divisão anterior

tape_1cm = full_tape_int  # Calcula a quantidade de fitas de 0.01m

print('Para um adereço de {:.2f} metro(s) são necessárias:'.format(full_tape))  # Imprime a quantidade de fita total
print('   1 m: {} fita(s)'.format(tape_100cm))  # Imprime a quantidade de 1m
print(' 0,5 m: {} fita(s)'.format(tape_50cm))  # Imprime a quantidade de 0.5m
print(' 0,2 m: {} fita(s)'.format(tape_20cm))  # Imprime a quantidade de 0.2m
print(' 0,1 m: {} fita(s)'.format(tape_10cm))  # Imprime a quantidade de 0.1m
print('0,05 m: {} fita(s)'.format(tape_5cm))  # Imprime a quantidade de 0.05m
print('0,01 m: {} fita(s)'.format(tape_1cm))  # Imprime a quantidade de 0.01m

