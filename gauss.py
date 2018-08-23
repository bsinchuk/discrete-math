"""
Realisation of Gaussian elimination algorithm for solving systems of linear equations.
n - number of equations. m - number of unknowns.
"""
import fractions

first_line = input().split(" ")
n = int(first_line[0])
m = int(first_line[1])
matrix = {}

for i in range (0, n):
    line = input().split(" ")
    line = list(map(float, line))
    line = list(map(fractions.Fraction, line))
    matrix[i] = line

#pryamoy hod
for column in range(0, m - 1):
    if column >= len(matrix):
        print ("INF")
        quit()
    if matrix[column][column] == 0:
        for i in range(column + 1, n):
            if matrix[i][column] != 0:
                temp = matrix[i]
                matrix[i] = matrix[column]
                matrix[column] = temp
        if matrix[column][column] == 0:
            print("INF")
            quit()
    for row in range(column + 1, n):
        k = (matrix[row][column] / matrix[column][column])
        if not k == 0:
            for i in range(m + 1):
                temp = matrix[column][i] * k
                matrix[row][i] = matrix[row][i] - temp
        if(matrix[row].count(0) == m) and (matrix[row][m] != 0):
                print ("NO")
                quit()
        if(matrix[row].count(0) == m + 1):
                matrix.pop(row)

if len(matrix) < m:
    print ("INF")
    quit()

answer = []
#obratniy hod
u = m - 1
for i in range(len(matrix)-1, -1, -1):
    for j in range(0, m):
        if matrix[i][j] != 0 and j != u:
            matrix[i][j] = matrix[i][j] * fractions.Fraction(-1.0)
            matrix[i][m] += matrix[i][j]
    if not i in range(len(matrix[i])-1):
        print ("NO")
        quit()
    if (matrix[i][i] != 0):
        result = matrix[i][m] / matrix[i][i]
        u = u-1
        answer.append(result)
        for j in range(0, i):
            matrix[j][i] *= result
print ("YES")
for elem in reversed(answer):
    if(float(elem) - int(elem) == 0):
        print (int(elem), end = ' ')
    else:
        print (float(elem), end = ' ')
