import xlsxwriter


def sec_deriv(a, b, c, d, e, f, fa, fb, fc, fd, fe, ff, excel, check):
    answer = list()
    row = 0
    col = 0
    df4, df5, df6 = 0, 0, 0
    this_dict = {
        a: fa,
        b: fb,
        c: fc,
        d: fd
    }
    flag1 = False
    flag2 = False
    if e != '' and f == '':
        flag1 = True
        try:
            e = float(e)
            fe = float(fe)
        except ValueError:
            return -2
        this_dict[e] = fe
    elif e != '' and f != '':
        flag2 = True
        try:
            e = float(e)
            fe = float(fe)
            f = float(f)
            ff = float(ff)
        except ValueError:
            return -2
        this_dict[e] = fe
        this_dict[f] = ff
    worksheet = 0
    workbook = 0
    if check:
        workbook = xlsxwriter.Workbook(excel+'.xlsx')
        worksheet = workbook.add_worksheet()
        worksheet.write(row, col, 'x')
        worksheet.write(row, col+1, 'f(x)')
        worksheet.write(row, col+2, 'f\'\'(x)')
        row += 1
    # x1:
    h = round(b - a, 1)
    df1 = (1 / (h * h)) * (2 * this_dict[a] - 5 * this_dict[round(a + h, 2)] + 4 * this_dict[round(a + 2 * h, 2)] -
                           this_dict[round(a + 3 * h)])
    # x2:
    h = round(c - b, 1)
    df2 = (1 / (h * h)) * (this_dict[round(b - h, 2)] - 2 * this_dict[b] + this_dict[round(b + h, 2)])
    # x3:
    h = round(d - c, 1)
    df3 = (1 / (h * h)) * (this_dict[round(c - h, 2)] - 2 * this_dict[c] + this_dict[round(c + h, 2)])
    answer.append(df1)
    answer.append(df2)
    answer.append(df3)
    if flag2:
        h = round(e - d, 1)
        df4 = (1 / (h * h)) * (this_dict[round(d - h, 2)] - 2 * this_dict[d] + this_dict[round(d + h, 2)])
        h = round(f - e, 1)
        df5 = (1 / (h * h)) * (this_dict[round(e - h, 2)] - 2 * this_dict[e] + this_dict[round(e + h, 2)])
        h = round(e - f, 1)
        df6 = (1 / (h * h)) * (2 * this_dict[f] - 5 * this_dict[round(f + h, 2)] + 4 * this_dict[round(f + 2 * h, 2)] -
                               this_dict[round(f + 3 * h)])
        answer.append(df4)
        answer.append(df5)
        answer.append(df6)
    elif flag1:
        h = e - d
        df4 = (1 / (h * h)) * (this_dict[round(d - h, 2)] - 2 * this_dict[d] + this_dict[round(d + h, 2)])
        h = d - e
        df5 = (1 / (h * h)) * (2 * this_dict[e] - 5 * this_dict[round(e + h, 2)] + 4 * this_dict[round(e + 2 * h, 2)] -
                               this_dict[round(e + 3 * h)])
        answer.append(df4)
        answer.append(df5)
    else:
        h = c - d
        df4 = (1 / (h * h)) * (2 * this_dict[d] - 5 * this_dict[round(d + h, 2)] + 4 * this_dict[round(d + 2 * h, 2)] -
                               this_dict[round(d + 3 * h)])
        answer.append(df4)
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
        worksheet.write(row+1, col+2, df2)
        worksheet.write(row+2, col+2, df3)
        worksheet.write(row+3, col+2, df4)
        if flag1 and not flag2:
            worksheet.write(row+4, col, e)
            worksheet.write(row+4, col+1, fe)
            worksheet.write(row+4, col+2, df5)
        elif flag2 and not flag1:
            worksheet.write(row+4, col, e)
            worksheet.write(row+4, col+1, fe)
            worksheet.write(row+4, col+2, df5)
            worksheet.write(row+5, col, f)
            worksheet.write(row+5, col+1, ff)
            worksheet.write(row+5, col+2, df6)
        workbook.close()
    return answer
