import xlsxwriter


def five_point(a, b, c, d, e, fa, fb, fc, fd, fe, excel, check):
    answer = list()
    row = 0
    col = 0
    df1, df3, df5 = 0, 0, 0
    this_dict = {
        a: fa,
        b: fb,
        c: fc,
        d: fd,
        e: fe
    }
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'x')
        worksheet.write(row, col+1, 'f(x)')
        worksheet.write(row, col+2, 'f\'(x)')
        row += 1
    h = b-a
    df1 = (1 / (12 * h)) * (-25*this_dict[a] + 48*this_dict[round(a+h, 2)] - 36*this_dict[round(a+2*h, 2)] +
                            16*this_dict[round(a+3*h, 2)] - 3*this_dict[round(a+4*h, 2)])
    h = d-c
    df3 = (1 / (12 * h)) * (this_dict[round(c-2*h, 2)] - 8 * this_dict[round(c-h, 2)] + 8 * this_dict[round(c+h, 2)] -
                            this_dict[round(c+2*h, 2)])
    h = d-e
    df5 = (1 / (12 * h)) * (-25*this_dict[e] + 48*this_dict[round(e+h, 2)] - 36*this_dict[round(e+2*h, 2)] +
                            16*this_dict[round(e+3*h, 2)] - 3*this_dict[round(e+4*h, 2)])
    answer.append(df1)
    answer.append(df3)
    answer.append(df5)
    if check:
        worksheet.write(row, col, a)
        worksheet.write(row+1, col, b)
        worksheet.write(row+2, col, c)
        worksheet.write(row+3, col, d)
        worksheet.write(row, col+1, fa)
        worksheet.write(row+1, col+1, fb)
        worksheet.write(row+2, col+1, fc)
        worksheet.write(row+3, col+1, fd)
        worksheet.write(row, col+2, df1)
        worksheet.write(row+2, col+2, df3)
        worksheet.write(row+4, col, e)
        worksheet.write(row+4, col+1, fe)
        worksheet.write(row+4, col+2, df5)
        workbook.close()
    return answer
