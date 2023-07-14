# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções sum_values e get_max_worms.
 (2) Imprime o máximo de minhocas chamando a função get_max_worms.
'''

def sum_values(seq):  # Define a função sum_values
    """
        Função que recebe uma lista e retorna a soma de seus valores.
        seq: lista de strings.
        Retorna a soma da lista.
    """
    
    total = 0  # Soma total
    for i in range(len(seq)):  # Percorre os valores da linha
        total += int(seq[i])  # Soma-os em total
    return total  # Retorna a soma

lines, columns = input().split()  # Le o número de linhas e colunas, na mesma linha
lines = int(lines)  # Converte lines em inteiro
columns = int(columns)  # Converte lines em columns

def get_max_worms(lines, columns):  # Define a função get_max_worms
    """
        Função que recebe o número de linhas e de colunas de uma matriz e
        retorn o máximo de minhocas coletadas em uma só passada (linha ou coluna).
        lines: inteiro representando o número de linhas.
        columns: inteiro representando o número de colunas.
        Retorna o máximo de minhocas coletadas em uma só passada (linha ou coluna).
    """
    
    bigger = 0  # Maior soma
    l_worms = 0  # Soma da linha
    columns_sum = [0] * columns  # Soma das colunas
    
    for i in range(lines):  # Percorre as linhas
        line = input().split()  # Le os valores de uma linha, separados por espaços
        l_worms = sum_values(line)  # Soma os valores da linha por sum_values
        
        if l_worms > bigger:  # Se a soma da linha é maior que bigger
            bigger = l_worms  # Bigger é l_worms
        
        for j in range(columns):  # Percorre as colunas
            columns_sum[j] += int(line[j])  # Soma o valor da coluna em column_sum[j]

    for i in range(columns):  # Percorre as colunas
        if columns_sum[i] > bigger:  # Se a soma da coluna for maior que bigger
            bigger = columns_sum[i]  # Bigger é column_sum[i]
            
    return bigger  # Retorna bigger

print(get_max_worms(lines, columns))  # Imprime o máximo de minhocas
    