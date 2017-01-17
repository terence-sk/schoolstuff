import math


def getValues(start, step, count):
    vals = []
    pom = start
    vals.append(start)
    for i in range(0, count):
        pom += step
        vals.append(pom)

    return vals


def scitajHodnotyFunkcie(hodnoty):
    suma = 0
    #x^2 - 5x
    for i in range(1, len(hodnoty)):
        suma += ((hodnoty[i]**2-5*hodnoty[i])+(hodnoty[i-1]**2-5*hodnoty[i-1]))/2
    return suma

interval_start = 6
interval_end = 10
num_intervals = 4
h = (interval_end - interval_start) / num_intervals
presnost = pow(10, -6)

xk0 = 0
xk1 = 1

while True:
    xk1 = h*scitajHodnotyFunkcie(getValues(interval_start, h, num_intervals))

    if abs(xk0 - xk1) <= presnost:
        break

    xk0 = xk1
    h /= 2
    num_intervals *= 2

print(xk1)
