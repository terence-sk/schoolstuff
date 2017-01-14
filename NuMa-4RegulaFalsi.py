import math


def f(x):
    return x**3 - math.log(10-x, math.e)

a = 1.2
b = 1.3
pom = 1.2
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
