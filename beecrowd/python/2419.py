# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções read_matrix, is_coast e count_coast.
 (2) Le o número de linhas e colunas de um mapa, na mesma linha, separados por espaços,
 pelo input().split(), e atribui para m e n.
 (3) Converte m para inteiro, atualiza a variável.
 (4) Converte n para inteiro, atualiza a variável.
 (5) Le a matriz por read_matrix e atribui para matrix.
 (6) Imprime o total de costas pela função count_coast.
'''

def read_matrix(m):  # Define a função read_matrix
    """
        Função que le uma matriz quadrada m e a retorna.
        m: inteiro referente ao número de linhas.
        Retorna a matriz lida.
    """
    
    matrix = []  # Inicia uma lista vazia
    for i in range(m):  # Percorre todas as linhas
        line = list(input())  # Le uma lista referente a uma linha do mapa
        matrix.append(line)  # Insere a linha na matriz
    return matrix  # Retorna a matriz

def is_coast(i, j, m, n, matrix):  # Define a função is_coast
    """
        Função que recebe um posição i;j, as dimensões de uma
        matrix e a matrix e retorna se determinado pedaço de terra é
        costa.
        i: inteiro referente à linha.
        j: inteiro referente à coluna.
        m: inteiro referente ao total de linhas.
        n: inteiro referente ao total de colunas.
        matrix: matriz em questão.
        Retorna True se for costa e False caso contrário.
    """
    
    edge_line = (i == 0 or (i == m - 1))  # Linha limite
    edge_column = (j == 0 or (j == n - 1))  # Coluna limite
    border = (edge_line or edge_column)  # Está na borda
    
    # Se está na beira do mapa ou existe coluna à direita e tem água
    if border or (j + 1 < n and matrix[i][j + 1] == "."):  
       return True   # É uma costa     
    # Se está na beira do mapa ou existe coluna à esquerda e tem água
    if border or (j - 1 >= 0 and matrix[i][j - 1] == "."):
        return True   # É uma costa
    # Se está na beira do mapa ou existe linha abaixo e tem água
    if border or (i + 1 < m and matrix[i + 1][j] == "."):
        return True   # É uma costa
    # Se está na beira do mapa ou existe linha acima e tem água
    if border or (i - 1 >= 0 and matrix[i - 1][j] == "."):
        return True  # É uma costa
    return False  # Não é uma costa

def count_coast(m, n, matrix):  # Define a função count_coast
    """
        Função que recebe o total de linhas e de colunas e
        uma matrix e conta quantas costas tem essa matriz.
        m: inteiro referente ao total de linhas.
        n: inteiro referente ao total de colunas.
        matrix: matriz em questão.
        Retorna o total de costas.
    """
    
    coasts = 0  # Contador de costas
    for i in range(m):  # Percorre todas as linhas
        for j in range(n):  # Percorre todas as colunas
            # Se é terra e é uma costa
            if matrix[i][j] == "#" and is_coast(i, j, m, n, matrix):
                coasts += 1  # Conta uma costa
    return coasts  # Retorna o número de costas

# Le as linhas e colunas de um mapa, na mesma linha, separados por espaços
m, n = input().split()  
m = int(m)  # Converte m em inteiro
n = int(n)  # Converte n em inteiro

matrix = read_matrix(m)  # Le a matriz
print(count_coast(m, n, matrix))  # Imprime o número de costas

