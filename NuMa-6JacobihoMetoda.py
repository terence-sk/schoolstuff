def rownorm(matrix):
    sums = []
    rowSum = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            rowSum += abs(matrix[i][j])
        sums.append(rowSum)
        rowSum = 0

    return max(sums)


def colnorm(matrix):
    sums = []
    colSum = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            colSum += abs(matrix[j][i])
        sums.append(colSum)
        colSum = 0

    return max(sums)


def frobnorm(matrix):
    total = 0

    for i in range(0, len(matrix)):
        for j in range(0, len(matrix)):
            total += pow(matrix[i][j], 2)

    return pow(total, 1/2)


def computereceq(equation, result, guess, i, signs):
    eq = equation[:]
    sg = signs[:]
    gs = guess[:]
    divide = 1/eq[i]
    eq.pop(i)
    sg.pop(i)
    gs.pop(i)
    part_result = 0

    for x in range(0, len(eq)):
        if sg[x] == '-':
            eq[x] = -eq[x]
        if sg[x] == '+':
            eq[x] = abs(eq[x])
        part_result += eq[x]*gs[x]

    return divide*(result+part_result)

accuracy = pow(10, -6)

testmatrix = [[7, 2, -3],
              [1, 10, 2],
              [4, 3, -8]
              ]

# TODO metodu na generovanie tohto pola z testmatrix
signs = [['-', '-', '+'],
         ['-', '-', '-'],
         ['-', '-', '+']
         ]
eqresultsmatrix = [14, 20, 16]
guessmatrix = [0, 0, 0]

#print(rownorm(testmatrix), colnorm(testmatrix), frobnorm(testmatrix))

realresults = []
iters = 0

while True:

    for i in range(0, len(testmatrix)):
        realresults.append(computereceq(testmatrix[i], eqresultsmatrix[i], guessmatrix, i, signs[i]))

    if abs(realresults[0]-guessmatrix[0]) <= accuracy:
        break

    iters += 1
    print(iters)

    guessmatrix.clear()
    guessmatrix = realresults[:]
    realresults.clear()
    print(guessmatrix)

