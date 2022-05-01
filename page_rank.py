import numpy as np
from scipy.linalg import eig
n = int(input("Enter the number of nodes:"))
c = int(input("Enter the number of connections:"))
matrix = np.zeros((n, n))
matrix1 = np.zeros((n, n))
for i in range(c):
    x, y = map(int, input().split())
    matrix[x - 1][y - 1] = 1
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
matrix1= matrix
matrix = matrix * (1 - a)
matrix = matrix + (a / n)

print(f"Probability transition matrix without random teleportations:\n{matrix1}")
# left eigenvector of matrix1
w1, vl1 = eig(np.array(matrix1), left=True,right=False)
sum1=0
list1=[]
for x in w1:
    if x == 1:
        list1=vl1[:,sum1]
    sum1=sum1+1
print("list1:",list1)
sum1=0
list2=[]
for i in range(len(list1)):
    sum1=sum1+list1[i]
for i in range(len(list1)):
    list2.append(list1[i]/ sum1)


print(f"Principal Left eigenvector of probability transition matrix without random teleportations:\n{list2}")
print(f"Probability transition matrix with random teleportations:\n{matrix}")
w, vl = eig(np.array(matrix), left=True,right=False)
sum = 0
list = []
maxeigenvalue=0
maxeigenvalueindex=0
for x in w:
    if x>maxeigenvalue:
        maxeigenvalue=x
        maxeigenvalueindex=sum
    sum =sum+ 1
list=vl[:, maxeigenvalueindex]
sum = 0
print("list:",list)
for i in range(len(list)):
    sum =sum+ list[i]
list3=[]
for i in range(len(list)):
    list3.append(list[i] / sum)
print(f"Normalized Principal Left eigenvector of probability transition matrix with random teleportations:\n{list3}")
# power method
# print(f"Power method for probability transition matrix with random teleportations:")
# l1 = np.array([1 / 4, 1 / 4, 1 / 4, 1 / 4])
# def rec(l3):
#     l2 = np.dot(l3, matrix)
#     dist = np.sum((l3 - l2) ** 2)
#     if dist > 0.001:
#         dist = rec(l2)
#     return l2, dist 
# x=rec(l1)
# print(x) 