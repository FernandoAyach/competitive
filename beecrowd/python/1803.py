# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define a função tochar().
 (2) Define uma matring vazia.
 (3) Inicia um for de intervalo [0, 4). A cada repetição:
     (4) Le uma linha e atribui para row.
     (5) Faz um append da linha em matring.
 (6) Inicia uma lista vazia sequences.
 (7) Inicia um for de intervalo [0, len(row) - 1]. A cada repetição:
     (8) Define uma string vazia string.
     (9) Inicia um for de intervalo [0, 4). A cada repetição:
         (10) Concatena o dígito de cada linha, da mesma coluna em string.
     (11) Faz um append da string em sequences, convertido em int.
 (12) Inicia um for de intervalo [1, len(sequences) - 1]. A cada repetição:
     (13) Converte a sequência em caracter pela função tochar()
     (14) Imprime o caracter sem pular linha.
 (15) Pula linha
'''

def tochar(sequence, i):  # Define a função tochar()
    """
        Função que recebe uma lista de sequências de números e retorna o caracter da matring.
        sequence: lista de números inteiros de 4 digitos.
        i: indice inteiro da coluna atual.
        Retorna o caracter resultante.
    """
    return chr((sequence[0] * sequences[i] + sequence[len(sequences) - 1]) % 257)  # Tranforma o digito em caracter

matring = []  # Define a matring vazia
for i in range(4):  # Percorre todas as linhas
    row = input()  # Obtem uma linha
 
    matring.append(row)  # Insere a linha  na matriz

sequences = []  # Define uma lista de sequências
for i in range(len(row)):  # Percorre todas as colunas
    
    string = ""  # Inicia uma string vazia
    for j in range(4):  # Percorre todas as linhas
        string += matring[j][i]  # Obtem o dígito de cada linha, da mesma coluna
    
    sequences.append(int(string))  # Insere o digito formado em sequences

# Percorre do segundo para o penultimo termo de sequences
for i in range(1, len(sequences) - 1):  
    char = tochar(sequences, i)  # Converte o digito em caracter
    print(char, end = "")  # Imprime o caracter sem pular linha
print()  # Pula linha
