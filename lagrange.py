from tkinter import messagebox

from sympy import var, SympifyError
from sympy import sympify
import xlsxwriter


def lagrange(a, b, c, d, e, xi, func, excel, check):
    answer = list()
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
    if d != '' and e == '':
        try:
            d = float(d)
        except ValueError:
            messagebox.showerror("Error", "Recheck the Numerical Inputs")
            return
        except TypeError:
            messagebox.showerror("Error", "Recheck the Numerical Inputs")
            return
    elif e != '':
        try:
            d = float(d)
            e = float(e)
        except ValueError:
            messagebox.showerror("Error", "Recheck the Numerical Inputs")
            return
        except TypeError:
            messagebox.showerror("Error", "Recheck the Numerical Inputs")
            return
    if check:
        workbook = xlsxwriter.Workbook(excel + '.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'P1')
        worksheet.write(row, col + 1, '|f(xi)-P1(xi)|')
        worksheet.write(row, col + 2, 'P2')
        worksheet.write(row, col + 3, '|f(xi)-P2(xi)|')
        if d != '' and e == '':
            worksheet.write(row, col + 4, 'P3')
            worksheet.write(row, col + 5, '|f(xi)-P3(xi)|')
        elif e != '':
            worksheet.write(row, col + 4, 'P3')
            worksheet.write(row, col + 5, '|f(xi)-P3(xi)|')
            worksheet.write(row, col + 6, 'P4')
            worksheet.write(row, col + 7, '|f(xi)-P4(xi)|')
        row += 1
    try:
        # 1st order:
        ans = func.subs(x, a) * ((xi - b) / (a - b)) + func.subs(x, b) * ((xi - a) / (b - a))
        if check:
            worksheet.write(row, col, ans)
            worksheet.write(row, col + 1, abs(func.subs(x, xi) - ans))
        answer.append(ans)
        # 2nd order:
        ans = func.subs(x, a) * (((xi - b) * (xi - c)) / ((a - b) * (a - c))) + \
              func.subs(x, b) * (((xi - a) * (xi - c)) / ((b - a) * (b - c))) + \
              func.subs(x, c) * (((xi - a) * (xi - b)) / ((c - a) * (c - b)))
        if check:
            worksheet.write(row, col + 2, ans)
            worksheet.write(row, col + 3, abs(func.subs(x, xi) - ans))
        answer.append(ans)
        # 3rd order:
        if d != '' and e == '':
            ans = func.subs(x, a) * (((xi - b) * (xi - c) * (xi - d)) / ((a - b) * (a - c) * (a - d))) + \
                  func.subs(x, b) * (((xi - a) * (xi - c) * (xi - d)) / ((b - a) * (b - c) * (b - d))) + \
                  func.subs(x, c) * (((xi - a) * (xi - b) * (xi - d)) / ((c - a) * (c - b) * (c - d))) + \
                  func.subs(x, d) * (((xi - a) * (xi - b) * (xi - c)) / ((d - a) * (d - b) * (d - c)))
            if check:
                worksheet.write(row, col + 4, ans)
                worksheet.write(row, col + 5, abs(func.subs(x, xi) - ans))
            answer.append(ans)
        elif e != '':
            ans1 = func.subs(x, a) * (((xi - b) * (xi - c) * (xi - d)) / ((a - b) * (a - c) * (a - d))) + \
                   func.subs(x, b) * (((xi - a) * (xi - c) * (xi - d)) / ((b - a) * (b - c) * (b - d))) + \
                   func.subs(x, c) * (((xi - a) * (xi - b) * (xi - d)) / ((c - a) * (c - b) * (c - d))) + \
                   func.subs(x, d) * (((xi - a) * (xi - b) * (xi - c)) / ((d - a) * (d - b) * (d - c)))
            ans2 = func.subs(x, a) * (
                    ((xi - b) * (xi - c) * (xi - d) * (xi - e)) / ((a - b) * (a - c) * (a - d) * (a - e))) + \
                   func.subs(x, b) * (
                           ((xi - a) * (xi - c) * (xi - d) * (xi - e)) / ((b - a) * (b - c) * (b - d) * (b - e))) + \
                   func.subs(x, c) * (
                           ((xi - a) * (xi - b) * (xi - d) * (xi - e)) / ((c - a) * (c - b) * (c - d) * (c - e))) + \
                   func.subs(x, d) * (
                           ((xi - a) * (xi - b) * (xi - c) * (xi - e)) / ((d - a) * (d - b) * (d - c) * (d - e))) + \
                   func.subs(x, e) * (
                           ((xi - a) * (xi - b) * (xi - c) * (xi - d)) / ((e - a) * (e - b) * (e - c) * (e - d)))
            if check:
                worksheet.write(row, col + 4, ans1)
                worksheet.write(row, col + 5, abs(func.subs(x, xi) - ans1))
                worksheet.write(row, col + 6, ans2)
                worksheet.write(row, col + 7, abs(func.subs(x, xi) - ans2))
            answer.append(ans1)
            answer.append(ans2)
    except TypeError:
        messagebox.showerror("Error", "Enter Correct Equation")
        return
    except ValueError:
        messagebox.showerror("Error", "Enter Correct Equation")
        return
    if check:
        workbook.close()
    return answer
