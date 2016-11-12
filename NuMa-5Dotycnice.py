import math


def f(x):
    return x - math.cos(x)


def f_first_deriv(x):
    return 1 + math.sin(x)


def f_second_deriv(x):
    return math.cos(x)


a = 0.7
b = 0.8

actual = 0.0
previous = 0.0
pom = 0.0

presnost = pow(10, -8)
iterations = 0

if f(a) * f_second_deriv(a) > 0:
    previous = a

elif f(b) * f_second_deriv(b) > 0:
    previous = b

while True:
    iterations += 1
    actual = previous-(f(previous) / f_first_deriv(previous))

    if abs(actual-previous) <= presnost:
        break
    else:
        pom = actual
        actual = previous
        previous = pom

print("Korenom je: ", "%.9f" % actual, " +- ", "%.8f" % presnost)
print("Trvalo nam to ", iterations, " iteracii")
