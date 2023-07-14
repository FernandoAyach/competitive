# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta 3 valores na mesma linha, separados por espaços, pelo input().split(), e atribui para as
 variáveis v1, v2, v3.
 (2) Converte cada variável para número real, pelo float(), e atualiza sua respectiva variável.
 (3) Coleta 3 pesos na mesma linha, separados por espaços, pelo input().split(), e atribui para as
 variáveis p1, p2, p3.
 (4) Converte cada variável para número inteiro, pelo int(), e atualiza sua respectiva variável.
 
Desenvolvimento:
 (1) Ordena os 3 primeiros valores em ordem crescente, para isso, fazem-se 3 processos:
 Se o segundo valor for menor que o primeiro, troca os valores entre eles.
 Se o terceiro valor for menor que o primeiro, mesmo se tiver tido troca anteriormente, troca os valores
 entre eles.
 Por fim, se o terceiro valor for menor que o segundo valor, troca as variáveis.
 (2) Agora é necessário ordenar os pesos em ordem decrescente, para isso, faz o mesmo processo para colocar
 em ordem crescente, mas ao inves de comparar se um valor é menor que outro, verifica se ele é maior. Nesse caso,
 troca as variáveis.
 (3) Calcula a média ponderada dos valores, atribuindo o menor valor ao maior peso, e assim por diante. Atribui
 o resultado para a variável average.

Saída:
 (1) Imprime os valores ordenados crescentemente, com 3 casas decimais de aproximação, todos na mesma linha,
 separados por espaços.
 (2) Imprime os pesos ordenados decrescentemente, todos na mesma linha, separados por espaços.
 (3) Pula uma linha.
 (4) Mostra a média ponderada com aproximação de 3 casas decimais.
'''

v1, v2, v3 = input().split()
v1 = float(v1)
v2 = float(v2)
v3 = float(v3)

p1, p2, p3 = input().split()
p1 = int(p1)
p2 = int(p2)
p3 = int(p3)

# Ordenar valores em ordem crescente

if v2 < v1:  # Se v2 é menor que v1
    aux = v1  # Armazena valor de v1
    v1 = v2  # Atribui o valor de v2 em v1
    v2 = aux  # Atribui o valor de v1 em v2

if v3 < v1:  # Se v3 é menor que v1
    aux = v1  # Armazena valor de v1
    v1 = v3  # Atribui o valor de v3 em v1
    v3 = aux  # Atribui o valor de v1 em v3

if v3 < v2:  # Se v2 é menor que v2
    aux = v2  # Armazena o valor de v2
    v2 = v3  # Atribui o valor de v3 em v2
    v3 = aux  # Atribui o valor e v2 em v3
    
# Ordenar pesos em ordem decrescente

if p2 > p1:  # Se p2 é maior que p1
    aux = p1  # Armazena valor de p1
    p1 = p2  # Atribui o valor de p2 em p1
    p2 = aux  # Atribui o valor de p1 em p2

if p3 > p1:  # Se p3 é maior que p1
    aux = p1  # Armazena valor de p1
    p1 = p3  # Atribui o valor de p3 em p1
    p3 = aux  # Atribui o valor de p1 em p3

if p3 > p2:  # Se p3 é maior que p2
    aux = p2  # Armazena o valor de p2
    p2 = p3  # Atribui o valor de p3 em p2
    p3 = aux  # Atribui o valor e p2 em p3

average = (v1*p1 + v2*p2 + v3*p3) / (p1 + p2 + p3)

print('{:.3f} {:.3f} {:.3f}'.format(v1, v2, v3))
print('{} {} {}'.format(p1, p2, p3))
print()
print('{:.3f}'.format(average))