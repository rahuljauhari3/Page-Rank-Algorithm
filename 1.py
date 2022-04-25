import numpy as np
from scipy.linalg import eig

n = int(input("Enter the number of nodes:"))
c = int(input("Enter the number of connections:"))
matrix = np.zeros((n, n))
for i in range(c):
    x, y = map(int, input().split())
    matrix[x - 1][y - 1] = 1
print(matrix)
# random page with probability is a
a = 0.1
for i in range(n):
    count = 0
    for j in range(n):
        if matrix[i][j] == 1:
            count += 1
    for j in range(n):
        if matrix[i][j] == 1:
            matrix[i][j] = 1 / count
# probability to go through a link is 1-a
matrix = matrix * (1 - a)
matrix = matrix + (a / n)
print(matrix)
w, vl, vr = eig(matrix, left=True)
print(vl)
