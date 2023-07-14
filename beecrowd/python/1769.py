# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Inicia um loop while infinito. A cada repetiçao:
     (2) Tenta ler os números de um CPF, na mesma linha, separado por "-", atribuindo para
     cpf, pelo input().split("-").
     (3) Se der EOFError, não há mais entradas, então para o loop com break.
     (4) Inicia uma variável cpf_1 para armazenar a primeira parte do CPF, separados por pontos, pelo
     cpf[0].split('.'), obtendo somente os números, em elementos de 3 em 3.
     (5) Usa o "".join(cpf_1) para juntar todos os números e atualiza cpf_1.
     (6) Cria uma lista cpf_numbers, com tamanho de cpf_1, para armazenar os valores de cpf_1 em forma
     de inteiro.
     (7) Cria um loop for de intervalo [0, len(cpf_1)). A cada repetição:
         (8) Converte cpf_1[i] em inteiro, pelo int(), e atribui para cpf_numbers[i].
     (9) Cria uma variável b1 armazenado o penúltimo valor do CPF, em inteiro.
     (10) Cria uma variável b2 armazenado o núltimo valor do CPF, em inteiro.
     (11) Cria uma variável sum_b1, com valor 0, para somar os números para encontrar b1.
     (12) Cria um variável j, com valor inicial 1, para atuar como multiplicador do elemento.
     (13) Cria um loop for de intervalo [0, len(cpf_numbers)). A cada repetição:
         (14) Calcula cpf_numbers[i] * j e soma em sum_b1.
         (15) Incrementa 1 em j.
     (16) Se o resto de sum_b1 % 11 for 10, cria uma variável expected_b1 com valor 0. Caso contrário, expected_b1 recebe
     sum_b1 % 11.
     (17) Repete o mesmo processo de cima (11 - 16), com variável de soma chamada sum_b2, j iniciando com 9 e decrescendo
     em 1 a cada repetição e a variável de resultado chamada expected_b2.
     (18) Se expected_b1 for igual a b1 e expected_b2 for igual a b2, imprime CPF valido.
     (19) Caso contrário, imprime imprime CPF invalido.
'''

while True:  # Loop infinito
    
    try:  # Tenta
        cpf = input().split("-")  # Le o CPF e separa em duas partes, divido pelo "-"
    except EOFError:  # Se não houver mais entradas
        break  # Para o loop

    cpf_1 = cpf[0].split('.')  # Obtem a somente os números da primeira parte do CPF
    cpf_1 = "".join(cpf_1)  # Junta os em uma string só, antes estavam 3 a 3
    
    cpf_numbers = [0] * len(cpf_1)  # Inicia uma lista para armazenar os números do CPF em inteiro
    
    for i in range(len(cpf_1)):  # Percorre cpf_1
        # Converte o elemento de cpf_1 em inteiro e insere na lista cpf_numbers
        cpf_numbers[i] = int(cpf_1[i])  
    
    b1 = int(cpf[1][0])  # Obtem o penúltimo número do CPF
    b2 = int(cpf[1][1])  # Obtem o último número do CPF
    
    # Inicia variável para somar os números para encontrar b1
    sum_b1 = 0  
    j = 1  # Multiplicador do elemento
    for i in range(len(cpf_numbers)):  # Percorre os elementos de cpf_numbers
        sum_b1 += cpf_numbers[i] * j  # Multiplica o elemento por seu indice e soma em sum_b1
        j += 1  # Incrementa o multiplicador
    
    if sum_b1 % 11 == 10:  # Se o resto for 10
        expected_b1 = 0  # o b1 esperado é 0
    else:  # Senão
        expected_b1 = sum_b1 % 11  # Obtem o resto da divisão por 11
    
    # Inicia variável para somar os números para encontrar b2
    sum_b2 = 0  
    j = 9  # Multiplicador do elemento
    for i in range(len(cpf_numbers)):  # Percorre os elementos de cpf_numbers
        sum_b2 += cpf_numbers[i] * j  # Multiplica o elemento pelo indice (decrescente) e soma em sum_b1
        j -= 1  # Decrementa o multiplicador
        
    if sum_b2 % 11 == 10:  # Se o resto for 10
        expected_b2 = 0  # o b2 esperado é 0
    else:  # Senão
         expected_b2 = sum_b2 % 11  # Obtem o resto da divisão por 11
    
    # Se os resultados esperados condizem com o número do CPF
    if expected_b1 == b1 and expected_b2 == b2:  
        print("CPF valido")  # Imprime que CPF valido
    else:  # Senão
        print("CPF invalido")   # Imprime que CPF invalido
            