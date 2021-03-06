from tkinter import messagebox
from sympy.matrices import Matrix, matrix2numpy
from sympy import symbols, sympify, linear_eq_to_matrix, SympifyError
import xlsxwriter


def lu(func1, func2, func3, func4, func5, func6, matrice, excel, check):
    flag = False
    x1, x2, x3, x4, x5, x6 = symbols('x1 x2 x3 x4 x5 x6')
    A, B, x, y = 0, 0, 0, 0
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'L')
        worksheet.write(row, col+9, 'U')
        worksheet.write(row, col+18, 'Y')
        worksheet.write(row, col+19, 'X')
        row += 1
    if func1 == '':
        try:
            M = Matrix(matrice)
            A, B = M[:, :-1], M[:, -1]
            flag = True
        except IndexError:
            messagebox.showerror('Error', 'Enter Correct Matrix')
            return
        except SyntaxError:
            messagebox.showerror('Error', 'Enter Correct Matrix')
            return
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
            messagebox.showerror('Error', "Enter Correct Equation")
            return
    if flag:
        try:
            L, U, _ = A.LUdecomposition()
            y = L.inv()*B
            x = U.inv()*y
        except ValueError:
            messagebox.showerror('Error', 'Enter Correct Matrix')
            return
    else:
        try:
            if func4 == '':
                eq = [func1, func2, func3]
                A, b = linear_eq_to_matrix(eq, [x1, x2, x3])
                L, U, _ = A.LUdecomposition()
            elif func4 != '':
                eq = [func1, func2, func3, func4]
                A, b = linear_eq_to_matrix(eq, [x1, x2, x3, x4])
                L, U, _ = A.LUdecomposition()
            elif func5 != '':
                eq = [func1, func2, func3, func4, func5]
                A, b = linear_eq_to_matrix(eq, [x1, x2, x3, x4, x5])
                L, U, _ = A.LUdecomposition()
            else:
                eq = [func1, func2, func3, func4, func5, func6]
                A, b = linear_eq_to_matrix(eq, [x1, x2, x3, x4, x5, x6])
                L, U, _ = A.LUdecomposition()
            bb = []
            for i in b.tolist():
                for j in i:
                    bb.append(j)
            bb = Matrix(bb)
            y = L.inv()*bb
            x = U.inv()*y
        except ValueError:
            messagebox.showerror('Error', 'Enter Correct Equation')
            return
    L = matrix2numpy(L)
    U = matrix2numpy(U)
    y = matrix2numpy(y)
    x = matrix2numpy(x)
    if check:
        for row, data in enumerate(L):
            row += 1
            worksheet.write_row(row, 0, data)
        for row, data in enumerate(U):
            row += 1
            worksheet.write_row(row, 9, data)
        for row, data in enumerate(y):
            row += 1
            worksheet.write_row(row, 18, data)
        for row, data in enumerate(x):
            row += 1
            worksheet.write_row(row, 19, data)
        workbook.close()
    return
