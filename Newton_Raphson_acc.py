import math
from tkinter import messagebox

from sympy import var
from sympy import sympify, SympifyError
from sympy import diff
import xlsxwriter


def getacc(accuracy):
    if accuracy == 1:
        return 1e-1
    elif accuracy == 2:
        return 1e-2
    elif accuracy == 3:
        return 1e-3
    elif accuracy == 4:
        return 1e-4
    elif accuracy == 5:
        return 1e-5
    elif accuracy == 6:
        return 1e-6
    elif accuracy == 7:
        return 1e-7
    elif accuracy == 8:
        return 1e-8


def raphson(a, func, accuracy, excel, check):
    x = var('x')
    try:
        func = sympify(func)
    except SympifyError:
        messagebox.showerror("Error", "Enter Correct Equation")
        return
    accuracy = getacc(accuracy)
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'a')
        worksheet.write(row, col+1, 'f(a)')
        worksheet.write(row, col+2, 'c')
        worksheet.write(row, col + 3, 'f(c)-f(c-1)')
        row += 1
    try:
        dif = diff(func, x)
    except TypeError:
        messagebox.showerror('Error', 'Enter Correct Equation')
        return
    c, d = a - func.subs(x, a)/dif.subs(x, a), 0
    while not math.isclose(c, d, rel_tol=accuracy):
        c = c.evalf()
        c = c - func.subs(x, c)/dif.subs(x, c)
        if check:
            worksheet.write(row, col, a)
            worksheet.write(row, col+1, func.subs(x, a))
            worksheet.write(row, col+2, c)
            worksheet.write(row, col + 3, c-d)
        d = c - func.subs(x, c)/dif.subs(x, c)
        row += 1
    if check:
        workbook.close()
    return c

#