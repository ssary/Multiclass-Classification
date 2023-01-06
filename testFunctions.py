import numpy as np
from PIL import Image
import os

def addArray(ar1, ar2, sign=1):
    result = []
    # init the summation with 0s
    if len(ar1) == 0:
        for i in range(len(ar2)):
            ar1.append(0)
    
    for i in range(len(ar1)):
        result.append(ar1[i] + sign*ar2[i])

    return result

def addMat(mat1, mat2, sign=1):
    resMatrix = []
    if (len(mat1) != len(mat2)) | (len(mat1[0])!= len(mat2[0])):
        print('the two matrices are not suitable for addition (size is not the same)')
        return
    for i in range(len(mat1)):
        resrow = []
        for j in range(len(mat1[0])):
            resrow.append(mat1[i][j] + sign*mat2[i][j])
        resMatrix.append(resrow)
    return resMatrix

def arraymultdot(ar1, ar2):
    result = 0
    for i in range(len(ar1)):
        result +=(ar1[i] * ar2[i])
    return result

def column(matrix, i):
    return [row[i] for row in matrix]

def matmult(mat1, mat2):
    n = len(mat1)
    m = len(mat1[0])
    l = len(mat2[0])
    z = len(mat2)

    if(z != m):
        print('Dimensions is not suitable for multiplication', n,m,z,l)
        return
    resMatrix = []
    for i in range(n):
        resMatrix.append([])
    # i-> row in mat1, j->col in mat2
    for i in range(n):
        for j in range(l):
            cellres = arraymultdot(mat1[i], column(mat2, j))
            resMatrix[i].append(cellres)
    return resMatrix

def transpose(mat):
    n = len(mat)
    m = len(mat[0])
    resMatrix = []
    for i in range(m):
        resMatrix.append(column(mat, i))
    return resMatrix

def fill0(dimensions):
    resMat = []
    for i in range(dimensions):
        row0 = []
        for j in range(dimensions):
            row0.append(0)
        resMat.append(row0)
    return resMat

def change(a1):
    for e in a1:
        e=3

ar1 = [1,2,3,4]
ar2 = [4,3,2,5]

mat1 = [[1,2],[3,4],[5,6]]
mat2 = [[2,3],[2,5],[4,3]]

# print(addArray(ar1, ar2))
# print(addArray(ar1,ar2,-1))

# print(addMat(mat1, mat2))
# print(addMat(mat1,[[1,3,4]]))
# print(arraymultdot(ar1,ar2))

# print(column(mat1, 1))

# print(matmult(mat1,[[2,3],[4,5]]))
# print(matmult(mat1, [[2,3]]))

# print(transpose(mat1))

# print(fill0(3))

# print([ar1])
# print(transpose([ar1]))

# change(ar1)
# print(ar1)

npar = np.array([])
npar = np.append(npar, 1)
print(npar)