# -*- coding: utf-8 -*-

'''
Cria uma lista vazia para armazenar todos os valores.
Inicializa todas as variáveis para conter os valores de quantidade de par, impar, positivo e negativo.
Inicia uma repetição que coletará valores do usuário, convertendo em inteiro, adicionará na lista de valores
e fará em seguida, com o valor coletado, a verificação de número par (resto da divisão com 2 é 0, caso contrario é impar) e
a verificação de positivo e negativo (se maior que zero é positivo, caso contrário é negativo).
Imprime as quantidades na tela após a repetição
'''

#Inicia lista vazia
values = []

#Inicia variáveis das quantidades de par, impar, positivo e negativo
pair = 0
odd = 0
positive = 0
negative = 0

#Inicia iterador
i = 0

#Repetição que percorrerá a lista de valores conforme for sendo adicionados os 5 elementos
while(i < 5):
    #Coleta valor, converte em inteiro e adiciona na lista
    values.append(int(input()))
    
    #Se esse valor for divisivel por 2, é par
    if(values[i] % 2 == 0):
        pair+= 1
    #Caso contrário é impar
    else:
        odd+= 1
    #Se for maior que zero, é positivo
    if(values[i] > 0):
        positive+= 1
    #Caso contrário, é negativo
    elif(values[i] < 0):
        negative+= 1
        
    #Incrementa iteração
    i+=1
    
#Imprime valores na tela
print('{} valor(es) par(es)'.format(pair))
print('{} valor(es) impar(es)'.format(odd))
print('{} valor(es) positivo(s)'.format(positive))
print('{} valor(es) negativo(s)'.format(negative))





