import math
from tkinter import messagebox

from sympy import var, SympifyError
from sympy import sympify
import xlsxwriter


def reg_falsi(a, b, func, iteration, excel, check):
    x = var('x')
    try:
        func = sympify(func)
    except SympifyError:
        messagebox.showerror("Error", "Enter Correct Equation")
        return
    try:
        if func.subs(x, a) * func.subs(x, b) >= 0:
            return -1
    except TypeError:
        messagebox.showerror('Error', 'Recheck the Function')
        return
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'a')
        worksheet.write(row, col+1, 'b')
        worksheet.write(row, col+2, 'f(a)')
        worksheet.write(row, col+3, 'f(b)')
        worksheet.write(row, col+4, 'c')
        worksheet.write(row, col+5, 'f(c)')
        row += 1
    c = (a*func.subs(x, b) - b*func.subs(x, a))/(func.subs(x, b)-func.subs(x, a))
    for _ in range(iteration):
        c = (a*func.subs(x, b) - b*func.subs(x, a))/(func.subs(x, b)-func.subs(x, a))
        if check:
            worksheet.write(row, col, a)
            worksheet.write(row, col+1, b)
            worksheet.write(row, col+2, func.subs(x, a))
            worksheet.write(row, col+3, func.subs(x, b))
            worksheet.write(row, col+4, c)
            worksheet.write(row, col+5, func.subs(x, c))
        if func.subs(x, a) * func.subs(x, c) >= 0:
            a = c
        elif func.subs(x, b) * func.subs(x, c) >= 0:
            b = c
        else:
            return -1
        row += 1
    if check:
        workbook.close()
    return c
