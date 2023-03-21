# 
#  simplex.py
#  @author kukimukiku
#  Simplex algorithm for linear programming problem
#  


import math
import numpy as np


# Given function
def f(x, y, z):
    return 2 * x -3 * y - 5 * z


def simplex(c, A, base):
    get_tableau = to_tableau(c, A, base)
    f_val = get_tableau[1]
    tableau = get_tableau[0]
    i = 0
    while can_be_improved(tableau):
        improve_tableu(tableau, base)
        get_tableau = to_tableau(tableau[3], [tableau[0], tableau[1], tableau[2]], tableau[4])
        f_val = get_tableau[1]
        tableau = get_tableau[0]
        i += 1
    answer = [0, 0, 0, 0, 0, 0, 0]
    answer[base[0] - 1] = tableau[0][7]
    answer[base[1] - 1] = tableau[1][7]
    answer[base[2] - 1] = tableau[2][7]
    print("\n")
    print("Function f(X) minimum - ", f_val)
    print("X = ", answer)


def to_tableau(c, A, base):
    xb = A

    x = 0
    y = 0
    z = 0

    x_for_f = 0
    y_for_f = 0
    z_for_f = 0

    for b in base:
        if b == 1:
            x = 2
        if b == 2:
            y = -3
        if b == 4:
            z = -5

    if base[0] == 1:
        x_for_f = xb[0][7]
    if base[1] == 1:
        x_for_f = xb[1][7]
    if base[2] == 1:
        x_for_f = xb[2][7]

    if base[0] == 2:
        y_for_f = xb[0][7]
    if base[1] == 2:
        y_for_f = xb[1][7]
    if base[2] == 2:
        y_for_f = xb[2][7]

    if base[0] == 3:
        z_for_f = xb[0][7]
    if base[1] == 3:
        z_for_f = xb[1][7]
    if base[2] == 3:
        z_for_f = xb[2][7]

    z = count_c(xb, x, y, z)

    print("\n     X1  X2  X3  X4  X5  X6  X7")
    print("X", base[0], xb[0])
    print("X", base[1], xb[1])
    print("X", base[2], xb[2])
    print("f", f(x_for_f, y_for_f, z_for_f), z)

    return [xb + [z] + [base]] + [f(x_for_f, y_for_f, z_for_f)]


def improve_tableu(tableau, base):
    i = 0

    while tableau[3][i] <= 0:
        i += 1

    if div(tableau[0][7], tableau[0][i]) <= div(tableau[1][7], tableau[1][i]) <= div(tableau[2][7], tableau[2][i]):
        tableau[0][:] = [x / tableau[0][i] for x in tableau[0]]
        base[0] = i + 1
        tableau[0][7] = div(tableau[0][7], tableau[0][i])
    elif div(tableau[0][7], tableau[0][i]) <= div(tableau[2][7], tableau[2][i]) <= div(tableau[1][7], tableau[1][i]):
        tableau[0][:] = [x / tableau[0][i] for x in tableau[0]]
        base[0] = i + 1
        tableau[0][7] = div(tableau[0][7], tableau[0][i])
    elif div(tableau[1][7], tableau[1][i]) <= div(tableau[0][7], tableau[0][i]) <= div(tableau[2][7], tableau[2][i]):
        tableau[1][:] = [x / tableau[1][i] for x in tableau[1]]
        base[1] = i + 1
        tableau[1][7] = div(tableau[1][7], tableau[1][i])
        tableau[0][:] = [x - tableau[1][i] for x in tableau[0]]
    elif div(tableau[1][7], tableau[1][i]) <= div(tableau[2][7], tableau[2][i]) <= div(tableau[0][7], tableau[0][i]):
        tableau[1][:] = [x / tableau[1][i] for x in tableau[1]]
        base[1] = i + 1
        tableau[1][7] = div(tableau[1][7], tableau[1][i])
        tableau[0][:] = [x - tableau[1][i] for x in tableau[0]]
    elif div(tableau[2][7], tableau[2][i]) <= div(tableau[1][7], tableau[1][i]) <= div(tableau[0][7], tableau[0][i]):
        tableau[2][:] = [x / tableau[2][i] for x in tableau[2]]
        base[2] = i+1
        tableau[2][7] = div(tableau[2][7], tableau[2][i])
        temp = []
        for item1, item in zip(tableau[0], tableau[2]):
            temp.append(item1 + item)
        tableau[0] = temp
    elif div(tableau[2][7], tableau[2][i]) <= div(tableau[0][7], tableau[0][i]) <= div(tableau[1][7], tableau[1][i]):
        tableau[2][:] = [x / tableau[2][i] for x in tableau[2]]
        base[2] = i+1
        tableau[2][7] = div(tableau[2][7], tableau[2][i])
        temp = []
        for item1, item in zip(tableau[0], tableau[2]):
            temp.append(item1 + item)
        tableau[0] = temp


def div(a, b):
    if b != 0 and b > 0:
        return a/b
    else:
        return 1000


# Checking if table can be improved
def can_be_improved(tableau):
    z = tableau[3]
    return any(x > 0 for x in z)

def count_c(A, x, y, z):
    c1 = A[0][0] * x + A[1][0] * y + A[2][0] * z - 2
    c2 = A[0][1] * x + A[1][1] * y + A[2][1] * z + 3
    c3 = A[0][2] * x + A[1][2] * y + A[2][2] * z
    c4 = A[0][3] * x + A[1][3] * y + A[2][3] * z + 5
    c5 = A[0][4] * x + A[1][4] * y + A[2][4] * z
    c6 = A[0][5] * x + A[1][5] * y + A[2][5] * z
    c7 = A[0][6] * x + A[1][6] * y + A[2][6] * z

    return [c1, c2, c3, c4, c5, c6, c7]


if __name__ == '__main__':
    print("Simplex algorithm for linear programming problem")

    c = [2, -3, 0, -5, 0, 0, 0]
    A = [
        [-1, 1, 0, 0, 1, 0, 1, 8],
        [2, 4, 0, 0, 0, 1, 0, 10],
        [0, 0, 1, 1, 0, 0, 1, 3]
    ]
    base = [5, 6, 7]
    simplex(c, A, base)