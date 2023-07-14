# -*- coding: utf-8 -*-

'''
Coleta a entrada inteira do usuário e separa seus elementos por espaços.
Insere cada elemento em sua respectiva variável em valor inteiro.
Inicizaliza variáveis correspondentes ao maior, menor e o número do meio.
Faz uma série de comparações verificando, primeiro quem é o maior.
Se um número é maior que todos os outros, ele é o maior.
Em seguida, verifica quem é o menor. Se um número é menor que todos os outros, ele é o menor
Cria um laço de repetição que correrá todos os elementos, verificando qual é o maior e qual é o menor.
O número que não se enquadra nisso é o número do meio.
Imprime os valores ordenados e os originais, com uma quebra de linha entre eles.
'''

#Coleta entrada inteira
wholeInput = input().split()

#Coleta os valores da entrada e converte para inteiro
firstValue = int(wholeInput[0])
secondValue = int(wholeInput[1])
thirdValue = int(wholeInput[2])

#Inicia variáveis para armazenar o maior, o meio e o menor
bigger = 0
mid = 0
minor = 0

#Verifica se o primeiro é o maior
if(firstValue > secondValue and firstValue > thirdValue):
    #Armazena o primeiro como maior
    bigger = firstValue
#Verifica se o segundo é o maior
elif(secondValue > thirdValue and secondValue > firstValue):
    #Armazena o segundo como maior
    bigger = secondValue
#Se não for nenhum dos outros dois, o terceiro é o maior
else:
    #Armazena o terceiro como maior
    bigger = thirdValue
    
#Verifica se o primeiro é o menor
if(firstValue < secondValue and firstValue < thirdValue):
    #Armazena o primeiro como menor
    minor = firstValue
#Verifica se o segundo é o menor
elif(secondValue < thirdValue and secondValue < firstValue):
    #Armazena o segundo como menor
    minor = secondValue
#Se não for nenhum dos outros dois, o terceiro é o menor
else:
    #Armazena o terceiro como menor
    minor = thirdValue

#Inicia variável de iteração
i = 0

#Percorre toda a entrada de elementos
while(i < len(wholeInput)):
    #Se o valor não for o maior nem o menor, ele será o do meio
    if(int(wholeInput[i]) != bigger and int(wholeInput[i]) != minor):
        #Armazena o valor como o do meio
        mid = int(wholeInput[i])
    #Incrementa iteração
    i+=1

#Imprime valores ordenados
print(minor)
print(mid)
print(bigger)

#Quebra linha
print()

#Imprime valores na ordem original
print(firstValue)
print(secondValue)
print(thirdValue)