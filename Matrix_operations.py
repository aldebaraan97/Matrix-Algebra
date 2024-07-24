# Functions to operate matrices made out of python lists
# explanation of how the algorithm works can be found in the first function.

# Adds a matrix A to a matrix B
def matrix_add(A, B):
    # precondition: A and B must be two matrices of the same size
    if len(A) == len(B) and len(A[0] == len(B[0])):
        # crates a list 'C' tha contains other lists(matrix C), each list is a row
        # first list contains 'len(A)' elements, which is the number of columns
        # after creating the first list (row), the iterator will create another list (row) and so on
        C = [[0 for j in range (len(A[0]))] for i in range(len(A))]

        # first loop will access the matrix A
        for i in range(len(A)):
            # second loop, once inside A, will populate each column of the first row
            for j in range(len(A[0])):
                # the matrix C will be populated starting from the first row to the last row
                # first row, first iteration C[0][0] = A[0][0] + B[0][0]
                # first row, second iteration C[0][1] = A[0][1] + B[0][1]
                # after looping through each column in the first row, the second row iteration set will start
                # second row, first iteration C[1][0] = A[1][0] + B[1][0]
                # second row, second iteration C[1][1] = A[1][1] + B[1][1]
                C[i][j] = A[i][j] + B[i][j]

        return C

def matrix_mult_by_scalar(A, alpha):
    C = [[0 for j in range(len(A[0]))] for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[i][j] = alpha * A[i][j]

    return C

def matrix_subtract(A, B):
    if len(A) == len(B) and len(A[0]) == len(B[0]):
        C = [[0 for j in range(len(A[0]))] for i in range(len(A))]

        for i in range(len(A)):
            for j in range(len(A[0])):
                C[i][j] = A[i][j] - B[i][j]

        return C

def matrix_transpose(A):
    C = [[0 for j in range(len(A))] for i in range(len(A[0]))]

    for i in range(len(A)):
        for j in range(len(A[0])):
            C[j][i] = A[i][j]
    return C

# Multiplication of matrices A and B
def matrix_mult(A, B):
    C = [[0 for j in range(len(B[0]))] for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            s = 0

            for k in range(len(B)):
                s += A[i][k] * B[k][j]

                C[i][j] = s
    return C