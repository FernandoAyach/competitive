# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta o total de estudantes, litros por rodada e a quantidade
 de café por estudante (em ml), na mesma linha, separado por espaços,
 a partir do input().split(). Armazena, respectivamente, nas variáveis
 total_students, liters_per_round e coffee_per_student.
 (2) Converte cada valor em inteiro e atualiza sua respectiva variável.
 
Desenvolvimento:
 (1) Primeiro, calcula-se a quantidade mínima de litros a ser feita, para isso,
 multiplica o total de estudantes pela quantidade que cada um bebe, convertida em litro, e
 atribui para a variável min_liters.
 (2) Em seguida, calcula a quantidade de rodadas de café a serem feitas, para isso, divide o total
 de litros pela quantidade de cada rodada. Deve se arredondar para cima, pois, em caso de números não inteiros,
 deve-se realizar mais uma rodada. Detalhe que isso só funciona porque os alunos não se importam se a quantidade de café
 for maior que a mínima.

Saída:
 (1) Por fim, imprime na tela a quantidade a ser feita multiplicando o total de rodadas
 pela quantidade de litros de cada uma.
'''
import math  # Importa o módulo math

# Coleta o total de estudantes, litros por rodada e ml por estudante, na mesma linha, separado por espaços
total_students, liters_per_round, coffee_per_student = input().split()  
total_students = int(total_students)  # Converte total de estudantes para inteiro
liters_per_round = int(liters_per_round)  # Converte litros por rodada para inteiro
coffee_per_student = int(coffee_per_student)  # Converte ml por estudante para inteiro

min_liters = total_students * (coffee_per_student / 1000)  # Calcula a quantidade mínima de café
 
coffee_rounds = math.ceil(min_liters / liters_per_round)  # Calcula quantos rodadas de café são necessárias, com arredondamento para cima

print(coffee_rounds * liters_per_round)  # Imprime a quantidade total na tela