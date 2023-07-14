"""
Resolução:
 (1) Define as funções is_possible_number, read_valid_matrix, is_pattern e verify_magic_square.
 (2) Le a dimensão da matriz, converte em inteiro e atribui para n.
 (3) Cria uma lista de booleanos com valor false de tamanho n**2 e atribui para used_numbers.
 (4) Le a matriz com read_valid_matrix e atribui para matrix.]
 (5) Se matrix == 0, imprime 0.
 (6) Senão, imprime o resultado de verify_magic_square.
"""

def is_possible_number(used_numbers, number):  # Define a função is_possible_number
    """
        Função que, dada uma uma lista de números possíveis e um número, verifica
        se ele é possivel na matriz.
        used_numbers: lista de booleanos de tamanho n**2.
        number: inteiro a ser analisado.
        Retorna False caso for invalido e True caso contrário.
    """
    
    # Se for menor que 1 ou maior que n**2
    if number < 1 or number > len(used_numbers):
        return False  # Retorna False
    
    # Se o número já não tiver sido usado
    if not used_numbers[number - 1]:
        used_numbers[number - 1] = True  # Marca-o como usado
        return True  # Retorna True
    return False  # Retorna False

def read_valid_matrix(used_numbers, n):  # Define a função read_valid_matrix
    """
        Função que recebe uma lista de números possíveis e a dimensão de uma
        matriz e a retorna com valores lidos, caso passar da validação dos números.
        Caso contrário, retorna 0.
        used_numbers: lista de booleanos de tamanho n**2.
        n: inteiro referente à dimensão da matriz.
        Retorna matriz com valores lidos, caso passar da validação dos números.
        Caso contrário, retorna 0.
    """
    
    matrix = []  # Inicia uma lista vazia
    
    for i in range(n):  # Percorre as linhas matriz
        line = input().split()  # Le os valores da linha
        line_int = [0] * n  # Cria um vetor de int de tamanho n
        
        for j in range(n):  # Percorre as colunas
            number = int(line[j])  # Converte o valor da linha para inteiro
            if not is_possible_number(used_numbers, number):  # Verifica se é um número invalido
                return 0  # Retorna 0
            
            line_int[j] = number  # Atribui o valor convertido para a linha de int
        matrix.append(line_int)  # Insere a linha na matriz
    return matrix  # Retorna a matriz

def is_pattern(pattern, number_sum):  # Define a função is_pattern
    """
        Função que recebe um padrão e uma soma e verifica se são iguais.
        pattern: inteiro referente ao padrão.
        number_sum: inteiro referente à soma.
        Retorna True se são iguais e False caso contrário;
    """
    # Retorna se a soma é igual ao padrão ou não
    return number_sum == pattern

def verify_magic_square(matrix, n):  # Define a função verify_magic_square
    """
        Função que recebe uma matriz e sua dimensão e verifica se é um quadrado
        mágico.
        matrix: matriz de tamanho nxn.
        n: inteiro referente à dimensão da matriz.
        Retorna a soma padrão do quadrado caso for mágico e 0 caso contrário.
    """
    
    pattern = 0  # Padrão
    c_sum = [0] * n  # Soma das colunas
    main_diagonal_sum = 0  # Soma das diagonais
    
    for i in range(n):  # Percorre as linhas
        line_sum = 0  # Soma da linha
        for j in range(n):  # Percorre as colunas
            line_sum += matrix[i][j]  # Soma o valor em line_sum
            c_sum[j] += matrix[i][j]  # Soma o valor em c_sum[j]
        
        if i == 0:  # Caso for a primeira iteração
            pattern = line_sum  # Define o padrão como a soma da linha
        
        # Se a soma da linha não respeitar o padrão
        if not is_pattern(pattern, line_sum):  
            return 0  # Retorna 0
        
        main_diagonal_sum += matrix[i][i]  # Soma o matrix[i][i] em main_diagonal_sum
    
    # Se a soma da diagonal não for padrão
    if not is_pattern(pattern, main_diagonal_sum):
        return 0  # Retorna 0
    else:  # Senão
        for i in range(n):  # Percorre as somas das colunas
            # Se a soma da coluna não for padrão
            if not is_pattern(pattern, c_sum[i]):
                return 0  # Retorna 0
    return pattern  # Retorna a soma padrão

n = int(input())  # Le a dimensão da matriz
used_numbers = [False] * (n**2)  # Lista de números já utilizados
matrix = read_valid_matrix(used_numbers, n)  # Le e verifica os números da matriz

if matrix == 0:  # Se a matriz for igual a 0
    print(0)  # Imprime 0
else:  # Senão
    print(verify_magic_square(matrix, n))  # Verifica e imprime a soma do quadrado
