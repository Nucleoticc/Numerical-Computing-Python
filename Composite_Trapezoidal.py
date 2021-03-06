from sympy import var, SympifyError
from sympy import sympify
import xlsxwriter
from tkinter import messagebox


def trapezoidal(a, b, n, h, func, excel, check):
    x = var('x')
    try:
        func = sympify(func)
    except SympifyError:
        messagebox.showerror('Error', 'Enter Correct Equation')
        return
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if n != '' and h != '':
        messagebox.showerror('Error', 'Enter Either n or h dumbass')
        return
    if n == '':
        h = float(h)
    elif h == '':
        n = int(n)
    if check:
        workbook = xlsxwriter.Workbook(excel + '.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'x')
        worksheet.write(row, col + 1, 'f(x)')
        worksheet.write(row, col + 2, 'f\'(x)')
        row += 1
    if h == '':
        h = (b - a) / n
    else:
        n = (b - a) / h
        n = int(n)
    prev_a = a
    add = 0
    try:
        if check:
            worksheet.write(row, col, a)
            worksheet.write(row, col + 1, func.subs(x, a))
            row += 1
        for _ in range(1, n):
            a = a+h
            add += func.subs(x, a)
            if check:
                worksheet.write(row, col, a)
                worksheet.write(row, col + 1, func.subs(x, a))
                row += 1
        add = 2*add
        add += func.subs(x, prev_a)
        add += func.subs(x, b)
        add = (h/2)*add
        if check:
            worksheet.write(row, col, b)
            worksheet.write(row, col+1, func.subs(x, b))
            worksheet.write(row + 1, col + 2, add)
    except TypeError:
        messagebox.showerror('Error', 'Enter Correct Equation')
        return
    except ValueError:
        messagebox.showerror('Error', 'Enter Correct Equation')
        return
    if check:
        workbook.close()
    return add
