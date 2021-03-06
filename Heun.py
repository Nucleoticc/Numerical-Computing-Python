from tkinter import messagebox

from sympy import var, SympifyError
from sympy import sympify
import xlsxwriter


def heun(a, b, xi, n, h, func, func2, excel, check):
    func = func.replace('t', 'x')
    func2 = func2.replace('t', 'x')
    x, y = var('x y')
    try:
        func = sympify(func)
    except SympifyError:
        messagebox.showerror('Error', 'Enter Correct Equation')
        return
    flag = False
    if func2 != '':
        flag = True
        try:
            func2 = sympify(func2)
        except SympifyError:
            messagebox.showerror('Error', 'Enter Correct Equation')
            return
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if n == '':
        h = float(h)
    else:
        n = int(n)
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'i')
        worksheet.write(row, col+1, 'ti')
        worksheet.write(row, col+2, 'yi')
        if flag:
            worksheet.write(row, col + 3, 'Actual Value')
            worksheet.write(row, col + 4, 'Absolute error')
        row += 1
    if n != '' and h != '':
        messagebox.showerror('Error', 'Enter Either n or h dumbass')
        return
    if n == '':
        n = (b - a)/h
        n = int(n)
    else:
        h = (b - a)/n
    add = list()
    try:
        for i in range(n):
            ans1 = (h/3)*func.subs([(x, a), (y, xi)])
            ans2 = (2/3)*h*func.subs([(x, a+(h/3)), (y, xi+ans1)])
            ans3 = 3*func.subs([(x, a+(2/3)*h), (y, xi+ans2)])
            xi = xi + 0.25*h*(func.subs([(x, a), (y, xi)]) + ans3)
            a += h
            if check:
                worksheet.write(row, col, i+1)
                worksheet.write(row, col + 1, a)
                worksheet.write(row, col + 2, xi)
                if flag:
                    actual_value = func2.subs([(x, a), (y, xi)])
                    worksheet.write(row, col + 3, actual_value)
                    worksheet.write(row, col + 4, abs(actual_value - xi))
                row += 1
            add.append(xi)
    except TypeError:
        messagebox.showerror('Error', 'Enter Correct Equation')
        return
    except ValueError:
        messagebox.showerror('Error', 'Enter Correct Equation')
        return
    if check:
        workbook.close()
    return add
