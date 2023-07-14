# -*- coding: utf-8 -*-

'''
Entrada:
 (1) Coleta 3 cores na mesma linha, separados por espaços, pelo input().split() e atribui
 para as variáveis c1, c2, c3.

Desenvolvimento + Saída:
 (1) Inicia variáveis booleanas para cada cor primária e secundárias, todas iniciadas com
 o valor falso. As variáveis primárias são blue, yellow e red. Já as secundárias são green, purple,
 orange.
 (2) Para cada cor, será verificada qual é a cor correspondente. No caso de ser a determinada cor, atualiza
 o valor da variável booelana respectiva para True, indicando a existência da cor. O padrão de comparação é o seguinte:
 Se for igual a azul, blue recebe True.
 Se for igual a amarela, yellow recebe True.
 Se for igual a vermelha, red recebe True.
 Se for igual a verde, green recebe True.
 Se for igual a roxa, purple recebe True.
 Senão, orange recebe True.
 Ressaltando, o procedimento é feito para cada variável de cor.
 (3) Se houver azul e amarelo e verde, imprime Azul e Amarela geraram Verde!.
 (4) Se houver azul e vermelho e roxa, Azul e Vermelha geraram Roxa!.
 (5) Se houver amarela e vermelha e laranja, imprime Amarela e Vermelha geraram Laranja!.
 (6) Caso contrário, imprime 'Não há casamento adequado das cores!'
'''

c1, c2, c3 = input().split()  # Coleta 3 cores, na mesma linha, separadas por espaços

blue = False  # Não há azul
yellow = False  # Não há amarela
red = False  # Não há vermelha
green = False  # Não há verde
purple = False  # Não há roxa
orange = False  # Não há laranja

if c1 == 'azul':  # se c1 é azul
    blue = True  # Tem azul
elif c1 == 'amarela': # se c1 é amarela
    yellow = True  # Tem amarela
elif c1 == 'vermelha': # se c1 é vermelha
    red = True  # Tem vermelha
elif c1 == 'verde': # se c1 é verde
    green = True  # Tem verde
elif c1 == 'roxa': # se c1 é roxa
    purple = True  # Tem roxa
else: # senão, c1 é laranja
    orange = True  # Tem laranja

if c2 == 'azul':  # se c2 é azul
    blue = True  # Tem azul
elif c2 == 'amarela': # se c2 é amarela
    yellow = True  # Tem amarela
elif c2 == 'vermelha': # se c2 é vermelha
    red = True  # Tem vermelha
elif c2 == 'verde': # se c2 é verde
    green = True  # Tem verde
elif c2 == 'roxa': # se c2 é roxa
    purple = True  # Tem roxa
else: # senão, c2 é laranja
    orange = True  # Tem laranja

if c3 == 'azul':  # se c3 é azul
    blue = True  # Tem azul
elif c3 == 'amarela': # se c3 é amarela
    yellow = True  # Tem amarela
elif c3 == 'vermelha': # se c3 é vermelha
    red = True  # Tem vermelha
elif c3 == 'verde': # se c3 é verde
    green = True  # Tem verde
elif c3 == 'roxa': # se c3 é roxa
    purple = True  # Tem roxa
else: # senão, c3 é laranja
    orange = True  # Tem laranja

if blue and yellow and green:  # se as cores são azul, amarela e verde
    print('Azul e Amarela geraram Verde!')  # Mostra resultado
elif blue and red and purple:  # se as cores são azul, vermelha e roxa
    print('Azul e Vermelha geraram Roxa!')  # Mostra resultado
elif yellow and red and orange:  # se as cores são amarela, vermelha e laranja
    print('Amarela e Vermelha geraram Laranja!')  # Mostra resultado
else: # senão, não é um casamento adequado
    print('Não há casamento adequado das cores!')  # Mostra resultado