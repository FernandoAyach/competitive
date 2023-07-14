# -*- coding: utf-8 -*-

'''
Coleta o valor do raio, converte em número real e armazena em uma variável
Insere o valor do PI em uma variável.
Faz o cálculo da área e insere em uma variável.
Imprime resultado na tela com 4 casas decimais de aproximação.
'''

r = float(input()) #Coleta o raio como numero real
pi = 3.14159 #Insere valor do PI
area =  pi * r**2 #Faz o calculo da area do circulo

print('A=%.4f' % (area)) #Imprime na tela com 4 casas de aproximação
