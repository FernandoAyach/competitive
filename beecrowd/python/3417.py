# -*- coding: utf-8 -*-

'''
Coleta entrada inteira e separa os valores.
Insere os valores de estudantes, litros por rodada e litros minimos por estudante
em variáveis, já em inteiro.
Calcula a quantidade mínima de litros necessária.
Calcula a quantidade de rodadas de café necessárias dividindo a quantidade minima
pela quantidade que pode ser feita por vez.
Detalhe que como só podem ser feitas uma quantidade fixa de café por vez,
na conta utiliza-se uma aproximação para cima, ou seja, se fossem necessários 0.4 litros a mais, uma rodada
inteira de café teria que ser feita, mesmo que ultrapassasse o mínimo.
Imprime na tela a quantidade total a ser feita.
'''

import math #Importa o módulo math

wholeInput = input().split() #Coleta entrada inteira

totalStudents = int(wholeInput[0]) #Insere o número de estudantes
litersPerTime = int(wholeInput[1]) #Insere os litros fixo por rodada
litersPerStudent = (int(wholeInput[2])) / 1000 #Insere a quantidade mínima de café por aluno
 
minLitersQuantity = totalStudents * litersPerStudent #Calcula a quantidade minima da sala

coffeeRounds = math.ceil(minLitersQuantity / litersPerTime) #Calcula a quantidade de rodadas necessárias para suprir o minimo

print(coffeeRounds * litersPerTime) #Imprime total na tela