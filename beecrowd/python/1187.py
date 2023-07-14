# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções read_superior_area_matrix e sum_values.
 (2) Le a operação a ser feita e atribui para operation.
 (3) Le os valores da área superior da matriz pela função
 read_superior_area_matrix e atribui para seq.
 (4) Soma os valores da sequência pela função sum_values e atribui para total.
 (5) Se a operação for média, imprime a média da soma dos valores, com uma casa decimal.
 (6) Senão, mostra total, com uma casa decimal.
'''

def read_superior_area_matrix(lines, columns):  # Define a função read_superior_area_matrix
    """
        Função que recebe as linhas e colunas de uma matriz e retorna a uma
        lista somente com os valores da área superior da matriz.
        lines: inteiro referente às linhas.
        columns: inteiro referente às colunas.
        Retorna uma lista com os valores da área superior da matriz.
    """
    seq = []  # Define uma lista vazia
    
    for i in range(lines):  # Percorre as linhas da matriz
        for j in range(columns):  # Percorre as colunas da matriz
            # Se o valor estiver na área superior da matriz
            if (j <= 5 and j > i) or (j >= 6 and i + j <= 10):  
                seq.append(float(input()))  # Insere o valor, já em real, em seq
            else:  # Senão
                input()  # Le um valor   
    return seq  # Retorna a lista com os valores da área superior da matriz.

def sum_values(seq):  # Define a função sum_values
    """
        Função que recebe uma lista e soma todos seus valores.
        seq: lista de floats.
        Retorna a soma total dos valores.
    """
    
    total = 0  # Soma total
    for i in range(len(seq)):  # Percorre a lista inteira
        total += seq[i]  # Soma os valores
    return total  # Retorna a soma

operation = input()  # Le a operação a ser feita

seq = read_superior_area_matrix(12, 12)  # Le a área superior da matriz.
total = sum_values(seq)  # Obtem a soma dos valores

if operation == "M":  # Se a operação é média
    print("{:.1f}".format(total / len(seq)))  # Imprime a média da soma dos valores, com uma casa decimal
else:  # Senão
    print("{:.1f}".format(total))  # Imprime a soma, com uma casa decimal
