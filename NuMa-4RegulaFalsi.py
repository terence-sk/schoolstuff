import math


def f(x):
    return math.sqrt(x) - math.cos(x)

a = 0.7
b = 0.8
pom = 0.7
presnost = pow(10, -5)

while True:

    x = a - (((b - a) / (f(b) - f(a))) * f(a))

    if f(a) * f(x) < 0:
        b = x

    elif f(b) * f(x) < 0:
        a = x

    if abs(x-pom) <= presnost:
        break

    pom = x

print("Korenom je: ", x, " +- ", "%.5f" % presnost)
