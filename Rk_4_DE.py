from tkinter import messagebox

from sympy import var
from sympy import sympify, SympifyError
import xlsxwriter


def rk_4(a, b, c, xi, n, h, func, func2, excel, check):
    func = func.replace('t', 'x')
    func2 = func2.replace('t', 'x')
    x, y, z = var('x y z')
    try:
        func = sympify(func)
        func2 = sympify(func2)
    except SympifyError:
        messagebox.showerror('Error', 'Enter Correct Equation')
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if n != '' and h != '':
        messagebox.showerror('Error', 'Enter Either n or h dumbass')
        return
    if n == '':
        h = float(h)
    else:
        n = int(n)
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'i')
        worksheet.write(row, col+1, 'ti')
        worksheet.write(row, col+2, 'k1')
        worksheet.write(row, col+3, 'l1')
        worksheet.write(row, col+4, 'k2')
        worksheet.write(row, col+5, 'l2')
        worksheet.write(row, col+6, 'k3')
        worksheet.write(row, col+7, 'l3')
        worksheet.write(row, col+8, 'k4')
        worksheet.write(row, col+9, 'l4')
        worksheet.write(row, col+10, 'yi')
        worksheet.write(row, col+11, 'zi')
        row += 1
    if n == '':
        n = (b - a)/h
        n = int(n)
    else:
        h = (b - a)/n
    add = list()
    try:
        for i in range(n):
            k1 = h*func.subs([(x, a), (y, xi), (z, c)])
            l1 = h*func2.subs([(x, a), (y, xi), (z, c)])
            k2 = h*func.subs([(x, a+(h/2)), (y, xi+(k1/2)), (z, c+(l1/2))])
            l2 = h*func2.subs([(x, a+(h/2)), (y, xi+(k1/2)), (z, c+(l1/2))])
            k3 = h*func.subs([(x, a+(h/2)), (y, xi+(k2/2)), (z, c+(l2/2))])
            l3 = h*func2.subs([(x, a+(h/2)), (y, xi+(k2/2)), (z, c+(l2/2))])
            k4 = h*func.subs([(x, a+h), (y, xi+k3), (z, c+l3)])
            l4 = h*func2.subs([(x, a+h), (y, xi+k3), (z, c+l3)])
            xi = xi + (1/6)*(k1+2*k2+2*k3+k4)
            c = c + (1/6)*(l1+2*l2+2*l3+l4)
            a += h
            if check:
                worksheet.write(row, col, i+1)
                worksheet.write(row, col + 1, a)
                worksheet.write(row, col + 2, k1)
                worksheet.write(row, col + 3, l1)
                worksheet.write(row, col + 4, k2)
                worksheet.write(row, col + 5, l2)
                worksheet.write(row, col + 6, k3)
                worksheet.write(row, col + 7, l3)
                worksheet.write(row, col + 8, k4)
                worksheet.write(row, col + 9, l4)
                worksheet.write(row, col + 10, xi)
                worksheet.write(row, col + 11, c)
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
