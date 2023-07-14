# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções sum_values, has_pattern.
 (2) Le a dimensão da matriz, em inteiro, e atribui para n.
 (3) Define as variáveis para soma da linha, soma da diagonal principal, da diagonal
 secundária e das colunas (lista de tamanho n), todas com valor inicial o, respectivamente
 line_sum, main_diagonal_sum, secondary_diagonal_sum e column_sum.
 (4) Inicia uma variável pattern para armazenar o padrão de soma.
 (5) Inicia uma variável booleana maybe_has_pattern, com valor True, para indicar se
 existe a possibilidade de ter padrão.
 (6) Inicia um loop for percorrendo n linhas. A cada repetição:
     (7) Le os valores de uma linha, separados por espaços, pelo input().split() e atribui para line.
     (8) Soma os valores de line e atribui para line_sum, com sum_values(line).
     (9) Se for a primeira iteração, define a line_sum como pattern.
     (10) Se line_sum for diferente de pattern, imprime -1, atribui False para maybe_has_pattern e para
     o loop com break.
     (11) Inicia um loop for percorrendo as n colunas. A cada repetição:
         (12) Obtem o valor da coluna e soma no índice respectivo em column_sum: column_sum[j] += int(line[j]).
         (13) Se i == j, soma o valor em main_diagonal_sum.
         (14) Se i + j == n - 1, soma o valor em secondary_diagonal_sum.
 (15) Se maybe_has_pattern for True, verifica se not has_pattern(column_sum, main_diagonal_sum, secondary_diagonal_sum, pattern) retorna True. Se sim,
 imprime -1.
 (16) Senão, imprime o pattern.
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

def has_pattern(column_sum, main_diagonal_sum, secondary_diagonal_sum, pattern):  # Define a função has_pattern
    """
        Função que recebe a soma das colunas e das diagonais e verifica se tem o padrão
        de soma.
        column_sum: lista de somas inteiras de colunas.
        main_diagonal_sum: soma da diagonal principal.
        secondary_diagonal_sum: soma da diagonal secundaria.
        pattern: inteiro representando o padrão de soma
        Retorna True se houver padrão em todas as somas e False caso contrário.
    """
    
    # Se a diagonal principal ou a secundária nao tem padrão
    if main_diagonal_sum != pattern or secondary_diagonal_sum != pattern:  
        return False  # Retorna False
    
    for i in range(len(column_sum)):  # Percorre os valores das colunas
        if column_sum[i] != pattern:  # Se a soma da coluna não for igual ao padrão
            return False  # Retorna False
    
    return True  # Retorna True, se todos tiverem padrão

n = int(input())  # Le a dimensão da matriz

line_sum = 0  # Soma da linha
main_diagonal_sum = 0  # Soma da diagonal principal
secondary_diagonal_sum = 0  # Soma da diagonal secundária
column_sum = [0] * n  # Soma das colunas

pattern = 0  # Padrão de soma
maybe_has_pattern = True  # Possibilidade de padrão

for i in range(n):  # Percorre as linhas da matriz
    line = input().split()  # Le os valores de uma linha, separados por espaços
    line_sum = sum_values(line)  # Soma os valores da linha
    
    if i == 0:  # Se for a primeira iteração
        pattern = line_sum  # Define a soma da linha como padrão
        
    if line_sum != pattern:  # Caso a soma da linha seja diferente do padrão
        print(-1)  # Imprime -1
        maybe_has_pattern = False  # Não há possibilidade de ter padrão
        break  # Para o loop
    
    for j in range(n):  # Percorre as colunas
        column_sum[j] += int(line[j])  # Soma o valor da coluna em column_sum[j]
        if i == j:  # Se for a diagonal principal
            main_diagonal_sum += int(line[j])  # Soma o valor em main_diagonal_sum
        if i + j == n - 1:  # Se for a diagonal secundária
            secondary_diagonal_sum += int(line[j])  # Soma o valor em secondary_diagonal_sum

if maybe_has_pattern:  # Se todas as linhas mantiveram padrão
    # Se não há padrão
    if not has_pattern(column_sum, main_diagonal_sum, secondary_diagonal_sum, pattern):
        print(-1)  # Imprime -1
    else:  # Senão
        print(pattern)  # Imprime o padrão identificado
        