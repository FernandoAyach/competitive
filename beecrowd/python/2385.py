# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções get_parameters, get_c_coordinates e get_c_term.
 (2) Le a dimensão da matriz, converte em inteiro, e atribui para n.
 (3) Le os parâmetros p, q, r, s, x, y pela função get_parameters.
 (4) Le as coordenadas da matriz c c_i, c_j pela função get_c_coordinates.
 (5) Imprime o elemento da matriz c: c[c_i][c_j] pela função get_c_term.
'''

def get_parameters():  # Define a função get_parameters
    """
        Função que le os parâmetros para a criação
        das matrizes A e B e os retorna.
        Retorna uma lista de parâmetros inteiros.
    """
    
    # Le os parâmetros, em uma linha, separados por espaços
    parameters = input().split()  
    
    for i in range(6):  # Percorre os 6 parâmetros
        parameters[i] = int(parameters[i])  # Converte em inteiro
    return parameters  # Retorna os parâmetros

def get_c_coordinates():  # Define a função get_c_coordinates
    """
        Função que le as coordenadas i j da matriz C e as retorna,
        convertidas em inteiro e decrescidas de 1.
        Retorna as coordenadas i j da matriz C, convertidas em
        inteiro e decrescidas de 1.
    """
    
    # Le a linha e a coluna da matriz C, na mesma linha, separadas por espaço
    c_i, c_j = input().split()  
    return (int(c_i) - 1), (int(c_j) -1)  # Retorna-as decrescidas de 1

def get_c_term(n, c_i, c_j):  # Define a função build_matrix_a_b
    """
        Função que recebe a dimensão da matriz, a coordenadas do elemento
        da matriz c e calcula o termo.
        n: inteiro referente à dimensão da matriz.
        c_i: inteiro referente à linha do elemento de c.
        c_j: inteiro referente à coluna do elemento de c.
        Retorna o elemento de c.
    """
    
    line_a = [0] * n  # Cria a linha de a
    column_b = [0] * n  # Cria a coluna de b
    value = 0  # Valor do termo de c
    for w in range(n):  # Percorre n vezes
        line_a[w] = (p * (c_i + 1) + q * (w + 1)) % x  # Calcula a linha de A
        column_b[w] = (r * (w + 1) + s * (c_j + 1)) % y  # Calcula a coluna de B
        value += line_a[w] * column_b[w]  # Calcula o termo
    
    return value  # Retorna o termo

n = int(input())  # Le a dimensão da matriz
p, q, r, s, x, y = get_parameters()  # Le os parâmetros 
c_i, c_j = get_c_coordinates()  # Le as coordenadas da matriz C

print(get_c_term(n, c_i, c_j))  # Imprime o valor de C[c_i][c_j]
