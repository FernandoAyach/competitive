# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções read_powered_matrix, fill_spaces, max_length_column e show_matrix.
 (2) Le o número de casos de teste, converte em inteiro, e atribui para n.
 (3) Cria um contador count com valor 0.
 (4) Cria um loop for que percorre n vezes. A cada repetição:
     (5) Le as dimensões da matriz, converte em inteiro, e atribui para d.
     (6) Le a matriz com valores ao quadrado e atribui para matrix.
     (7) Imprime o número do quadrado do Atrapalhilton.
     (8) Imprime a matriz com show_matrix.
     (9) Incrementa count em 1.
     (10) Pula uma linha em branco, se não for a última matriz
'''

def read_powered_matrix(d):  # Define a função read_sudoku
    """
        Função que recebe a dimensão de uma matriz quadrada, a cria, e a
        retorna com valores ao quadrado.
        d: inteiro referente as dimensões da matriz.
        Retorna a matriz com valores ao quadrado.
    """
    
    matrix = []  # Cria uma lista vazia
    for j in range(d):  # Percorre as linhas 
        line = [0] * d  # Cria uma linha vazia
        line_input = input().split()  # Le uma linha
        for w in range(d):  # Percorre as colunas
            line[w] = int(line_input[w]) ** 2  # Converte o valor em inteiro
        matrix.append(line)  # Insere a linha na matriz

    return matrix  # Retorna a matriz

def max_length_column(matrix, d):  # Define a função max_length_column
    """
        Função que calcula a largura de cada coluna de uma
        matriz de dimensão d.
        matriz: matriz de inteiros.
        d: dimensão da matriz.
        Retorna uma lista com a largura de cada coluna.
    """
    
    bigger_lengths_columns = [0]*d  # Lista de larguras das colunas
    
    for j in range(d):  # Percorre todas as colunas
        for i in range(d):  # Percorre todas as linhas
            if matrix[i][j] > bigger_lengths_columns[j]:  # Se o número for maior que a largura atual
                bigger_lengths_columns[j] = matrix[i][j]  # O número será o maior da coluna
    
    for i in range(d):  # Percorre a lista de larguras
        # Calcula a largura do maior número da coluna
        bigger_lengths_columns[i] = len(str(bigger_lengths_columns[i]))  
    return bigger_lengths_columns   # Retorna a lista de larguras 

def fill_spaces(n):  # Define a função fill_spaces
    """
        Função que imprime n espaços sem pular linha.
        n: inteiro referente ao número de espaços.
        Não há retorno
    """
    
    for i in range(n):  # Repete n vezes
        print(" ", end = "")  # Imprime um espaço
                
def show_matrix(matrix, d):  # Define a função show_bricks
    """
        Função que recebe uma matriz e sua dimensão e imprime
        os valores alinhados a direita e separados por espaços.
        matrix: matrix de inteiros.
        d: dimensão da matriz.
        Não há retorno.
    """
    
    bigger_columns = max_length_column(matrix, d)  # Alinhamento da coluna
    
    for i in range(d):  # Percorre todas as linhas
        for j in range(d - 1):  # Percorre até a penúltima linha
            number_length = len(str(matrix[i][j]))  # Calcula o tamanho do número
            # Calcula o número de espaços antes do número
            total_spaces = bigger_columns[j] - number_length  
            fill_spaces(total_spaces)  # Imprime os espaços
            print(matrix[i][j], end = " ")  # Imprime o número com espaço após o número
        
        number_spaces = len(str(matrix[i][d - 1]))  # Calcula o tamanho do último número
        # Calcula o número de espaços antes do número
        total_spaces = bigger_columns[d - 1] - number_spaces
        fill_spaces(total_spaces)  # Imprime os espaços
        print(matrix[i][d - 1])  # Imprime o último número sem espaço, pulando linha

n = int(input())  # Le o número de casos de teste
count = 0  # Contador de quadrados
for i in range(n):  # Percorre os casos de teste
    d = int(input())  # Le as dimensões da matriz
    
    matrix = read_powered_matrix(d)  # Le a matriz com valores ao quadrado
    
    print("Quadrado da matriz #{}:".format(4 + count))  # Imprime o número do quadrado
    show_matrix(matrix, d)  # Imprime o matriz formatada
    count += 1  # Atualiza o contador
    
    if i != n - 1:  # Se não for a ultima linha
        print()  # Pula uma linha
    