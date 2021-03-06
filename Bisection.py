import math
from sympy import var
from sympy import sympify, SympifyError
from tkinter import messagebox
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


def bisection(a, b, func, accuracy, iteration, excel, check):
    x = var('x')
    try:
        func = sympify(func)
    except SympifyError:
        messagebox.showerror('Error', 'Enter Correct Equation')
        return
    try:
        if func.subs(x, a) * func.subs(x, b) >= 0:
            return -1
    except TypeError:
        messagebox.showerror('Bisection', 'Recheck the Function')
        return
    flag = True
    try:
        if iteration == '':
            accuracy = int(accuracy)
            accuracy = getacc(accuracy)
            flag = False
        else:
            iteration = int(iteration)
    except ValueError:
        messagebox.showerror("Error", 'Enter Correct iteration or accuracy')
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

    c, d, steps = (a + b) / 2, 0, 0
    if not flag:
        while not math.isclose(c, d, rel_tol=accuracy):
            c = (a + b) / 2
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
            d = (a + b) / 2
            steps += 1
            row += 1
            if func.subs(x, b) == 0 or func.subs(x, a) == 0 or func.subs(x, c) == 0:
                break
    else:
        for _ in range(iteration):
            c = (a + b) / 2
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
            steps += 1
            row += 1
    if check:
        workbook.close()
    return c
