import xlsxwriter


def f_b_d(a, b, c, fa, fb, fc, excel, check):
    row = 0
    col = 0
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'x')
        worksheet.write(row, col+1, 'f(x)')
        worksheet.write(row, col+2, 'f\'(x)')
        row += 1
    ans = []
    x1 = (fb - fa)/(b - a)
    x2 = (fc - fb)/(c - b)
    x3 = (fa - fb)/(a - b)
    x4 = (fb - fc)/(b - c)
    ans.append(x1)
    if x2 > x3:
        ans.append(x2)
    else:
        ans.append(x3)
    ans.append(x4)
    if check:
        worksheet.write(row, col, a)
        worksheet.write(row+1, col, b)
        worksheet.write(row+2, col, c)
        worksheet.write(row, col+1, fa)
        worksheet.write(row+1, col+1, fb)
        worksheet.write(row+2, col+1, fc)
        worksheet.write(row, col+2, ans[0])
        worksheet.write(row+1, col+2, ans[1])
        worksheet.write(row+2, col+2, ans[2])
        workbook.close()
    return ans
