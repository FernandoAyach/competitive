# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções read_matrix e print_board.
 (2) Inicia um loop while infinito. A cada repetição:
     (3) Tenta ler as linhas e colunas da matriz, na mesma linha, separados por espaços,
     pelo input().split(), e atribuir para m e n.
     (4) Se der EOFError e não houver mais entradas, para o loop com break.
     (5) Converte m para int e atualiza a variável.
     (6) Converte n para int e atualiza a variável.
     (7) Le a matriz pelo read_matrix(m, n) e atribui para board.
     (8) Imprime o tabuleiro pelo print_board(board).
'''

def read_matrix(m, n):  # Define a função read_matrix
    """
        Função que recebe linhas e colunas e le os valores da matriz.
        m: inteiro referente ao número de linhas.
        n: inteiro referente ao número de colunas.
        Retorna a matrix lida.
    """
    
    matrix = []  # Inicia uma matriz vazia
    for i in range(m):  # Percorre as linhas
        line = input().split()  # Le os valores da linha, separados por espaços
        matrix.append(line)  # Insere a linha na matriz
    return matrix  # Retorna a matriz

def print_board(board):  # Define a função create_board
    """
        Função que recebe uma matriz e imprime na tela o tabuleiro de PãodeQuejoSweeper.
        board: matriz de strings.
        Não há retorno.
    """
    
    for i in range(m):  # Percorre as linhas da matriz
        line = ""  # Inicia uma string vazia para a nova linha do tabuleiro
        
        for j in range(n):  # Percorre as colunas
           
            if board[i][j] == "1":  # Se o valor for 1
                line += "9"  # Concatena 9 na linha nova
            else:  # Senão
                 cheese_bun = 0  # Contador de pão de queijo
                 
                 # Se existe coluna à direita e tem pão de queijo
                 if j + 1 < n and board[i][j + 1] == "1":  
                     cheese_bun += 1  # Conta um pão de queijo
                 # Se existe coluna à esquerda e tem pão de queijo
                 if j - 1 >= 0 and board[i][j - 1] == "1":
                     cheese_bun += 1  # Conta um pão de queijo
                 # Se existe linha abaixo e tem pão de queijo
                 if i + 1 < m and board[i + 1][j] == "1":
                     cheese_bun += 1  # Conta um pão de queijo
                 # Se existe linha acima e tem pão de queijo
                 if i - 1 >= 0 and board[i - 1][j] == "1":
                    cheese_bun += 1  # Conta um pão de queijo
                 
                 # Concatena o número de pães de queijo, em string, em line
                 line += str(cheese_bun)  
        print(line)  # Imprime a linha

while True:  # Loop infinito
    
    try:  # Tenta
        # Le as linhas e colunas da matriz, na mesma linha, separados por espaços
        m, n = input().split()
    except EOFError:  # Se não houver mais entradas
        break  # Para o loop
 
    m = int(m)  # Converte m em inteiro
    n = int(n)  # Converte n em inteiro

    board = read_matrix(m, n)  # Le a matriz
    print_board(board)  # Imprime o tabuleiro
