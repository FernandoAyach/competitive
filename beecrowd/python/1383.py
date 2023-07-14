# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções read_sudoku, is_sudoku9x9, is_sudoku3x3 e verify_sudoku.
 (2) Le o número de casos de teste, converte em inteiro, e atribui para n.
 (3) Percorre um loop for n vezes. A cada repetição:
     (4) Le uma matriz 9x9 pela função read_sudoku e atribui para sudoku.
     (5) Imprime a instância respectiva.
     (6) Se for sudoku, pela função verify_sudoku, imprime SIM.
     (7) Caso contrário, imprime NAO.
     (8) Pula uma linha
'''   

def read_sudoku():  # Define a função read_sudoku
    """
        Função que le uma matriz 9x9 e a retorna.
    """
    
    sudoku = []  # Sudoku vazio
    
    for i in range(9):  # Percorre as linhas 
        line = [0] * 9  # Cria uma linha vazia
        line_input = input().split()  # Le uma linha
        for j in range(9):  # Percorre as colunas
            line[j] = int(line_input[j])  # Converte o valor em inteiro
        sudoku.append(line)  # Insere a linha na matriz
    return sudoku  # Retorna o sudoku

def is_sudoku9x9(sudoku):  # Define a função is_sudoku9x9
    """
        Função que recebe uma matriz 9x9 e retorna se é sudoku, sem analisar as submatrizes.
        sudoku: matriz 9x9 de inteiros.
        Retorna True se a matriz 9x9 é sudoku, sem analisar as submatrizes, e False caso contrário.
    """
    
    
    for i in range(9):  # Percorre as linhas da matriz
        used_1_to_9_number = [False] * 9  # Lista de números possíveis
        for j in range(9):  # Percorre as colunas da matriz
            if not used_1_to_9_number[sudoku[i][j] - 1]:  # Se for um número de 1 a 9 e não tiver sido usado
                used_1_to_9_number[sudoku[i][j] - 1] = True  # Marca-o como usado
            else:  # Senão
                return False  # Retorna que não é sudoku
            
    for j in range(9):  # Percorre as colunas da matriz
        used_1_to_9_number = [False] * 9 # Lista de números possíveis
        for i in range(9):  # Percorre as linhas da matriz
            if not used_1_to_9_number[sudoku[i][j] - 1]:  # Se for um número de 1 a 9 e não tiver sido usado
                used_1_to_9_number[sudoku[i][j] - 1] = True  # Marca-o como usado
            else:  # Senão
                return False  # Retorna que não é sudoku
    return True  # Retorna que é sudoku

def is_sudoku3x3(sudoku, start_line, finish_line, start_column, finish_column):  # Define a função is_sudoku3x3
    """
        Função que recebe as coordenadas de uma submatriz do sudoku e verifica se é sudoku.
        sudoku:
        start_line: inteiro que representa a linha de começo
        finish_line: inteiro que representa a linha de finalização
        start_column: inteiro que representa a coluna de começo
        finish_column: inteiro que representa a coluna de finalização
        Retorna True se for sudoku e False caso contrário.
    """
    
    used_1_to_9_number = [False] * 9  # Lista de números possíveis
    
    for i in range(start_line, finish_line + 1):  # Percorre as linhas da submatriz
        for j in range(start_column, finish_column + 1):  # Percorre as colunas da submatriz
            if not used_1_to_9_number[sudoku[i][j] - 1]:  # Se for um número de 1 a 9 e não tiver sido usado
                used_1_to_9_number[sudoku[i][j] - 1] = True  # Marca-o como usado
            else:  # Senão
                return False  # Retorna que não é sudoku
    return True  # Retorna que é sudoku
    
def verify_sudoku(sudoku):  # Define a função verify_sudoku
    """
        Função que recebe uma matriz 9x9 e verifica se é
        sudoku.
        sudoku: matriz 9x9 de inteiros.
        Retorna uma variável booleana que é True se for sudoku e não,
        caso contrário.
    """
    
    is_sudoku = is_sudoku9x9(sudoku)  # Verifica se é sudoku 9x9
    
    i = 0  # Iterador das linhas
    # Se tende a ser sudoku e a linha é i <= 6
    while is_sudoku and i <= 6:  
        j = 0  # Iterador das colunas
        
        # Se tende a ser sudoku e a coluna é j <= 6
        while is_sudoku and j <= 6:
            is_sudoku = is_sudoku3x3(sudoku, i, i + 2, j, j + 2)  # Verifica se é sudoku 3x3
            j += 3  # Passa para próxima coluna da submatriz
        i += 3  # Passa para próxima linha da submatriz
    return is_sudoku  # Retorna se é sudoku

n = int(input())  # Le o número de casos de teste

for i in range(n):  # Percorre os casos de teste
    sudoku = read_sudoku()  # Le uma matriz sudoku
    
    print("Instancia", i + 1)  # Imprime a instância respectiva

    if verify_sudoku(sudoku):  # Se for sudoku
        print("SIM")  # Imprime SIM
    else:  # Senão
        print("NAO")  # Imprime NAO
    print()  # Pula uma linha
      