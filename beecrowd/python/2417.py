c_victories, c_draws, c_gols, f_victories, f_draws, f_gols = map(int, input().split())

if c_victories * 3 + c_draws > f_victories * 3 + f_draws:
    print('C')
elif f_victories * 3 + f_draws > c_victories * 3 + c_draws:
    print('F')
else:

    if c_gols > f_gols:
        print('C')
    elif f_gols > c_gols:
        print('F')
    else:
        print('=')