import numpy as np


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


# def computereceq(equation, result, guess, i, signs):
#     eq = equation[:]
#     sg = signs[:]
#     gs = guess[:]
#     divide = 1/eq[i]
#     eq.pop(i)
#     sg.pop(i)
#     gs.pop(i)
#     part_result = 0
#     #eq-1
#     for x in range(0, len(eq)):
#         if sg[x] == '-':
#             part_result = part_result - (abs(eq[x])*gs[x])
#         elif sg[x] == '+':
#             part_result = part_result + (abs(eq[x])*gs[x])
#
#     return divide*(result+part_result)

def jacobi(A, b, x, n):

    D = np.diag(A)
    R = A - np.diagflat(D)

    for i in range(n):
        x = (b - np.dot(R, x)) / D
        print(x)


equations = np.array([[7.0, 2.0, -3.0], [1.0, 10.0, 2.0], [4.0, 3.0, -8.0]])
equation_results = [14.0, 20.0, 16.0]
guesses = [0.0, 0.0, 0.0]
n = 25

guesses = jacobi(equations, equation_results, guesses, n)

# accuracy = pow(10, -3)
#
# testmatrix = [[7, 2, -3],
#               [1, 10, 2],
#               [4, 3, -8]
#               ]
#
# # TODO metodu na generovanie tohto pola z testmatrix
# signs = [['-', '-', '+'],
#          ['-', '-', '-'],
#          ['-', '-', '+']
#          ]
# eqresultsmatrix = [14, 20, 16]
# guessmatrix = [0, 0, 0]
#
# #print(rownorm(testmatrix), colnorm(testmatrix), frobnorm(testmatrix))
#
# realresults = []
# iters = 0
#
# while True:
#     print(iters)
#     iters += 1
#
#     for i in range(0, len(testmatrix)):
#         realresults.append(computereceq(testmatrix[i], eqresultsmatrix[i], guessmatrix, i, signs[i]))
#
#     if abs(realresults[0]-guessmatrix[0]) <= accuracy:
#         break
#
#     guessmatrix.clear()
#     guessmatrix = realresults[:]
#     realresults.clear()
#     print(guessmatrix)

