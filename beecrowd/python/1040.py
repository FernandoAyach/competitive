# -*- coding: utf-8 -*-

'''
Coleta as 4 notas da entrada e as converte em número real.
Calcula a média ponderada dessas notas, correspondente à primeira média.
Imprime o valor na tela.
Caso a nota for maior ou igual a 7, imprime que aluno foi aprovado.
Se for menor que 5, imprime que aluno foi reprovado.
Caso contrário, imprime que está em exame.
Estando em exame, coleta a nota do exame, converte em real e imprime na tela.
Calcula a média final, considerando a média anterior e a nota do exame.
Se for maior ou igual a 5, imprime que foi aprovado.
Caso contrário, aluno é reprovado.
No final, imprime o valor da média final.
'''

n1, n2, n3, n4 = input().split()  # Coleta os valores das notas
n1 = float(n1)  # Converte n1 em real
n2 = float(n2)  # Converte n2 em real
n3 = float(n3)  # Converte n3 em real
n4 = float(n4)  # Converte n4 em real

first_average = (n1*2 + n2*3 + n3*4 + n4) / 10  # Calcula a média ponderada

print('Media: {:.1f}'.format(first_average))  # Imprime a média na tela, com 1 casa decimal

if(first_average >= 7):  # Verifica se aluno foi aprovado
    print('Aluno aprovado.')  # Imprime que foi aprovado
elif(first_average < 5):  # Verifica se aluno foi reprovado
    print('Aluno reprovado.')  # Imprime que foi reprovado
else:  # Aluno está de exame
    print('Aluno em exame.')  # Imprime que está de exame
    
    exam_grade = float(input())  # Coleta o valor da nota do exame
    print('Nota do exame: {:.1f}'.format(exam_grade))  #Imprime o valor da nota, com 1 casa decimal
    
    final_average = (first_average + exam_grade) / 2  # Calcula a média final
    
    if(final_average >= 5):  # Verifica se foi aprovado
        print('Aluno aprovado.')  # Imprime que foi aprovado
    else:  # Aluno foi reprovado
        print('Aluno reprovado.')  # Imprime que foi reprovado
    print('Media final: {:.1f}'.format(final_average))  # Imprime valor da média final, com 1 casa decimal