import math


def f(x):
    return x**3 - math.log(10-x, math.e)


def f_first_deriv(x):
    return 3*x**2+(1/10-x)


def f_second_deriv(x):
    return 6*x+(1/(10-x)**2)


a = 1.25
b = 1.3

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
