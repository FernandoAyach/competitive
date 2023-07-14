# -*- coding: utf-8 -*-

'''
Coleta as tres informações do animal: formação óssea, classe e dieta.
Em seguida, ocorrem comparações afunilando o tipo de animal com base em suas características.
São feitas primeiro comparações da formação óssea, depois classe e por último dieta.
Se for vertebrado, ave e carnivoro, é águia.
Se for vertebrado, ave e não carnivoro, é pomba.
Se for vertebrado, não for ave e for onivoro, é homem.
Se for vertebrado, não for ave e não for onivoro, é vaca.
Se for invertebrado, for inseto e hematofago, é pulga.
Se for invertebrado, for inseto e não hematofago, é lagarta.
Se for invertebrado, não for inseto e for hematofago, é sanguessuga.
Se for invertebrado, não for inseto e não for hematofago, é minhoca.
Em cada caso, imprime o nome do animal na tela. 
'''

#Coleta informação óssea
boneFormation = input()
#Coleta a classe do animal
animalClass = input()
#Coleta a dieta do animal
diet = input()

#Verifica se é invertebrado
if(boneFormation == 'vertebrado'):
    
    #Verifica se é ave
    if(animalClass == 'ave'):
        
        #Verifica se é carnívoro
        if(diet == 'carnivoro'):
            #O animal é uma aguia, imprime na tela
            print('aguia')
        #Se não for carnívoro, é onívoro
        else:
            #O animal é uma pomba, imprime na tela
            print('pomba')
            
    #Se não for ave, é mamífero    
    else:
        #Verifica se é onivoro
        if(diet == 'onivoro'):
            #O animal é um homem, imprime na tela
            print('homem')
        #Se não for onivoro, é herbivoro
        else:
            #O animal é uma vaca, imprime na tela
            print('vaca')
#Se não for vertebrado, é invertebrado
else:
    #Verifica se é inseto
    if(animalClass == 'inseto'):
        
        #Verifica se é hematofago
        if(diet == 'hematofago'):
            #O animal é uma pulga, imprime na tela
            print('pulga')
        #Se não for hematofago, é herbivoro
        else:
            #O animal é uma lagarta, imprime na tela
            print('lagarta')
    #Se não for inseto, é anelideo    
    else:
        #Verifica se é hematofago
        if(diet == 'hematofago'):
            #O animal é uma sanguessuga, imprime na tela
            print('sanguessuga')
        #Se não for hematofago, é onivoro
        else:
            #O animal é uma minhoca, imprime na tela
            print('minhoca')