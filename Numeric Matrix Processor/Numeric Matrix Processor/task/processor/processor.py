import numpy as np

matrix = []
matrix2 = []


def menu():
    print('''1. Add matrices
2. Multiply matrix by a constant
3. Multiply matrices
4. Transpose matrix
5. Calculate a determinant
6. Inverse matrix
0. Exit''')
    operation(int(input('Your choice: ')))


def operation(matrix_operation):
    if matrix_operation == 1:
        a = first_matrix(*[int(num) for num in input('Enter size of first matrix: ').split()])
        b = second_matrix(*[int(num) for num in input('Enter size of second matrix: ').split()])
        print('The result is:')
        sum_of_matrices(a, b)
        menu()
    elif matrix_operation == 2:
        a = first_matrix(*[int(num) for num in input('Enter size of matrix: ').split()], text="Enter matrix:")
        constant = float(input('Enter constant:'))
        multiplication_by_number(a, constant)
        menu()
    elif matrix_operation == 3:
        a = first_matrix(*[int(num) for num in input('Enter size of first matrix: ').split()])
        b = second_matrix(*[int(num) for num in input('Enter size of second matrix: ').split()])
        matrix_multiplication(a, b)
        menu()
    elif matrix_operation == 4:
        print('''1. Main diagonal
2. Side diagonal
3. Vertical line
4. Horizontal line''')
        user = int(input('Your choice: '))
        transpose(first_matrix(*[int(num) for num in input('Enter size of matrix: ').split()], text='Enter matrix:'),
                  user)
    elif matrix_operation == 5:
        determinant(first_matrix(*[int(num) for num in input('Enter matrix size: ').split()], text='Enter matrix:'))
        menu()
    elif matrix_operation == 6:
        inverse(first_matrix(*[int(num) for num in input('Enter matrix size: ').split()], text='Enter matrix:'))
        menu()
    elif matrix_operation == 0:
        exit()


def determinant(c):
    print('The result is:')
    print(np.linalg.det(c))


def inverse(a):
    det = np.linalg.det(a)
    if det != 0:
        c = np.linalg.inv(a)
        matrix_output(c)
    else:
        print("This matrix doesn't have an inverse.")


def first_matrix(matrix1_row, matrix1_col, text='Enter first matrix:'):
    print(text)
    return [[float(j) for j in input().split()] for _ in range(matrix1_row)]


def second_matrix(matrix2_row, matrix2_col, text='Enter second matrix:'):
    print(text)
    return [[float(j) for j in input().split()] for _ in range(matrix2_row)]


def sum_of_matrices(a, b):
    if len(a) == len(b) and len(a[0]) == len(b[0]):
        c = [[a[i][k] + b[i][k] for k in range(len(a[0]))] for i in range(len(a))]
        matrix_output(c)
    else:
        print('The operation cannot be performed.')


def multiplication_by_number(a, b):
    c = [[b * a[i][k] for k in range(len(a[0]))] for i in range(len(a))]
    print('The result is:')
    matrix_output(c)


def matrix_multiplication(a, b):
    rows_a, cols_a, rows_b, cols_b = len(a), len(a[0]), len(b), len(b[0])
    if cols_a == rows_b:
        print('The result is:')
        c = [[0 for _ in range(cols_b)] for _ in range(rows_a)]
        for i in range(rows_a):
            for j in range(cols_b):
                for k in range(cols_a):
                    c[i][j] += a[i][k] * b[k][j]
        matrix_output(c)
        a.clear()
        b.clear()
    else:
        print('The operation cannot be performed.')


def transpose(a, transpose_operation):
    c = [[0 for _ in range(len(a[0]))] for _ in range(len(a))]
    if transpose_operation == 1:
        # транспонирование по главной диагонали
        for i in range(len(a)):
            for k in range(len(a[0])):
                c[i][k] = a[k][i]
    elif transpose_operation == 2:
        # транспонирование по боковой диагонали
        for i in range(len(a)):
            for k in range(len(a[0])):
                c[i][k] = a[-1 - k][-1 - i]
    elif transpose_operation == 3:
        # транспонирование по вертикали
        for i in range(len(a)):
            a[i].reverse()
        c = a
    elif transpose_operation == 4:
        # транспонирование по горизонтальной линии
        for i in range(len(a)):
            for k in range(len(a[0])):
                c[i][k] = a[-1 - i][k]
    print('The result is:')
    matrix_output(c)
    menu()


def matrix_output(c):
    for i in range(len(c)):
        for k in range(len(c[i])):
            print("{:}".format(int(c[i][k])), end=" ") if c[i][k] % 1 == 0 else print("{:2f}".format(c[i][k]),
                                                                                      end=" ")
        print()


menu()
