# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define a função mdc(x, y);
 (2) Inicia um loop infinito while. A cada repetição:
     (3) Tenta ler uma entrada de dois valores x e y, na mesma linha, separados por espaços,
     pelo input().split().
     (4) Caso der EOFError, para o loop com break.
     (5) Converte x em inteiro e atualiza a variável.
     (6) Converte y em inteiro e atualiza a variável.
     (7) Se y for maior que x, troca as variáveis x e y.
     (8) Calcula o tamanho da estaca pela função mdc(x, y) e atribui para stack_size.
     (9) Calcula o número de estacas dividindo cada lado do terreno por stack_size e multiplicando por 2, pois trata-se de um
     retângulo/quadrado e atribui para stacks.
     (10) Imprime stacks
'''

def mdc(x, y):  # Define a função mdc
    
    """
        Função que calcula o mdc entre dois números pelo Algoritmo de Euclides.
        x: número inteiro, x > y.
        y: número inteiro, y < x.
        Retorna um número inteiro, correspondente ao mdc de x e y.
    """
    
    while x % y != 0:  # Enquanto o resto entre x e y for diferente de 0
        aux = y  # Armazena o valor de y
        y = x % y  # Armazena o valor do resto em y
        x = aux  # Insere o valor de y em x
    return y  # Retorna o mdc
    
while True:  # Inicia um loop infinito
    
    try:  # Tenta
        x, y = input().split()  # Le dois valores, na mesma linha, separados por espaços
    except EOFError:  # Se não houverem mais entradas
        break  # Para o loop
    
    x = int(x)  # Converte x em inteiro
    y = int(y)  # Converte y em inteiro
    
    if y > x:  # Se y for maior que x
        aux = x  # Armazena o valor de x
        x = y  # Insere o valor de y em x
        y = aux  # Insere o valor de x em y
    
    stack_size = mdc(x, y)  # Calcula o número de estacas pelo mdc entre x e y
    
    stacks = 2 * ((x // stack_size) + (y // stack_size))  # Calcula o número de estacas
    print(stacks)  # Imprime o total de estacas
        