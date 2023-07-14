while True:
    n_attackers, n_defenders = map(int, input().split())

    if n_attackers == 0 or n_defenders == 0:
        break
    
    attackers = list((map(int, input().split())))
    defenders = list((map(int, input().split())))

    attackers.sort()
    defenders.sort()
    no_impediment = True

    for attacker in attackers:

        if attacker < defenders[1]:
            print('Y')
            no_impediment = False
            break
        
    if no_impediment:
        print('N')       

    
