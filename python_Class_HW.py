import random

class Matrix:
    __matrix = []
    __row = 0
    __column = 0
    def __init__(self, n, m):
        self.__row = n
        self.__column = m
        for i in range(n):
            self.__matrix.append([])
            for j in range(m):
                self.__matrix[i].append(random.randint(0, 100))

    def printMatrix(self):
        for i in range(len(self.__matrix)):
            for j in range(len(self.__matrix[i])):
                print(self.__matrix[i][j], end="  ")
            print()
    
    def mean(self):
        sum = 0
        for i in range(self.__row):
            for j in range(self.__column):
                sum += self.__matrix[i][j]
        return sum / (self.__row * self.__column)
    
    def sumOfRow(self, r):
        sum = 0
        for i in range(self.__column):
            sum += self.__matrix[r][i]
        return sum
    
    def averageOfColumn(self, c):
        sum = 0
        for i in range(self.__row):
            sum += self.__matrix[i][c]
        return sum / self.__row
    
    def Submatrix(self, *args):
        col1, col2, row1, row2 = args
        for i in range(row2 - row1 + 1):
            for j in range(col2 - col1 + 1):
                print(self.__matrix[row1 + i][col1 + j], end="  ")
            print()
                



m1 = Matrix(5, 4)
m1.printMatrix()
print(m1.mean())
print(m1.sumOfRow(0))
print(m1.averageOfColumn(0))
m1.Submatrix(1, 3, 2, 4)
