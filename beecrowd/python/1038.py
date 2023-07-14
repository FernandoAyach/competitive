# -*- coding: utf-8 -*-

'''
Coleta entrada inteira, separando seus elementos(código e quantidade).
Armazena cada elemento da entrada em uma variável, convertendo-os em inteiro.
Realiza uma série de condições que verificam qual o código do produto.
Em cada caso, multiplica-se a quantidade pelo valor do produto, com aproximação
de 2 casas decimais, e imprime na tela.
'''

#Coleta a entrada inteira e quebra em espaços
wholeInput = input().split()

#Recolhe o primeiro elemento da entrada,
#converte em inteiro e armazena na variavel
code = int(wholeInput[0])

#Recolhe o segundo elemento da entrada,
#converte em inteiro e armazena na variavel
quantity = int(wholeInput[1])

#Verifica se é cachorro quente
if(code == 1):
    #Acha o valor total, com duas casas decimais, e imprime na tela
    print('Total: R$ {:.2f}'.format(quantity * 4))
#Verifica se é x-salada
elif(code == 2):
    #Acha o valor total, com duas casas decimais, e imprime na tela
    print('Total: R$ {:.2f}'.format(quantity * 4.5))
#Verifica se é x-bacon
elif(code == 3):
    #Acha o valor total, com duas casas decimais, e imprime na tela
    print('Total: R$ {:.2f}'.format(quantity * 5))
#Verifica se é torrada simples
elif(code == 4):
    #Acha o valor total, com duas casas decimais, e imprime na tela
    print('Total: R$ {:.2f}'.format(quantity * 2))
#Se não foi nenhum dos outros, restou ser refrigerante
else:
    #Acha o valor total, com duas casas decimais, e imprime na tela
    print('Total: R$ {:.2f}'.format(quantity * 1.5))