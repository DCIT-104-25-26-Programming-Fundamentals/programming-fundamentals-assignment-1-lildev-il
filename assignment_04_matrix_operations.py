# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 4
# Topic: Multi-dimensional Arrays (2D Lists), Nested Loops, and Functions
# =============================================================================
#
# TASK: Matrix Operations
#
# Write a Python program that performs three operations on matrices (2D lists),
# each implemented in its own function.

# Function to read a matrix
def read_matrix(rows, cols):
    matrix = []
    for i in range(rows):
        row = list(map(int, input(f"Enter row {i + 1}: ").split()))
        matrix.append(row)
    return matrix


# Function to display a matrix
def display_matrix(matrix):
    for row in matrix:
        for value in row:
            print(f"{value:5}", end="")
        print()


# Part A: Transpose a matrix
def transpose_matrix(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    transpose = []
    for j in range(cols):
        new_row = []
        for i in range(rows):
            new_row.append(matrix[i][j])
        transpose.append(new_row)

    return transpose


# Part B: Add two matrices
def add_matrices(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])

    result = []
    for i in range(rows):
        row = []
        for j in range(cols):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)

    return result


# Part C: Multiply two matrices
def multiply_matrices(matrixA, matrixB):
    rowsA = len(matrixA)
    colsA = len(matrixA[0])
    colsB = len(matrixB[0])

    result = []

    for i in range(rowsA):
        row = []
        for j in range(colsB):
            total = 0
            for k in range(colsA):
                total += matrixA[i][k] * matrixB[k][j]
            row.append(total)
        result.append(row)

    return result


# ---------------- Main Program ----------------

# Part A
print("PART A - Transpose Matrix")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = read_matrix(rows, cols)

print("\nOriginal Matrix:")
display_matrix(matrix)

print("\nTransposed Matrix:")
display_matrix(transpose_matrix(matrix))


# Part B
print("\nPART B - Add Two Matrices")
rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter Matrix 1:")
matrix1 = read_matrix(rows, cols)

print("Enter Matrix 2:")
matrix2 = read_matrix(rows, cols)

print("\nSum of Matrices:")
display_matrix(add_matrices(matrix1, matrix2))


# Part C
print("\nPART C - Multiply Two Matrices")

rowsA = int(input("Enter rows of Matrix A: "))
colsA = int(input("Enter columns of Matrix A: "))

print("Enter Matrix A:")
matrixA = read_matrix(rowsA, colsA)

rowsB = int(input("Enter rows of Matrix B: "))
colsB = int(input("Enter columns of Matrix B: "))

if colsA != rowsB:
    print("Matrix multiplication is not possible.")
else:
    print("Enter Matrix B:")
    matrixB = read_matrix(rowsB, colsB)

    print("\nProduct of Matrices:")
    display_matrix(multiply_matrices(matrixA, matrixB))

