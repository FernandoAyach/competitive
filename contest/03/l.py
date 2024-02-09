coeficientes1 = list(map(int, input().split()))
coeficientes2 = list(map(int, input().split()))

A1, B1, R1 = coeficientes1
A2, B2, R2 = coeficientes2

det_principal = A1 * B2 - A2 * B1
det_X = R1 * B2 - R2 * B1
det_Y = A1 * R2 - A2 * R1

if det_principal != 0:
    X = det_X / det_principal
    Y = det_Y / det_principal
    print("{:.2f} {:.2f}".format(X, Y))
else:
    print("sistema indeterminado")