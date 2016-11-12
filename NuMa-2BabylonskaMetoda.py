pociatocna_hodnota = 200
cislo_na_odmocnenie = 4843
pozadovana_presnost = pow(10, -2)

xk = 1/2*(pociatocna_hodnota + (cislo_na_odmocnenie / pociatocna_hodnota))
xk1 = 1/2*(xk + (cislo_na_odmocnenie / xk))

# lebo uz sme vyratali hodnoty xk a xk1, iteracii je 1
iteracii = 1

while abs(xk-xk1) > pozadovana_presnost or abs(xk-xk1) == 0:
    print("ITERACIA " + str(iteracii))
    print("XK = " + str(xk) + "\nXK+1 = " + str(xk1) + "\n")

    xk = xk1
    xk1 = 1/2*(xk1 + (cislo_na_odmocnenie / xk1))

    iteracii += 1

print("\nVYSLEDOK: " + str(xk1) + "\nPocet Iteracii: " + str(iteracii))
