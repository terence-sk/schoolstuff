import math


def moja_funkcia(x):
    return x**3 - 12*x + 8

interval_a = 1
interval_b = 1.1
presnost = pow(10, -3)

interval_aprox = (interval_a + interval_b) / 2

if interval_a * interval_aprox < 0:
    interval_b = interval_aprox

while interval_b - interval_a > presnost:
    interval_aprox = (interval_a + interval_b) / 2

    if moja_funkcia(interval_a) * moja_funkcia(interval_aprox) < 0:
        interval_b = interval_aprox

    elif moja_funkcia(interval_b) * moja_funkcia(interval_aprox) < 0:
        interval_a = interval_aprox

print("a: ", interval_a)
print("b: ", interval_b)
print("a-b: ", interval_b-interval_a)
