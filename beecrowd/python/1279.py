# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Coleta o valor do ano, em uma linha, converte para inteiro, pelo int(), e atribui para a variável year.
 (2) Inicia um loop infinito while
 (3) Cria 3 variáveis booelanas leap, huluculu e bulukulu com valor False, para posterior uso.
 (4) Se for bissexto, imprime 'This is leap year.' e atualiza leap para True.
 (5) Se for huluculu, imprime 'This is huluculu festival year.' e atualiza huluculu para True.
 (6) Se for bulukulu, imprime 'This is bulukulu festival year.' e atualiza bulukulu para True.
 (7) Se leap, huluculu e bulukulu forem False, é um ano normal, imprime 'This is an ordinary year.'.
 (8) Tenta pegar mais um valor de ano, pelo mesmo processo do passo 1, se der EOF, para o loop com break,
 caso contrário, obtem o ano e pula uma linha, pois ainda há mais casos de teste.
'''

year = int(input())  # Coleta o ano, em inteiro
while True:  # Inicia um loop infinito
    leap = False  # Não é bissexto
    huluculu = False  # Não é huluculu
    bulukulu = False  # Não é bulukulu
   
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:   # Se é ano bissexto
        print('This is leap year.')  # Imprime bissexto na tela
        leap = True  # É bissexto
    if year % 15 == 0:  # Se o ano é huluculu
        print('This is huluculu festival year.')  # Imprime huluculu na tela
        huluculu = True  # É huluculu
    if year % 55 == 0 and leap:   # Se o ano é bulukulu
        print('This is bulukulu festival year.')  # Imprime bulukulu na tela
        bulukulu = True  # É bulukulu
    
    if not (leap or huluculu or bulukulu):  # Se não há especialidades no ano
        print('This is an ordinary year.')  # Imprime ano normal
    
    try:  # Tenta obter próxima entrada
        year = int(input())  # Coleta o próximo ano
        print()  # Pula uma linha, já que não é o último teste
    except EOFError:  # Se acabaram as entradas
        break  # Para o loop
    
    