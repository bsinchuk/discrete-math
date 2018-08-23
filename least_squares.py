"""
Realisation of least squares approach for solving systems of linear equations.
n - number of equations. m - number of unknowns.
"""
import fractions

def scalar(first, second):
    res = 0
    for i in range(len(first)):
        res += first[i] * second[i]
    return res

first_line = input().split(" ")
n = int(first_line[0])
m = int(first_line[1])
input_matrix = {}

for i in range(0, m + 1):

    input_matrix[i] = []

for i in range(n):
    line = input().split(" ")
    if line.count(' ') > 0:
        line.remove(' ')
    if line.count('') > 0:
        line.remove('')
    line = list(map(fractions.Fraction, line))
    for j in range(m + 1):
        input_matrix[j].append(line[j])

matrix = {}
for i in range(0, m):
    matrix[i] = []

for i in range(0, m):
    for j in range(0, m + 1):
        if j == m:
            matrix[i].append(scalar(input_matrix[m], input_matrix[i]))
        else:
            matrix[i].append(scalar(input_matrix[i], input_matrix[j]))
#pryamoy hod
for column in range(0, m - 1):
    if matrix[column][column] == 0:
        for i in range(column + 1, m):
            if matrix[i][column] != 0:
                temp = matrix[i]
                matrix[i] = matrix[column]
                matrix[column] = temp
    for row in range(column + 1, m):
        k = (matrix[row][column] / matrix[column][column])
        if not k == 0:
            for i in range(m + 1):
                temp = matrix[column][i] * k
                matrix[row][i] = matrix[row][i] - temp
        if(matrix[row].count(0) == m + 1):
                matrix.pop(row)
answer = []
#obratniy hod
u = m - 1
for i in range(len(matrix)-1, -1, -1):
    for j in range(0, m):
        if matrix[i][j] != 0 and j != u:
            matrix[i][j] = matrix[i][j] * fractions.Fraction(-1.0)
            matrix[i][m] += matrix[i][j]
    if (matrix[i][i] != 0):
        result = matrix[i][m] / matrix[i][i]
        u = u-1
        answer.append(result)
        for j in range(0, i):
            matrix[j][i] *= result
for elem in reversed(answer):
    if(float(elem) - int(elem) == 0):
        print (int(elem), end = ' ')
    else:
        print (float(elem), end = ' ')
