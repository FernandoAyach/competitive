# -*- coding: utf-8 -*-

'''
Entrada
 (1) Coleta a posição do kung, em uma linha, converte em inteiro, e atribui para
 a variável kung.
 (2) Coleta a posição do lu, em uma linha, converte em inteiro, e atribui para
 a variável lu.

Desenvolvimento:
 (1) Para saber a fase que irão se encontrar, algumas regras lógicas são seguidas, considere
 x e y como jogadores para exemplificação:
 (2) Para se encontrarem na final: x <= 8 and y >= 9
 (3) Para se encontrarem na semifinal: x <= 4 e y entre 5 e 8 ou x entre 9 e 12 e y maior que 13
 (4) Para se encontrarem nas quartas: x(1 ou 2) e y (3 ou 4) ou x(5 ou 6) e y (7 ou 8)
 ou x(9 ou 10) e y (11 ou 12) ou x(13 ou 14) e y >= 15
 (5) Se não for as de cima, se encontrarão, portanto, nas oitavas
 OBS: As comparações serão feitas nas duas possibilidades de arranjo, sendo um na direita
 e outro na esquerda e o contrário.

Saída:
 (1) Em cada caso acima, imprime a fase que se encontrarão na tela
'''
# Coleta a posição do Mestre kung
kung = int(input())

# Coleta a posição do Mestre Lu
lu = int(input())

# Verifica se se encontrarão nas finais
if (kung <= 8 and lu >= 9) or (lu <= 8 and kung >= 9):
    print('final')  # Imprime que se encontrarão na final

# Verifica se se encontrarão nas semifinais
elif kung <= 4 and (lu >= 5 and lu <= 8) \
     or lu <= 4 and (kung >= 5 and kung <= 8) \
     or (kung >= 9 and kung <= 12) and (lu >= 13) \
     or (lu >= 9 and lu <= 12) and (kung >= 13):
    print('semifinal')  # Imprime que se encontrarão na semifinal
# Verifica se se encontrarão nas quartas
elif kung <= 2 and (lu >= 3 and lu <= 4) \
    or lu <= 2 and (kung >= 3 and kung <= 4) \
    or (kung >= 5 and kung <= 6) and (lu >= 7 and lu <= 8) \
    or (lu >= 5 and lu <= 6) and (kung >= 7 and kung <= 8) \
    or (kung >= 9 and kung <= 10) and (lu >= 11 and lu <= 12) \
    or (lu >= 9 and lu <= 10) and (kung >= 11 and kung <= 12) \
    or (kung >= 13 and kung <= 14) and (lu >= 15) \
    or (lu >= 13 and lu <= 14) and (kung >= 15):
    print('quartas')  # Imprime que se encontrarão nas quartas

# Se não se encontrarão nas de cima, se encontrão nas oitavas
else:
    print('oitavas')  # Imprime que se encontrarão nas oitavas
