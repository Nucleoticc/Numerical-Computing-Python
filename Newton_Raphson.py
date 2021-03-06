from tkinter import messagebox

from sympy import var, SympifyError
from sympy import sympify
from sympy import diff
import xlsxwriter


def raphson(a, func, iteration, excel, check):
    x = var('x')
    try:
        func = sympify(func)
    except SympifyError:
        messagebox.showerror("Error", "Enter Correct Equation")
        return
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
        row += 1
    try:
        dif = diff(func, x)
    except TypeError:
        messagebox.showerror('Error', 'Enter Correct Equation')
        return
    c = a - func.subs(x, a)/dif.subs(x, a)
    for _ in range(iteration):
        c = c.evalf()
        c = c - func.subs(x, c)/dif.subs(x, c)
        if check:
            worksheet.write(row, col, a)
            worksheet.write(row, col+1, func.subs(x, a))
            worksheet.write(row, col+2, c)
        row += 1
    if check:
        workbook.close()
    return c

#exp(x)+2**(-x)+2*cos(x)-6