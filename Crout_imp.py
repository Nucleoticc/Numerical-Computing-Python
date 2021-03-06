

def Crout(A):

    n = len(A)
    L = [[0] * n for i in range(n)]
    U = [[0] * n for i in range(n)]

    for j in range(n):
        for i in range(j, n):
            summ = 0
            for k in range(j):
                summ += L[i][k]*U[k][j]
            L[i][j] = A[i][j] - summ
        for i in range(j, n):
            summ = 0
            for k in range(j):
                summ += L[j][k]*U[k][i]
            if L[j][j] == 0:
                return
            U[j][i] = (A[j][i] - summ)/L[j][j]

    return L, U
