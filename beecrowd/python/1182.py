# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções read_matrix e sum_column.
 (2) Le a coluna ser somada, converte em inteiro e atribui para column_to_sum.
 (3) Le a operação a ser feita e atribui para operation.
 (4) Define uma lista vazia matrix.
 (5) Le os valores da matriz pela função read_matrix.
 (6) Soma a coluna pela função sum_column e atribui para column_sum.
 (7) Se a operação for média, imprime a média da soma dos valores, com uma casa decimal.
 (8) Senão, mostra column_sum.
'''

def read_matrix(lines, columns, matrix):  # Define a função read_matrix
    """
        Função que recebe o número de linhas e colunas de uma matriz e
        uma matriz vazia e a preenche com números float.
        lines: inteiro representando as linhas.
        columns: inteiro representando as colunas.
        matrix: lista vazia.
        Retorna uma matriz lines x columns com valores inteiros.
    """
    
    for i in range(lines):  # Percorre as linhas
        
        line = [0] * lines  # Cria uma linha com posições zero
        for j in range(columns):  # Percorre as colunas
            line[j] = float(input())  # Le o valor, converte em float e atribui para a coluna
        
        matrix.append(line)  # Insere a linha na matriz

def sum_column(column, lines, matrix):  # Define a função sum_line
    """
        Função que recebe uma coluna, o número de linhas e uma matriz e soma
        os valores da coluna determinada.
        column: inteiro representando a coluna a ser somada.
        lines: número de linhas da matriz.
        matrix: matriz qualquer.
        Retorna a soma dos valores da coluna determinada.
    """
    
    column_sum = 0  # Soma da coluna
    for i in range(lines):  # Percorre as linhas
        column_sum += matrix[i][column]  # Soma todos os valores da coluna em column_sum
    return column_sum  # Retorna a soma

column_to_sum = int(input())  # Le a coluna a ser somada
operation = input()  # Le a operação a ser feita

matrix = []  # Inicia uma lista vazia
# Le uma série de valores float e insere na matriz
read_matrix(12, 12, matrix)  

column_sum = sum_column(column_to_sum, 12, matrix)  # Soma a coluna da matriz

if operation == "M":  # Se a operação é média
    print("{:.1f}".format(column_sum / 12))  # Imprime a média da soma dos valores, com uma casa decimal
else:  # Senão
    print(column_sum)  # Imprime a soma da coluna
