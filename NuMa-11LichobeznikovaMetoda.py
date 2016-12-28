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
    suma += math.e**(hodnoty[0])

    for i in range(1, len(hodnoty)-1):
        suma += 2* (math.e**(hodnoty[i]))

    suma += math.e**(hodnoty[len(hodnoty)-1])
    return suma

interval_start = -1
interval_end = 1
num_intervals = 4
h = (interval_end - interval_start) / num_intervals

print( (h/2 ) * scitajHodnotyFunkcie(getValues(interval_start, h, num_intervals)))

