def squareEachElemAndSum(input):
    suma = 0
    for i in range(0, len(input)):
        suma += input[i]**2
    return suma


def multiplyArraysAndSum(a1, a2):
    suma = 0
    for i in range(0, len(a1)):
        suma += a1[i]*a2[i]
    return suma

uzly = [-3,-1,1,3]
funkcne_h = [2,5,3,4]

pocet_uzly = len(uzly)
suma_uzly = sum(uzly)
suma_square_uzly = squareEachElemAndSum(uzly)

suma_funkcne_h = sum(funkcne_h)
suma_funkcne_x_uzly = multiplyArraysAndSum(uzly, funkcne_h)

print("c1 = " + str(suma_funkcne_h) + " / " + str(pocet_uzly + suma_uzly) + " = " + str(suma_funkcne_h / (pocet_uzly + suma_uzly)))
print("c2 = " + str(suma_funkcne_x_uzly) + " / " + str(suma_uzly + suma_square_uzly) + " = " + str(suma_funkcne_x_uzly / (suma_uzly + suma_square_uzly)))
print(str(suma_square_uzly) + "c1 + " + str(suma_uzly) + "c2" + " = " + str(suma_funkcne_x_uzly))
print(str(suma_uzly) + "c1 + " + str(pocet_uzly)+"c2" + " = " + str(suma_funkcne_h))