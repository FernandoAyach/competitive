# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta 3 números e 2 operadores, na mesma linha, separados por espaços, pelo input().split(). Atribui os 3 valores,
 respectivamente, para n1, n2 e n3. Atribui os 2 operadores para op1 e op2.
 (2) Converte os números para real, usando o float(), e atualiza suas respectivas variáveis.
 (3) Cria constantes DIVISION, MULTIPLICATION, SUM e SUBTRACTION para representar os símbolos /, *, + e -.
 
Desenvolvimento + Saída:
 (1) Se houver uma divisão envolvendo 0 no cálculo, não é possível resolver a conta e imprime
 Cálculo impossível!.
 (2) Se forem operadores iguais, verifica qual é o operador e faz o cálculo só aplicando
 a ordem natural dos números, utilizando o mesmo operador. Imprime o resultado na tela, com 2 casas decimais.
 (3) No caso anterior, verifica-se o operador comparando com o operador com as constantes DIVISION, MULTIPLICATION, SUM e SUBTRACTION.
 (4) Senão for nenhum dos casos acima, são operadores diferentes, portanto, serão analisados todos os
 casos possíveis, utilizando o método de comparação já usado anteriormente. Para cada caso, calcula o resultado da conta,
 respeitando a precedência. Os casos analisados são: 
 Divisão e multiplicação 
 Multiplicação e divisão 
 Soma e subtração 
 Subtração e soma 
 Multiplicação e soma  
 Multiplicação e subtração 
 Divisão e soma 
 Divisão e subtração 
 Soma e multiplicação
 Soma e divisão
 Subtração e multiplicação
 Subtração e divisão
 Para cada caso, imprime o resultado da conta na tela, com 2 casas decimais.
'''

n1, op1, n2, op2, n3 = input().split()  # Coleta 3 números e 2 operadores
n1 = float(n1)  # Converte n1 para real
n2 = float(n2)  # Converte n2 para real
n3 = float(n3)  # Converte n3 para real

DIVISION = '/'
MULTIPLICATION = '*'
SUM = '+'
SUBTRACTION = '-'

# Se tem divisão envolvendo zero
if  op1 == DIVISION and n2 == 0 \
    or op1 == DIVISION and n1 == 0 \
    or op2 == DIVISION and n2 == 0 \
    or op2 == DIVISION and n3 == 0:
    print('Cálculo impossível!')  # Imprime cálculo impossível
elif op1 == op2:  # Se operadores são os mesmos
    if op1 == SUM:  # Se é soma
        print('{:.2f}'.format(n1 + n2 + n3))  # Mostra a soma de todos os números, com 2 casas decimais
    elif op1 == SUBTRACTION:  # Se é subtração
        print('{:.2f}'.format(n1 - n2 - n3))  # Mostra a subtração de todos os números, com 2 casas decimais
    elif op1 == MULTIPLICATION:  # Se é mulitiplicação
        print('{:.2f}'.format(n1 * n2 * n3))  # Mostra a mulitiplicação de todos os números, com 2 casas decimais
    else:  # Senão, é divisão
        print('{:.2f}'.format(n1 / n2 / n3))  # Mostra a divisão de todos os números, com 2 casas decimais
else:  # São operadores diferentes
    if op1 == DIVISION and op2 == MULTIPLICATION:  # se é divisão e multiplicação
        print('{:.2f}'.format(n1 / n2 * n3))  # Mostra resultado na tela
    elif op1 == DIVISION and op2 == SUM:  # se é divisão e soma
        print('{:.2f}'.format(n1 / n2 + n3))  # Mostra resultado na tela
    elif op1 == DIVISION and op2 == SUBTRACTION:  # se é divisão e subtração
        print('{:.2f}'.format(n1 / n2 - n3))  # Mostra resultado na tela
    elif op1 == MULTIPLICATION and op2 == SUBTRACTION:  # se é multiplicação e subtração
        print('{:.2f}'.format(n1 * n2 - n3))  # Mostra resultado na tela
    elif op1 == MULTIPLICATION and op2 == SUM:  # se é multiplicação e soma
        print('{:.2f}'.format(n1 * n2 + n3))  # Mostra resultado na tela
    elif op1 == MULTIPLICATION and op2 == DIVISION:  # se é multiplicação e divisão
        print('{:.2f}'.format(n1 * n2 / n3))  # Mostra resultado na tela
    elif op1 == SUM and op2 == SUBTRACTION:  # se é soma e subtração
        print('{:.2f}'.format(n1 + n2 - n3))  # Mostra resultado na tela
    elif op1 == SUM and op2 == MULTIPLICATION:  # se é soma e multiplicação
        print('{:.2f}'.format(n1 + n2 * n3))  # Mostra resultado na tela
    elif op1 == SUM and op2 == DIVISION:  # se é soma e divisão
        print('{:.2f}'.format(n1 + n2 / n3))  # Mostra resultado na tela
    elif op1 == SUBTRACTION and op2 == SUM:  # se é subtração e soma
        print('{:.2f}'.format(n1 - n2 + n3))  # Mostra resultado na tela
    elif op1 == SUBTRACTION and op2 == MULTIPLICATION:  # se é subtração e multiplicação
        print('{:.2f}'.format(n1 - n2 * n3))  # Mostra resultado na tela
    else:  # se é subtração e divisão
        print('{:.2f}'.format(n1 - n2 / n3))  # Mostra resultado na tela
    
    
    
    
    