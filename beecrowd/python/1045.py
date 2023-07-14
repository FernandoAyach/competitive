# -*- coding: utf-8 -*-

'''
Coleta a entrada completa e separa seus elementos em uma lista.
Insere cada elemento (lado do triângulo) em variáveis, como números reais.
Define variáveis para armazenar o maior valor, menor valor e o do meio.
Tendo os dados em mãos, primeiro é preciso colocar os valores em ordem decrescente, para isso,
São verificadas as seguintes condições:

Valores todos iguais:
Define os valores na ordem natural: A maior, B do meio, C menor

Valores todos diferentes:
Compara-se em cada valor se é maior que todos os outros, menor que todos os outros ou um valor mediano,
não sendo maior que todos e nem menor que todos.

2 valores iguais:
Em todos os casos verifica-se quais são os valores iguais e se são maiores que o terceiro valor. Caso
forem menores que esse terceiro valor, serão posicionados como valor do meio e valor menor.
Se forem maiores que o terceiro valor, serão posicionados como valor maior e valor do meio.

Ordenados os valores, utiliza das fórmulas de existência de triângulo para definir se os
lados recebidos conferem um triângulo possivel, retângulo, obtusângulo ou acutângulo.
Também se é equilátero ou isosceles.
Em cada caso imprime o resultado na tela.
'''

#Coleta a entrada e insere em uma lista cada valor
wholeInput = input().split()

#Coleta o primeiro valor
A = float(wholeInput[0])
#Coleta o segundo valor da lista
B = float(wholeInput[1])
#Coleta o segundo valor da lista
C = float(wholeInput[2])

#Inicia variáveis que armazenarão os valores do maior, do meio e do menor
bigger = 0.0
mid = 0.0
minor = 0.0

#Ordenar em ordem decrescente:

if(A == B and A == C): #Todos iguais
    bigger = A #Define A como maior
    mid = B #Define B como meio
    minor = C  #Define C como menor
elif((A != B and A != C) and (B != A and B != C)): #Todos diferentes
    
    #Verificações de A, considerando que todos são diferentes
    
    if(A > B and A > C): #A é o maior
        bigger = A #Define A como maior
    elif(A < B and A < C): #A é o menor
        minor = A #Define A como menor
    else: #Se não é o maior, nem o menor, é o do meio
        mid = A #Define A como meio
    
    #Verificações de B, considerando que todos são diferentes
        
    if(B > A and B > C): #B é o maior
        bigger = B #Define B como maior
    elif(B < A and B < C): #B é o menor
        minor = B #Define B como menor
    else: #Se não é o maior, nem o menor, é o do meio
        mid = B #Define B como meio
    
    #Verificações de C, considerando que todos são diferentes
        
    if(C > B and C > A): #C é o maior
        bigger = C #Define C como maior
    elif(C < A and C < B): #C é o menor
        minor = C #Define C como menor
    else: #Se não é o maior, nem o menor, é o do meio
        mid = C #Define como meio        
else: # Se não 100% iguais, nem diferentes, existem 2 números iguais
    
    if(A == B): #A é igual a B
        if(A > C): #A é maior que C, sendo igual ao B
            bigger = A #Define A com maior
            mid = B #Define B com meio
            minor = C #Define C com menor
        else: # A não é maior que C
            bigger = C #Define C com maior
            mid = A #Define A com meio
            minor = B #Define B com menor
    elif(B == C): # B é igual a C
        if(B > A): #B é maior que A
            bigger = B #Define B com maior
            mid = C #Define C como meio
            minor = A #Define A como menor
        else: #B é menor que A
            bigger = A #Define A com maior
            mid = B #Define B como meio
            minor = C #Define C como menor
    else: #A não é igual B e B não é igual a C, portanto, A == C, já que são 2 números iguais
        if(A > B): #A é maior que B
            bigger = A #Define A com maior
            mid = C #Define C como meio
            minor = B #Define B como menor
        else: #A não é maior que B
            bigger = B #Define B com maior
            mid = A #Define A como meio
            minor = C #Define C como menor
            
#Definir Triângulo:

if(bigger >= mid + minor): #Não forma triângulo, pois o maior é maior ou igual a soma dos menores
    print('NAO FORMA TRIANGULO') #Imprime resultado na tela
elif(bigger**2 == mid**2 + minor**2): #É um triângulo retângulo, pois o quadrado do maior é igual que a soma do quadrado dos menores
    print('TRIANGULO RETANGULO') #Imprime resultado na tela
elif(bigger**2 > mid**2 + minor**2): #É um triângulo obtusângulo, pois o quadrado do maior é maior que a soma do quadrado dos menores
    print('TRIANGULO OBTUSANGULO') #É um triângulo obtusângulo
elif(bigger**2 < mid**2 + minor**2): #É um triângulo acutângulo, pois o quadrado do maior é menor que a soma do quadrado dos menores
    print('TRIANGULO ACUTANGULO') #É um triângulo acutângulo
    
if(bigger == mid and bigger == minor): #É um triângulo equilátero, pois tem 3 lados iguais
    print('TRIANGULO EQUILATERO') #Imprime resultado na tela
elif(bigger == mid or bigger == minor): #É um triângulo isosceles, pois tem 2 lados iguais
    print('TRIANGULO ISOSCELES') #Imprime resultado na tela
elif(mid == minor): #É um triângulo isosceles, pois tem 2 lados iguais
    print('TRIANGULO ISOSCELES') #Imprime resultado na tela