# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Le uma letra e atribui para letter.
 (2) Le um texto, pelo input(), e obtem somente as palavras, a partir split(), e atribui para
 a lista text.
 (3) Inicia um contador de palavras word_count, com valor 0, para contar as palavras que contem a letra.
 (4) Cria um loop for que percorre todas as palavras em text. A cada palavra:
     (5) Se letter in word, incrementa word_count em 1.
 (6) Se word_count == 0, então a porcentagem é 0, imprime 0.0 na tela.
 (7) Senão, calcula a porcentagem de palavras que contem a letra por (word_count / len(text)) * 100 e imprime
 na tela o resultado com uma casa decimal.
'''

letter = input()  # Le uma letra
text = input().split()  # Le um texto, em uma linha, e obtem somente as palavras, ignorando os espaços

word_count = 0  # Contador de palavras que contem a letra

for word in text:  # Inicia um loop que percorre as palavras de text
    if letter in word:  # Se word contém letter
        word_count += 1  # Incrementa word_count em 1

if word_count == 0:  # Se não havia palavras que tivesse a letra
    print("0.0")  # Imprime porcentagem 0, com uma casa decimal
else:  # Senão
    result = (word_count / len(text)) * 100  # Calcula a porcentagem
    print("{:.1f}".format(result))  # Imprime o resultado com uma casa decimal