# -*- coding: utf-8 -*-

'''
Coleta o valor do nome, do salário e das vendas feitas, respectivamente
em string, real e real.
Calcula o valor recebido total, que é a soma do salário fixo mais 15% das vendas.
Imprime na tela com 2 casas decimais de aproximação.
'''

name = input()  # Coleta o nome do vendedor
salary = float(input())  # Coleta o salário fixo do vendedor
sales = float(input())  # Coleta as vendas do vendedor

month_total = salary + (sales*0.15)  # Calcula o total a se receber

print('TOTAL = R$ {:.2f}'.format(month_total))  # Imprime resultado na tela com 2 casas decimais