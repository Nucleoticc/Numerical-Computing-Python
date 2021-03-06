from tkinter import messagebox

from sympy.matrices import Matrix, matrix2numpy
from sympy import symbols, sympify, linear_eq_to_matrix, SympifyError
import xlsxwriter


def ldl(func1, func2, func3, func4, func5, func6, matrice, excel, check):
    flag = False
    x1, x2, x3, x4, x5, x6 = symbols('x1 x2 x3 x4 x5 x6')
    A = 0
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'L')
        worksheet.write(row, col+9, 'D')
        row += 1
    if func1 == '':
        A = Matrix(matrice)
        flag = True
    else:
        try:
            func1 = sympify(func1)
            func2 = sympify(func2)
            func3 = sympify(func3)
            if func4 != '':
                func4 = sympify(func4)
            if func5 != '':
                func5 = sympify(func5)
            if func6 != '':
                func6 = sympify(func6)
        except SympifyError:
            messagebox.showerror('Error', 'Enter Correct Equation')
            return
    if flag:
        try:
            L, D = A.LDLdecomposition(hermitian=False)
        except ValueError:
            messagebox.showerror('Error', 'Enter Correct Matrix')
            return
    else:
        try:
            if func4 == '':
                eq = [func1, func2, func3]
                A, b = linear_eq_to_matrix(eq, [x1, x2, x3])
                L, D = A.LDLdecomposition(hermitian=False)
            elif func4 != '' and func5 == '':
                eq = [func1, func2, func3, func4]
                A, b = linear_eq_to_matrix(eq, [x1, x2, x3, x4])
                L, D = A.LDLdecomposition(hermitian=False)
            elif func5 != '' and func6 == '':
                eq = [func1, func2, func3, func4, func5]
                A, b = linear_eq_to_matrix(eq, [x1, x2, x3, x4, x5])
                L, D = A.LDLdecomposition(hermitian=False)
            else:
                eq = [func1, func2, func3, func4, func5, func6]
                A, b = linear_eq_to_matrix(eq, [x1, x2, x3, x4, x5, x6])
                L, D = A.LDLdecomposition(hermitian=False)
        except ValueError:
            messagebox.showerror('Error', 'Enter Correct Equation')
            return
    L = matrix2numpy(L)
    D = matrix2numpy(D)
    if check:
        for row, data in enumerate(L):
            row += 1
            worksheet.write_row(row, 0, data)
        for row, data in enumerate(D):
            row += 1
            worksheet.write_row(row, 9, data)
        workbook.close()
    return
