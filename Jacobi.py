from tkinter import messagebox

from sympy import symbols
from sympy import sympify, SympifyError
import xlsxwriter


def jacobi(a, b, c, d, e, f, xf1, xf2, xf3, xf4, xf5, xf6, iteration, excel, check):
    x1, x2, x3, x4, x5, x6 = symbols('x1 x2 x3 x4 x5 x6')
    try:
        xf1 = sympify(xf1)
        xf2 = sympify(xf2)
        xf3 = sympify(xf3)
        flag4, flag5, flag6 = False, False, False
        if xf6 != '':
            xf4 = sympify(xf4)
            xf5 = sympify(xf5)
            xf6 = sympify(xf6)
            d = float(d)
            e = float(e)
            f = float(f)
            flag6 = True
        elif xf5 != '':
            xf4 = sympify(xf4)
            xf5 = sympify(xf5)
            d = float(d)
            e = float(e)
            flag5 = True
        elif xf4 != '':
            d = float(d)
            xf4 = sympify(xf4)
            flag4 = True
    except SympifyError:
        messagebox.showerror("Error", "Enter Correct Equation")
        return
    except ValueError:
        messagebox.showerror("Error", "Enter Correct Numerical Value")
        return
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'x1')
        worksheet.write(row, col + 1, 'x2')
        worksheet.write(row, col + 2, 'x3')
        if flag4:
            worksheet.write(row, col + 3, 'x4')
        elif flag5:
            worksheet.write(row, col + 3, 'x4')
            worksheet.write(row, col + 4, 'x5')
        elif flag6:
            worksheet.write(row, col + 3, 'x4')
            worksheet.write(row, col + 4, 'x5')
            worksheet.write(row, col + 5, 'x6')
        row += 1
    v1, v2, v3, v4, v5, v6 = a, b, c, d, e, f
    ans = list()
    try:
        if not flag4 and not flag5 and not flag6:
            if check:
                worksheet.write(row, col, v1)
                worksheet.write(row, col + 1, v2)
                worksheet.write(row, col + 2, v3)
                row += 1
            for _ in range(iteration):
                prev_v1, prev_v2, prev_v3 = v1, v2, v3
                v1 = xf1.subs([(x2, prev_v2), (x3, prev_v3)])
                v2 = xf2.subs([(x1, prev_v1), (x3, prev_v3)])
                v3 = xf3.subs([(x1, prev_v1), (x2, prev_v2)])
                if check:
                    worksheet.write(row, col, v1)
                    worksheet.write(row, col + 1, v2)
                    worksheet.write(row, col + 2, v3)
                    row += 1
            ans.append(v1)
            ans.append(v2)
            ans.append(v3)
        elif flag4:
            if check:
                worksheet.write(row, col, v1)
                worksheet.write(row, col + 1, v2)
                worksheet.write(row, col + 2, v3)
                worksheet.write(row, col + 3, v4)
                row += 1
            for _ in range(iteration):
                prev_v1, prev_v2, prev_v3, prev_v4 = v1, v2, v3, v4
                v1 = xf1.subs([(x2, prev_v2), (x3, prev_v3), (x4, prev_v4)])
                v2 = xf2.subs([(x1, prev_v1), (x3, prev_v3), (x4, prev_v4)])
                v3 = xf3.subs([(x1, prev_v1), (x2, prev_v2), (x4, prev_v4)])
                v4 = xf4.subs([(x1, prev_v1), (x2, prev_v2), (x3, prev_v3)])
                if check:
                    worksheet.write(row, col, v1)
                    worksheet.write(row, col + 1, v2)
                    worksheet.write(row, col + 2, v3)
                    worksheet.write(row, col + 3, v4)
                    row += 1
            ans.append(v1)
            ans.append(v2)
            ans.append(v3)
            ans.append(v4)
        elif flag5:
            if check:
                worksheet.write(row, col, v1)
                worksheet.write(row, col + 1, v2)
                worksheet.write(row, col + 2, v3)
                worksheet.write(row, col + 3, v4)
                worksheet.write(row, col + 4, v5)
                row += 1
            for _ in range(iteration):
                prev_v1, prev_v2, prev_v3, prev_v4, prev_v5 = v1, v2, v3, v4, v5
                v1 = xf1.subs([(x2, prev_v2), (x3, prev_v3), (x4, prev_v4), (x5, prev_v5)])
                v2 = xf2.subs([(x1, prev_v1), (x3, prev_v3), (x4, prev_v4), (x5, prev_v5)])
                v3 = xf3.subs([(x1, prev_v1), (x2, prev_v2), (x4, prev_v4), (x5, prev_v5)])
                v4 = xf4.subs([(x1, prev_v1), (x2, prev_v2), (x3, prev_v3), (x5, prev_v5)])
                v5 = xf5.subs([(x1, prev_v1), (x2, prev_v2), (x3, prev_v3), (x4, prev_v4)])
                if check:
                    worksheet.write(row, col, v1)
                    worksheet.write(row, col + 1, v2)
                    worksheet.write(row, col + 2, v3)
                    worksheet.write(row, col + 3, v4)
                    worksheet.write(row, col + 4, v5)
                    row += 1
            ans.append(v1)
            ans.append(v2)
            ans.append(v3)
            ans.append(v4)
            ans.append(v5)
        elif flag6:
            if check:
                worksheet.write(row, col, v1)
                worksheet.write(row, col + 1, v2)
                worksheet.write(row, col + 2, v3)
                worksheet.write(row, col + 3, v4)
                worksheet.write(row, col + 4, v5)
                worksheet.write(row, col + 5, v6)
                row += 1
            for _ in range(iteration):
                prev_v1, prev_v2, prev_v3, prev_v4, prev_v5, prev_v6 = v1, v2, v3, v4, v5, v6
                v1 = xf1.subs([(x2, prev_v2), (x3, prev_v3), (x4, prev_v4), (x5, prev_v5), (x6, prev_v6)])
                v2 = xf2.subs([(x1, prev_v1), (x3, prev_v3), (x4, prev_v4), (x5, prev_v5), (x6, prev_v6)])
                v3 = xf3.subs([(x1, prev_v1), (x2, prev_v2), (x4, prev_v4), (x5, prev_v5), (x6, prev_v6)])
                v4 = xf4.subs([(x1, prev_v1), (x2, prev_v2), (x3, prev_v3), (x5, prev_v5), (x6, prev_v6)])
                v5 = xf5.subs([(x1, prev_v1), (x2, prev_v2), (x3, prev_v3), (x4, prev_v4), (x6, prev_v6)])
                v6 = xf6.subs([(x1, prev_v1), (x2, prev_v2), (x3, prev_v3), (x4, prev_v4), (x5, prev_v5)])
                if check:
                    worksheet.write(row, col, v1)
                    worksheet.write(row, col + 1, v2)
                    worksheet.write(row, col + 2, v3)
                    worksheet.write(row, col + 3, v4)
                    worksheet.write(row, col + 4, v5)
                    worksheet.write(row, col + 5, v6)
                    row += 1
            ans.append(v1)
            ans.append(v2)
            ans.append(v3)
            ans.append(v4)
            ans.append(v5)
            ans.append(v6)
    except TypeError:
        messagebox.showerror("Error", "Enter Correct Equation")
    except ValueError:
        messagebox.showerror("Error", "Enter Correct Equation")
    if check:
        workbook.close()
    return ans
