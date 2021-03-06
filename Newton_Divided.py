from tkinter import messagebox

import xlsxwriter


def func(xi, xj, fxi, fxj):
    return (fxi - fxj)/(xi-xj)


def func2(xi, xj, xk, fxi, fxj, fxk):
    return (func(xi, xj, fxi, fxj)-func(xj, xk, fxj, fxk))/(xi-xk)


def func3(xi, xj, xk, xl, fxi, fxj, fxk, fxl):
    return (func2(xi, xj, xk, fxi, fxj, fxk)-func2(xj, xk, xl, fxj, fxk, fxl))/(xi-xl)


def func4(xi, xj, xk, xl, xm, fxi, fxj, fxk, fxl, fxm):
    return (func3(xi, xj, xk, xl, fxi, fxj, fxk, fxl)-func3(xj, xk, xl, xm, fxj, fxk, fxl, fxm))/(xi-xm)


def divided(a, b, c, d, e, fa, fb, fc, fd, fe, xi, excel, check):
    answer = list()
    row = 0
    col = 0
    flag = False
    if e != '':
        try:
            e = float(e)
            fe = float(e)
            flag = True
        except ValueError:
            messagebox.showerror('Error', "Enter Correct Numerical Values")
            return
        except TypeError:
            messagebox.showerror('Error', "Enter Correct Numerical Values")
            return
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel + '.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'P1')
        worksheet.write(row, col + 1, 'P2')
        worksheet.write(row, col + 2, 'P3')
        if flag:
            worksheet.write(row, col + 3, 'P4')
        row += 1
    # 1st Order:
    p4 = 0
    p1 = fa + func(a, b, fa, fb)*(xi-a)
    # 2nd Order:
    p2 = p1 + func2(a, b, c, fa, fb, fc)*(xi-a)*(xi-b)
    # 3rd Order:
    p3 = p2 + func3(a, b, c, d, fa, fb, fc, fd)*(xi-a)*(xi-b)*(xi-c)
    answer.append(p1)
    answer.append(p2)
    answer.append(p3)
    if flag:
        p4 = p3 + func4(a, b, c, d, e, fa, fb, fc, fd, fe)*(xi-a)*(xi-b)*(xi-c)*(xi-d)
        answer.append(p4)
    if check:
        worksheet.write(row, col, p1)
        worksheet.write(row, col + 1, p2)
        worksheet.write(row, col + 2, p3)
        if flag:
            worksheet.write(row, col + 3, p4)
        row += 5
        worksheet.write(row, col, a)
        worksheet.write(row + 2, col, b)
        worksheet.write(row + 4, col, c)
        worksheet.write(row + 6, col, d)
        if flag:
            worksheet.write(row + 8, col, e)
            worksheet.write(row + 8, col + 1, fe)
            worksheet.write(row + 7, col + 2, func(d, e, fd, fe))
            worksheet.write(row + 6, col + 3, func2(c, d, e, fc, fd, fe))
            worksheet.write(row + 5, col + 4, func3(b, c, d, e, fb, fc, fd, fe))
            worksheet.write(row + 4, col + 5, func4(a, b, c, d, e, fa, fb, fc, fd, fe))
        worksheet.write(row, col + 1, fa)
        worksheet.write(row + 2, col + 1, fb)
        worksheet.write(row + 4, col + 1, fc)
        worksheet.write(row + 6, col + 1, fd)
        worksheet.write(row + 1, col + 2, func(a, b, fa, fb))
        worksheet.write(row + 3, col + 2, func(b, c, fb, fc))
        worksheet.write(row + 5, col + 2, func(c, d, fc, fd))
        worksheet.write(row + 2, col + 3, func2(a, b, c, fa, fb, fc))
        worksheet.write(row + 4, col + 3, func2(b, c, d, fb, fc, fd))
        worksheet.write(row + 3, col + 4, func3(a, b, c, d, fa, fb, fc, fd))
        workbook.close()
    return answer
