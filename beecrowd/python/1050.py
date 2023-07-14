# -*- coding: utf-8 -*-

'''
Coleta o DDD, em inteiro.
Verifica o DDD coletado com a discagem interurbana de cada cidade correspondente.
Se for correspondente com a discagem de uma, imprime mensagem na tela com o nome da cidade.
Caso contrário, imprime que o DDD recebido não é cadastrado.
'''
#Coleta o DDD, convertendo em inteiro
ddd = int(input())

#Verifica se é correspondente ao de DDD de Brasilia
if(ddd == 61):
    #Imprime cidade na tela
    print('Brasilia')
#Verifica se é correspondente ao de DDD de Salvador
elif(ddd == 71):
    #Imprime cidade na tela
    print('Salvador')
#Verifica se é correspondente ao de DDD de Paulo
elif(ddd == 11):
    #Imprime cidade na tela
    print('Sao Paulo')
#Verifica se é correspondente ao de DDD de Rio de Janeiro
elif(ddd == 21):
    #Imprime cidade na tela
    print('Rio de Janeiro')
#Verifica se é correspondente ao de DDD de Juiz de Fora
elif(ddd == 32):
    #Imprime cidade na tela
    print('Juiz de Fora')
#Verifica se é correspondente ao de DDD de Campinas
elif(ddd == 19):
    #Imprime cidade na tela
    print('Campinas')
#Verifica se é correspondente ao de DDD de Vitoria
elif(ddd == 27):
    #Imprime cidade na tela
    print('Vitoria')
#Verifica se é correspondente ao de DDD de Belo Horizonte
elif(ddd == 31):
    #Imprime cidade na tela
    print('Belo Horizonte')
#Se não for nenhum dos casos a cima
else:
    #Imprime DDD nao cadastrado
    print('DDD nao cadastrado')
    