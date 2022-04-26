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
sum = 0
for i in range(n):
    sum += vl[i][0]
list = []
for i in range(n):
    list.append(vl[i][0] / sum)
print(list)

# power method
l1 = np.array([1 / 4, 1 / 4, 1 / 4, 1 / 4])


def rec(l3):
    l2 = np.dot(l3, matrix)
    # dist = [(l2 - l3) ** 2].sum()
    # dist = distances(l2, l3)
    dist = np.sum((l3 - l2) ** 2)
    if dist > 0.001:
        dist = rec(l2)
    return l2, dist


print(rec(l1))
