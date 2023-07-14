# -*- coding: utf-8 -*-

'''
Coleta o valor do antigo salário e converte em real.
Inicia variáveis do novo salário, reajuste e porcentagem de reajuste.
Se o salário for acima de 2000, receberá 4% de reajuste, atualiza as variáveis de acordo.
Senão se o salário for acima de 1200, receberá 7% de reajuste, atualiza as variáveis de acordo.
Senão se o salário for acima de 800, receberá 10% de reajuste, atualiza as variáveis de acordo.
Senão se o salário for acima de 400, receberá 12% de reajuste, atualiza as variáveis de acordo.
Senão o salário receberá 15% de reajuste, atualiza as variáveis de acordo.
Imprime o novo salário, reajuste ganho e reajuste em porcentagem.
'''

old_salary = float(input())  # Coleta o antigo salário, em real

new_salary = 0  # Inicia variável de novo salário
reajust = 0  # Inicia variável de reajuste
reajust_percentage = ''  # Inicia variável de reajuste em porcentagem

if(old_salary > 2000):  # Verifica se salário é acima de 2000
    reajust_percentage = '4 %'  # Reajuste de 4 %
    reajust = old_salary * 0.04  # Calcula o valor do reajuste
    new_salary = old_salary * 1.04  # Calcula o novo salário
elif(old_salary > 1200):  # Senão se o salário for acima de 1200
    reajust_percentage = '7 %'  # Reajuste de 7 %
    reajust = old_salary * 0.07  # Calcula o valor do reajuste
    new_salary = old_salary * 1.07
elif(old_salary > 800):  # Senão se o salário for acima de 800
    reajust_percentage = '10 %'  # Reajuste de 10 %
    reajust = old_salary * 0.1  # Calcula o valor do reajuste
    new_salary = old_salary * 1.1  # Calcula o novo salário
elif(old_salary > 400):  # Senão se o salário for acima de 400
    reajust_percentage = '12 %'  # Reajuste de 12 %
    reajust = old_salary * 0.12  # Calcula o valor do reajuste
    new_salary = old_salary * 1.12  # Calcula o novo salário
else:  # Senão, o salário é menor que 400 
    reajust_percentage = '15 %'  # Reajuste de 15 %
    reajust = old_salary * 0.15  # Calcula o valor do reajuste
    new_salary = old_salary * 1.15  # Calcula o novo salário

print('Novo salario: {:.2f}'.format(new_salary))  # Imprime novo salário na tela, com 2 casas decimais
print('Reajuste ganho: {:.2f}'.format(reajust))  # Imprime o reajuste na tela, com 2 casas decimais
print('Em percentual:', reajust_percentage)  # Imprime o reajuste em porcentagem na tela