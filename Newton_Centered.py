import xlsxwriter


def func(xi, xj, fxi, fxj):
    return (fxi - fxj)/(xi-xj)


def func2(xi, xj, xk, fxi, fxj, fxk):
    return (func(xi, xj, fxi, fxj)-func(xj, xk, fxj, fxk))/(xi-xk)


def func3(xi, xj, xk, xl, fxi, fxj, fxk, fxl):
    return (func2(xi, xj, xk, fxi, fxj, fxk)-func2(xj, xk, xl, fxj, fxk, fxl))/(xi-xl)


def func4(xi, xj, xk, xl, xm, fxi, fxj, fxk, fxl, fxm):
    return (func3(xi, xj, xk, xl, fxi, fxj, fxk, fxl)-func3(xj, xk, xl, xm, fxj, fxk, fxl, fxm))/(xi-xm)


def center(a, b, c, d, e, fa, fb, fc, fd, fe, xi, excel, check):
    answer = list()
    row = 0
    col = 0
    p4 = 0
    worksheet = 0
    workbook = 0
    cell_format = 0
    if check:
        workbook = xlsxwriter.Workbook(excel + '.xlsx')
        worksheet = workbook.add_worksheet()
        cell_format = workbook.add_format({'bold': True, 'underline': True, 'font_color': 'red'})
        worksheet.write(row, col, 'P1')
        worksheet.write(row, col + 1, 'P2')
        worksheet.write(row, col + 2, 'P3')
        worksheet.write(row, col + 3, 'P4')
    f1a = func(b, c, fb, fc)
    f1b = func(c, d, fc, fd)
    f2 = func2(b, c, d, fb, fc, fd)
    f3a = func3(a, b, c, d, fa, fb, fc, fd)
    f3b = func3(b, c, d, e, fb, fc, fd, fe)
    f4 = func4(a, b, c, d, e, fa, fb, fc, fd, fe)
    h = b - a
    s = (xi - c)/h
    # 1st Order:
    p1 = fc + s*(h/2)*(f1a+f1b)
    # 2nd Order:
    p2 = p1 + s**2*h**2*f2
    # 3rd Order:
    p3 = p2 + (s/2)*((s**2)-1)*h**3*(f3a+f3b)
    # 4th Order:
    p4 = p3 + s**2*(s**2-1)*h**4*f4
    answer.append(p1)
    answer.append(p2)
    answer.append(p3)
    answer.append(p4)
    if check:
        worksheet.write(row, col, p1)
        worksheet.write(row, col + 1, p2)
        worksheet.write(row, col + 2, p3)
        worksheet.write(row, col + 3, p4)
        row += 5
        worksheet.write(row, col, a)
        worksheet.write(row + 2, col, b)
        worksheet.write(row + 4, col, c)
        worksheet.write(row + 6, col, d)
        worksheet.write(row + 8, col, e)
        worksheet.write(row, col + 1, fa)
        worksheet.write(row + 2, col + 1, fb)
        worksheet.write(row + 4, col + 1, fc, cell_format)
        worksheet.write(row + 6, col + 1, fd)
        worksheet.write(row + 8, col + 1, fe)
        worksheet.write(row + 1, col + 2, func(a, b, fa, fb))
        worksheet.write(row + 3, col + 2, func(b, c, fb, fc), cell_format)
        worksheet.write(row + 5, col + 2, func(c, d, fc, fd), cell_format)
        worksheet.write(row + 7, col + 2, func(d, e, fd, fe))
        worksheet.write(row + 2, col + 3, func2(a, b, c, fa, fb, fc))
        worksheet.write(row + 4, col + 3, func2(b, c, d, fb, fc, fd), cell_format)
        worksheet.write(row + 6, col + 3, func2(c, d, e, fc, fd, fe))
        worksheet.write(row + 3, col + 4, func3(a, b, c, d, fa, fb, fc, fd), cell_format)
        worksheet.write(row + 5, col + 4, func3(b, c, d, e, fb, fc, fd, fe), cell_format)
        worksheet.write(row + 4, col + 5, func4(a, b, c, d, e, fa, fb, fc, fd, fe), cell_format)
        workbook.close()
    return answer
