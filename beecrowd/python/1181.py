# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções read_matrix e sum_line.
 (2) Le a linha ser somada, converte em inteiro e atribui para line_to_sum.
 (3) Le a operação a ser feita e atribui para operation.
 (4) Define uma lista vazia matrix.
 (5) Le os valores da matriz pela função read_matrix.
 (6) Soma a linha pela função sum_line e atribui para line_sum.
 (7) Se a operação for média, imprime a média da soma dos valores, com uma casa decimal.
 (8) Senão, mostra line_sum.
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

def sum_line(line, columns, matrix):  # Define a função sum_line
    """
        Função que recebe uma linha, o número de colunas e uma matriz e soma
        os valores da linha determinada.
        line: inteiro representando a linha a ser somada.
        columns: número de colunas da matriz.
        matrix: matriz qualquer.
        Retorna a soma dos valores da linha determinada.
    """
    
    line_sum = 0  # Soma da linha
    for i in range(columns):  # Percorre as colunas
        line_sum += matrix[line][i]  # Soma todos os valores da linha em line_sum
    return line_sum  # Retorna a soma

line_to_sum = int(input())  # Le a linha a ser somada
operation = input()  # Le a operação a ser feita

matrix = []  # Inicia uma lista vazia
# Le uma série de valores float e insere na matriz
read_matrix(12, 12, matrix)  

line_sum = sum_line(line_to_sum, 12, matrix)  # Soma a linha da matriz

if operation == "M":  # Se a operação é média
    print("{:.1f}".format(line_sum / 12))  # Imprime a média da soma dos valores, com uma casa decimal
else:  # Senão
    print(line_sum)  # Imprime a soma da linha