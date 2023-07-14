total_table = 0  # Coleta o total de mesas
pattern_table = 0  # Coleta o total de mesas padrão
special_table = 0  # Coleta o total de mesas especias

while True:  # Inicia um loop infinito
    try:
        table_type = input()  # Tenta pegar um tipo de mesa, em uma linha
    except EOFError:  # Se não tiver mais entradas
        break  # Para o loop
    
    if table_type == 'padrão':  # Se for mesa padrão
        print('padrão')  # Imprime tipo padrão
        print('tampo madeira marrom')  # Imprime tampo madeira marrom
        print('saias do tampo madeira marrom')  # Imprime saias do tampo madeira marrom
        print('pernas madeira marrom')  # Imprime pernas madeira marrom
        pattern_table += 1  # Incrementa uma mesa padrão
    else:  # Senão, for alterada
        has_saias = True  # Tem saias
        
        tamp_material = 'madeira'  # define material do tampo padrão
        tamp_color = 'marrom'  # define cor do tampo padrão
        
        leg_material = 'madeira'  # define material da perna padrão
        leg_color = 'marrom'  # define material da perna padrão
        
        saia_material = 'madeira'  # define material da saia padrão
        saia_color = 'marrom'  # define material da saia padrão
        
        modifications = int(input())  # Coleta o número de modificações
        
        for i in range(modifications):  # Percorre a quantidade as modificações
            modification = input()  # Coleta uma modificação
            
            if modification == 'sem saias do tampo':  # Se for em saias do tampo
                has_saias = False  # Não tem saias
            else:
                component, quality, new = modification.split()
                
                if component == 'tampo':
                    
                    if quality == 'material':
                        tamp_material = new
                    else:
                        tamp_color = new
                
                if component == 'saias':
                    if quality == 'material':
                        saia_material = new
                    else:
                        saia_color = new
                
                if component == 'pernas':
                    if quality == 'material':
                            leg_material = new
                    else:
                        leg_color = new
        
        print('alterada')  # Imprime alterada
        print('tampo', tamp_material, tamp_color)  # Imprime as características do tampo
        if has_saias:  # Se tiver saias
            print('saias do tampo', saia_material, saia_color)  # Imprime as características da saia
        print('pernas', leg_material, leg_color)  # Imprime as características da perna
        
        # Se for uma mesa especial
        if tamp_material == 'aço' and tamp_color == 'cinza' and not has_saias and leg_material == 'ferro' and leg_color == 'preta':
            special_table += 1  # Incrementa special_table em 1
    total_table += 1  # Incrementa total_table em 1
    print()
print(total_table, pattern_table, special_table)  # Imprime todas as quantias
           
