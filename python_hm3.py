# lection 6
import random
def generate_random_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        matrix.append([])
        for j in range(cols):
            matrix[i].append(random.randint(1, 100))
    return matrix

rows = int(input("Enter rows number: "))
cols = int(input("Enter columns number: "))
matrix = generate_random_matrix(rows, cols)
print("Your matrix is:", matrix)

def get_column_sum(mat, col):
    if len(mat[0]) <= col:
        return "Column does not exist!!!"
    sum = 0
    for i in range(len(mat)):
        sum += mat[i][col]
    return sum

col = int(input("Enter the column: "))
col_sum = get_column_sum(matrix, col)
print("Sum of col:", col_sum)

def get_row_average(mat, row):
    if len(mat) <= row:
        return "Row does not exist!!!"
    average = 0
    for i in range(len(matrix[row])):
        average += matrix[row][i]
    return average / len(matrix[row])

row = int(input("Enter the row: "))
row_average = get_row_average(matrix, row)
print("Average of row:", row_average)