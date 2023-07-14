# -*- coding: utf-8 -*-

'''
Coleta entrada inteira, separa e insere os valores de a, b e c
em variáveis, em número real.
Calcula o valor do delta.
Se o delta for negativo ou o "a" for zero, é impossivel calcular.
Contrário, faz o cálculo restante encontrando o valor das raízes.
Imprime na tela.
'''

whole_input = input().split() # Coleta entrada inteira

a = float(whole_input[0]) # Insere o valor de a
b = float(whole_input[1]) # Insere o valor de b
c = float(whole_input[2]) # Insere o valor de c

delta = (b**2 - 4*a*c) # Calcula o delta

if(delta < 0 or a == 0): # Impossivel calcular se for true
    print('Impossivel calcular') # Imprime na tela
else: # É possivel calcular
    r1 = (-b + delta**0.5) / (2*a) # Calcula a raiz 1
    r2 = (-b - delta**0.5) / (2*a) # Calcula a raiz 2
    
    # Imprime valores na tela
    print('R1 = {:.5f}'.format(r1)) 
    print('R2 = {:.5f}'.format(r2))