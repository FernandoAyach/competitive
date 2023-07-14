# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Define função min_f(sequence).
 (2) Define função average_f(sequence).
 (3) Le o número de casos de teste, converte em inteiro, pelo int(), e atribui para n.
 (4) Inicia um loop for que repete n vezes. A cada repetição:
     (5) Le um nome e atribui para name.
     (6) Le as notas do aluno, na mesma linha, separadas por espaços, pelo input().split(), e atribui
     para grades.
     (7) Inicia uma variável average para armazenar a média, com valor inicial 0.
     (8) Cria um loop for que percorre o intervalo [0, len(grades)). A cada repetição:
         (9) Se houver 4 notas:
             (10) Calcula a menor nota, pelo min_f() e atribui para minor.
             (11) Cria uma lista updated_list para armazenar a lista atualizada.
             (12) Cria um loop for que percorre o intervalo [0, len(grades) - 1). A cada repetição:
                 (13) Se a nota do trabalho for maior que a nota atual e essa nota for a menor, insere a nota
                 do trabalho nessa nota.
                 (14) Concatena a nota em updated_list.
             (15) Atribui o valor de updated_list em grades.
     (16) Calcula a média das notas por average_f(grades) e atribui para average.
     (17) Imprime o nome do aluno e sua nota final, com uma casa decimal de aproximação            
'''

def min_f(sequence):  # Define a função min_f
    """
        Função que calcula a menor nota, sem considerar o trabalho.
        sequence: lista de notas float.
        Retorna a menor nota.
    """
    minor = sequence[0]  # Define uma referência de menor
       
    for i in range(1, len(sequence) - 1):  # Percorre a partir do termo 1 até o termo 2
        if sequence[i] < minor:  # Se a nota for menor que a menor
            minor = sequence[i]  # Esta será a menor
    return minor  # Retorna a menor nota

def average_f(sequence):  # Define a função average_f
    
    """
        Função que calcula a média das notas.
        sequence: lista de notas float.
        Retorna a média das notas.
    """
    
    n = len(sequence)  # Coleta o número de elementos da sequencia
    sum_n = 0  # Inicia variável para soma dos termos
    for j in range(n):  # Percorre todos os elementos
        sum_n += sequence[j]  # Soma os elementos em sum_n
        
    if n == 1:  # Se houver somente uma nota
        return sum_n / 2  # Retorna média: (n + 0) / 2
    return sum_n / n  # Retorna média

n = int(input())  # Le o número de casos de teste

for i in range(n):  # Loop que repete n vezes
    
    name = input()  # Le o nome do aluno
    # Le as notas do aluno, na mesma linha, separadas por espaços
    grades = input().split()  
    average = 0  # Cria variável para armazenar a média
    
    for j in range(len(grades)):  # Loop que percorre o intervalo [0, len(grades))
        grades[j] = float(grades[j])  # Converte a nota em float e atribui para a mesma posição
    
    if len(grades) == 4:  # Se forem 4 notas
        minor = min_f(grades)  # Calcula a menor nota (sem considerar o trabalho)
        updated_list = []  # Cria uma lista para inserir as novas notas
        
        for j in range(len(grades) - 1):  # Percorre todas as notas, menos o trabalho
            # Se o trabalho for maior que a nota e ela for a maior
            if grades[3] > grades[j] and grades[j] == minor:  
                grades[j] = grades[3]  # Insere a nota do trabalho nessa nota
            updated_list += [grades[j]]  # Insere a nota na lista atualizada
            
        grades = updated_list  # Atualiza a lista atual com a atualizada
         
    average = average_f(grades)  # Calcula a média das notas por average_f(grades)
    
    # Imprime o nome do aluno e sua nota final, com uma casa decimal de aproximação
    print("{}: {:.1f}".format(name, average))  
              