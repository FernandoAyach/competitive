# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta a idade da Mônica, em uma linha, converte para inteiro, pelo int(), e atribui
 para a variável monica.
 (2) Coleta a idades dos filhos, um em cada linha, converte-as em inteiro e atribui para as variáveis
 son1 e son2, respectivamente.
 (3) A idade do terceiro filho é a idade de monica menos a soma da idade dos outros filhos. Obtem o resultado
 e atribui para variável son3.
 (3) Inicializa uma variável de mais velho, older, e armazena inicialmente o son1.
 
Desenvolvimento:
 (1) Se o son2 for maior que o older, ele será o mais velho, substitui a variável.
 (2) Se o son3 for maior que o older, ele será o mais velho, substitui a variável.
 (3) Se não for nenhum dos casos, s1 já era o mais velho.
 
Saída:
 (1) Imprime a idade do mais velho
'''

monica = int(input())  # Coleta a idade de monica em inteiro
son1 = int(input())  # Coleta a idade do primeiro filho em inteiro
son2 = int(input())  # Coleta a idade do segundo filho em inteiro

son3 = monica - (son1 + son2)  # Calcula a idade do terceiro filho

older = son1  # Define um mais velho provisório

# Se son2 for mais velho que o atual
if son2 > older:
    # Esse será o mais velho
    older = son2
# Se son3 for mais velho que o atual
if son3 > older:
    # Esse será o mais velho
    older = son3
    
# Imprime o mais velho na tela  
print(older)