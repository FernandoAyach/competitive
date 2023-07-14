# -*- coding: utf-8 -*-

'''
Resolução:
 (1) Inicia um loop while True infinito. A cada repetição:
     (2) Le o total de temporadas e a duração de cada capitulo, em uma mesma linha, separados por espaços, pelo input().split(),
     e atribui para as variáveis seasons e duration.
     (3) Se seasons == "-1", para o loop com break, pois acabaram as entradas.
     (4) Converte seasons para inteiro, pelo int(), e atualiza a variável.
     (5) Converte duration para inteiro, pelo int(), e atualiza a variável.
     (6) Le os capitulos, em uma mesma linha, separados por espaços, pelo input().split(), e atribui para chapters.
     (7) Inicia um loop for de intervalo [0, len(chapters)). A cada repetição:
         (8) Converte chapters[i] em inteiro, pelo int(), e atualiza o elemento.
     (9) Inicia uma variável repeat para armazenar a repetição de cada capitulo, começa com valor seasons.
     (10) Inicia uma variável total para armazenar a soma total de minutos, com valor 0.
     (12) Inicia um loop for de intervalo [0, seasons). A cada repetição:
         (13) Calcula chapters[i] * repeat * duration e soma em total.
         (14) Decresce em 1 repeat.
     (15) Imprime o total de minutos
'''

while True:  # Inicia um loop infinito
    
    # Le o total de temporadas e a duração de cada capitulo, em uma mesma linha, separados por espaços
    seasons, duration = input().split()
  
    if seasons == "-1":  # Se não houver mais entradas
        break  # Para o loop
    
    seasons = int(seasons)  # Converte seasons para inteiro
    duration = int(duration)  # Converte duration para inteiro

    chapters = input().split()  # Le os capitulos, em uma mesma linha, separados por espaços

    for i in range(len(chapters)):  # Percorre com um loop os capitulos
        chapters[i] = int(chapters[i])  # Converte cada um em inteiro

    repeat = seasons  # Repetições de cada capitulo
    total = 0  # Soma total  
    for i in range(seasons):  # Percorre todas as temporadas
        total += chapters[i] * repeat * duration  # Para cada capitulo, multiplica pela duração e repetição
        repeat -= 1  # Diminui o número de repetições

    print(total)  # Imprime o total de minutos
