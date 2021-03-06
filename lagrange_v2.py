from tkinter import messagebox

from sympy import var, SympifyError
from sympy import sympify
import xlsxwriter


def lagrange(a, b, c, xi, func, fa, fb, fc, excel, check):
    x = var('x')
    flag = False
    if func != '':
        try:
            func = sympify(func)
            flag = True
        except SympifyError:
            messagebox.showerror("Error", "Enter Correct Equation")
            return
    else:
        try:
            fa = float(fa)
            fb = float(fb)
            fc = float(fc)
        except ValueError:
            messagebox.showerror("Error", "Enter Correct Numerical")
            return
        except TypeError:
            messagebox.showerror("Error", "Enter Correct Equation")
            return
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel + '.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col + 1, 'P')
        if flag:
            worksheet.write(row, col + 2, '|f(xi)-P(xi)|')
        row += 1
    try:
        if flag:
            # 2nd order:
            ans = func.subs(x, a) * ((2*xi - b - c) / ((a - b) * (a - c))) + \
                  func.subs(x, b) * ((2*xi - a - c) / ((b - a) * (b - c))) + \
                  func.subs(x, c) * ((2*xi - a - b) / ((c - a) * (c - b)))
            if check:
                worksheet.write(row, col + 1, ans)
                worksheet.write(row, col + 2, abs(func.subs(x, xi) - ans))
        else:
            # 2nd order:
            ans = fa * ((2*xi - b - c) / ((a - b) * (a - c))) + \
                  fb * ((2*xi - a - c) / ((b - a) * (b - c))) + \
                  fc * ((2*xi - a - b) / ((c - a) * (c - b)))
            if check:
                worksheet.write(row, col + 1, ans)
    except TypeError:
        messagebox.showerror("Error", "Enter Correct Equation")
        return
    except ValueError:
        messagebox.showerror("Error", "Enter Correct Equation")
        return
    if check:
        workbook.close()
    return ans
