# -*- coding: utf-8 -*-

'''
Coleta o número do funcionário, horas trabalhadas e ganho por hora,
respectivamente em inteiro, inteiro e real.
Calcula o valor do salário pelo produto das horas pelo ganho.
Imprime o número do funcionário e o salário, com duas casas decimais.
'''

workerNumber = int(input())  # Coleta o número do funcionário
workHours = int(input())  # Coleta horas trabalhadas
moneyPerHour = float(input())  # Coleta ganho por hora

salary = workHours * moneyPerHour  # Calcula o salário

print('NUMBER = {}'.format(workerNumber))  # Imprime o número do funcionário
print('SALARY = U$ {:.2f}'.format(salary))  # Imprime o salário, com 2 casas decimais
