# -*- coding: utf-8 -*-

'''
Coleta os 3 valores da peça 1 e da 2. Faz as respectivas conversões.
Para calcular o total a pagar, multiplica-se o valor unitário de cada peça
pela sua quantidade e, em seguida, soma os dois valores obtidos.
Imprime na tela o resultado com 2 casas decimais de aproximação.
'''

code1, quantity1, value1 = input().split()  # Coleta entradas da 1ª peça
quantity1 = int(quantity1)  # Converte quantidade da peça 1 para inteiro
value1 = float(value1)  # Converte valor da peça 1 para real

code2, quantity2, value2 = input().split() # Coleta entradas da 2ª peça
quantity2 = int(quantity2)  # Converte quantidade da peça 2 para inteiro
value2 = float(value2)  # Converte valor da peça 2 para real

total = (quantity1*value1) + (quantity2*value2)  # Calcula o total a se pagar

print('VALOR A PAGAR: R$ {:.2f}'.format(total))  # Imprime total na tela com aproximação de 2 casas decimais