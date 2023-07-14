# -*- coding: utf-8 -*-

'''
Coleta o valor do salário e converte para real.
Para o cálculo do imposto, fazem-se comparações para saber
a qual faixa o salário pertence, aplicando as taxas de acordo.
Em cada caso, aplica-se a taxa para cada segmentação do salário, ou seja, o salário
é decomposto e a diferentes taxas serão aplicadas para cada ordem de grandeza do valor.
Após isso, soma o valor total do imposto.
No caso de ser um salário menor ou igual a 2000, é isento de imposto.
Imprime o valor total do imposto de renda a ser pago, com duas casas decimais.
'''
salary = float(input())  # Coleta o valor do salário em real

tax = 0  # Inicia variável para taxa
if salary > 4500:  # Verifica se é maior que 4500
    amount_28 = salary - 4500  # Coleta o valor acima de 4500
    tax_28 = amount_28*0.28  # Aplica a taxa sobre o valor selecionado
    salary -= amount_28  # Retira o valor acima de 4500
    tax += tax_28  # Adiciona na taxa total
if salary > 3000: # Verifica se é maior que 3000
    amount_18 = salary - 3000  # Coleta o valor acima de 3000
    tax_18 = amount_18*0.18  # Aplica a taxa sobre o valor selecionado
    salary -= amount_18  # Retira o valor acima de 3000
    tax += tax_18  # Adiciona na taxa total
if salary > 2000:  # Verifica se é maior que 2000
    amount_8 = salary - 2000  # Coleta o valor acima de 2000
    tax_8 = amount_8*0.08  # Aplica a taxa sobre o valor selecionado
    tax += tax_8  # Adiciona na taxa total
        
if(tax == 0):  # Se a taxa for zero, quer dizer que o valor é menor que 2000
    print('Isento')  # Portanto é isento
else:  # Caso contrário, há taxa
    print('R$ {:.2f}'.format(tax))  # Imprime o valor com 2 casas decimais