# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define as funções convert e play.
 (2) Cria a matriz game com valores 0, -1 e 1, representado, de acordo com a coordenada, se
 empatou, rajesh ganhou ou sheldon ganhou, respectivamente.
 (3) Le o número de linhas n, em inteiro.
 (4) Inicia o jogo com play()
'''

def convert(bet):  # Define a função convert
    """
        Função que converte a string em uma coordenada
        da matriz game.
        bet: string (spock, tesoura, papel, pedra ou lagarto).
        Retorna um número de 0 a 4, dependendo da resposta.
    """
    
    if bet == "spock":  # Se for spock
        return 0  # Retorna 0
    if bet == "tesoura":  # Se for tesoura
        return 1  # Retorna 1
    if bet == "papel":  # Se for papel
        return 2  # Retorna 2
    if bet == "pedra":  # Se for pedra
        return 3  # Retorna 3
    return 4  # Retorna 4

def play(n):  # Define a função play
    """
        Função que recebe um número de linhas, le 2 entradas
        do jogo e diz quem é o vencedor: rajesh ou sheldon.
        n: inteiro referente às linhas.
        Não há retorno
    """
    
    for i in range(n):  # Percorre as linhas
        # Le as entradas de rajesh e sheldon, na mesma linha, separados por espaços
        rajesh, sheldon = input().split()  
        rajesh = convert(rajesh)  # Converte rajesh para número
        sheldon = convert(sheldon)  # Converte sheldon para número
        
        winner = game[sheldon][rajesh]  # Obtem o vencedor
        
        if winner == -1:  # Rajesh ganhou
            print("rajesh")  # Imprime rajesh
        elif winner == 1:  # Sheldon ganhou
            print("sheldon")  # Imprime sheldon
        else:  # Senão
            print("empate")  # Imprime empate

# Determina os vencedores do jogo
game = [[0, 1, -1, 1, -1],[-1, 0, 1, -1, 1],[1, -1, 0, 1, -1],[-1, 1, -1, 0, 1], [1, -1, 1, -1, 0]]
n = int(input())  # Le o número de linhas da matriz
play(n)  # Começa o jogo
