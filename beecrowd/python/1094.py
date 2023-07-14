# -*- coding: utf-8 -*-

'''
Entrada + Desenvolvimento:
 (1) Coleta os casos de teste, em uma linha, converte para inteiro, e atribui para a variável n
 (2) Inicia variável total_dummies, com valor zero, para o total de cobaias
 (3) Inicia variável rabbits, com valor zero, para o total de coelhos
 (4) Inicia variável rats, com valor zero, para o total de ratos
 (4) Inicia variável frogs, com valor zero, para o total de sapos
 (5) Inicia um loop for de intervalo [0, 10). Para cada repetição:
 (6) Coleta o número de cobaias e seu tipo, em uma mesma linha, separados por espaços, pelo input().split() e atribui
 para as variáveis dummies e dummie_type.
 (7) Converte dummies para inteiro e atualiza a variável
 (8) Soma dummies à variável total_dummies
 (9) Se dummie_type for igual a C, é coelho e adiciona o número de cobaias para rabbits
 (9) Se dummie_type for igual a R, é rato e adiciona o número de cobaias para rats
 (9) Senão, é sapo e adiciona o número de cobaias para frogs

Saída:
 (1) Imprime o total de cobaias, em uma linha
 (2) Imprime o total de coelhos, em uma linha
 (3) Imprime o total de ratos, em uma linha
 (4) Imprime o total de sapos, em uma linha
 (5) Imprime o percetual de coelhos, em uma linha
 (6) Imprime o percetual de ratos, em uma linha
 (7) Imprime o percetual de sapos, em uma linha
'''

n = int(input())  # Coleta os casos de teste

total_dummies = 0  # Total de cobaias
rabbits = 0  # Total de coelhos
rats = 0  # Total de ratos
frogs = 0  # Total de sapos

for i in range(n):  # Itera num intervalo [0, 10)
    
    # Coleta o número de cobaias e seu tipo, na mesma linha, separado por espaços
    dummies, dummie_type = input().split()  
    dummies = int(dummies)  # Converte o número de cobaias para inteior
    
    total_dummies += dummies  # Soma o número de cobaias ao valor total
    
    if dummie_type == 'C':  # Se for coelho
        rabbits += dummies  # Soma o número de cobaias à rabbits
    elif dummie_type == 'R':  # Se for Rato
        rats += dummies  # Soma o número de cobaias à rats
    else:  # Senão, é sapo
        frogs += dummies  # Soma o número de cobaias à frogs
         
print('Total: {} cobaias'.format(total_dummies))  # Imprime o total de cobaias
print('Total de coelhos: {}'.format(rabbits))  # Imprime o total de coelhos
print('Total de ratos: {}'.format(rats))  # Imprime o total de ratos
print('Total de sapos: {}'.format(frogs))  # Imprime o total de sapos
print('Percentual de coelhos: {:.2f} %'.format((rabbits / total_dummies) * 100))  # Imprime o percentual de coelhos
print('Percentual de ratos: {:.2f} %'.format((rats / total_dummies) * 100))  # Imprime o percentual de ratos
print('Percentual de sapos: {:.2f} %'.format((frogs / total_dummies) * 100))  # Imprime o percentual de sapos
    