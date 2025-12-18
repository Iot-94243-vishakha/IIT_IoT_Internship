"""Create matrix of dim 3x4 as list of list with few fixed values. Create another matrix of dim 3x4 as tuple of
tuple with few fixed values. Create a function that takes these two matrices as params and calculate
their addition & subtraction. The function should return both result matrices and they should be
printed in main."""



matrix1 = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

matrix2 = (
    (10, 20, 30, 40),
    (50, 60, 70, 80),
    (90, 100, 110, 120)
)

def matrix_operations(m1, m2):
    add = []
    sub = []
    for i in range(len(m1)):
        add_row = []
        sub_row = []
        for j in range(len(m1[0])):
            add_row.append(m1[i][j] + m2[i][j])
            sub_row.append(m1[i][j] - m2[i][j])
        add.append(add_row)
        sub.append(sub_row)
    return add, sub

addition, subtraction = matrix_operations(matrix1, matrix2)

print("Addition Matrix: \n", addition,"\n")
print("Subtraction Matrix:\n", subtraction,"\n")