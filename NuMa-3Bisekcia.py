import math


def moja_funkcia(x):
    return x - math.cos(x)

interval_a = 0.7
interval_b = 0.8
presnost = pow(10, -2)

interval_aprox = (interval_a + interval_b) / 2

if interval_a * interval_aprox < 0:
    interval_b = interval_aprox

while interval_b - interval_a > presnost:
    interval_aprox = (interval_a + interval_b) / 2

    if moja_funkcia(interval_a) * moja_funkcia(interval_aprox) < 0:
        interval_b = interval_aprox

    elif moja_funkcia(interval_b) * moja_funkcia(interval_aprox) < 0:
        interval_a = interval_aprox

print(interval_a)
print(interval_b)
print(interval_b-interval_a)
