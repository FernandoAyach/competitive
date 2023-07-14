# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define a função is_consonant(char).
 (2) Le o número de casos de teste, converte em inteiro e atribui para n.
 (3) Inicia um loop for que repete n vezes. A cada repetição:
     (4) Le um nome e atribui para name.
     (5) Inicia um contador de palavras consecutivas cout com valor 0.
     (6) Inicia um loop que percorre o intervalo [0, len(name)]. A cada repetição:
         (7) Se for consoante: is_consonant(name[j]), adiciona o count em 1.
         (8) Senão, reinicia o count para 0.
         (9) Se count chegar a 3, imprime '<name> nao eh facil' e para o loop com break.
    (10) Se após do loop count for menor que 3, imprime '<name> eh facil'.
'''

def is_consonant(char):  # Define função is_consonant
    
    """
        Função que verifica se um caracter é uma consoante.
        char: string.
        Retorna True se for consoante e False se não for.
    """
    vowel = ['a', 'A', 'e', 'E', 'i', 'I', 'o', 'O','u', 'U']  # Lista de vogais
    
    for i in range(len(vowel)):  # Percorre o intervalo [0, len(not_consonant))
        if char == vowel[i]:  # Se for vogal
            return False  # Retorna False
    return True  # Retorna True


n = int(input())  # Coleta o número de casos de teste

for i in range(n):  # Percorre n vezes
    name = input()  # Coleta um nome
    
    count = 0  # Inicia um contador de palavras consecutivas
    for j in range(len(name)):  # Percorre os indices do nome
         
        if is_consonant(name[j]):  # Se for consoante
            count += 1  # Soma o contador em 1
        else:  # Senão
            count = 0  # Volta o contador para 0
        
        if count == 3:  # Se houver 3 consoantes consecutivas
            print(name, 'nao eh facil')  # Imprime que o nome não é fácil
            break  # Para o loop
    if count < 3:  # Se forem menos de 3 consoantes consecutivas
        print(name, 'eh facil')  # Imprime que o nome é fácil
    