from tkinter import messagebox

import xlsxwriter


def lagrange(a, b, c, d, e, fa, fb, fc, fd, fe, xi, excel, check):
    answer = list()
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if d != '' and e == '':
        try:
            d = float(d)
            fd = float(d)
        except ValueError:
            messagebox.showerror("Error", "Recheck the Numerical Inputs")
            return
        except TypeError:
            messagebox.showerror("Error", "Recheck the Numerical Inputs")
            return
    elif e != '':
        try:
            d = float(d)
            fd = float(d)
            e = float(e)
            fe = float(fe)
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
        worksheet.write(row, col + 1, 'P2')
        if d != '' and e == '':
            worksheet.write(row, col + 2, 'P3')
        if e != '':
            worksheet.write(row, col + 2, 'P3')
            worksheet.write(row, col + 3, 'P4')
        row += 1
    # 1st order:
    ans = fa * ((xi - b) / (a - b)) + fb * ((xi - a) / (b - a))
    if check:
        worksheet.write(row, col, ans)
    answer.append(ans)
    # 2nd order:
    ans = fa * (((xi - b) * (xi - c)) / ((a - b) * (a - c))) + \
          fb * (((xi - a) * (xi - c)) / ((b - a) * (b - c))) + \
          fc * (((xi - a) * (xi - b)) / ((c - a) * (c - b)))
    if check:
        worksheet.write(row, col + 1, ans)
    answer.append(ans)
    # 3rd order:
    if d != '' and e == '':
        ans = fa * (((xi - b) * (xi - c) * (xi - d)) / ((a - b) * (a - c) * (a - d))) + \
              fb * (((xi - a) * (xi - c) * (xi - d)) / ((b - a) * (b - c) * (b - d))) + \
              fc * (((xi - a) * (xi - b) * (xi - d)) / ((c - a) * (c - b) * (c - d))) + \
              fd * (((xi - a) * (xi - b) * (xi - c)) / ((d - a) * (d - b) * (d - c)))
        if check:
            worksheet.write(row, col + 2, ans)
        answer.append(ans)
    elif e != '':
        ans1 = fa * (((xi - b) * (xi - c) * (xi - d)) / ((a - b) * (a - c) * (a - d))) + \
               fb * (((xi - a) * (xi - c) * (xi - d)) / ((b - a) * (b - c) * (b - d))) + \
               fc * (((xi - a) * (xi - b) * (xi - d)) / ((c - a) * (c - b) * (c - d))) + \
               fd * (((xi - a) * (xi - b) * (xi - c)) / ((d - a) * (d - b) * (d - c)))
        ans2 = fa * (
                ((xi - b) * (xi - c) * (xi - d) * (xi - e)) / ((a - b) * (a - c) * (a - d) * (a - e))) + \
               fb * (
                       ((xi - a) * (xi - c) * (xi - d) * (xi - e)) / ((b - a) * (b - c) * (b - d) * (b - e))) + \
               fc * (
                       ((xi - a) * (xi - b) * (xi - d) * (xi - e)) / ((c - a) * (c - b) * (c - d) * (c - e))) + \
               fd * (
                       ((xi - a) * (xi - b) * (xi - c) * (xi - e)) / ((d - a) * (d - b) * (d - c) * (d - e))) + \
               fe * (
                       ((xi - a) * (xi - b) * (xi - c) * (xi - d)) / ((e - a) * (e - b) * (e - c) * (e - d)))
        if check:
            worksheet.write(row, col + 2, ans1)
            worksheet.write(row, col + 3, ans2)
        answer.append(ans1)
        answer.append(ans2)
    if check:
        workbook.close()
    return answer
