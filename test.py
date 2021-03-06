# from sympy import Matrix, matrix2numpy
# import Crout_imp
# # M = [[2, 3, -1, 2], [4, 4, -1, -1], [-2, -3, 4, 1]]
# # M = [[1, -1, 0, 0], [-2, 4, -2, -1], [0, -1, 2, 1.5]]
# M = [[0.5, 0.25, 0, 0, 0.35], [0.35, 0.8, 0.4, 0, 0.77], [0, 0.25, 1, 0.5, -0.5], [0, 0, 1, -2, -2.25]]
# # M = [[10, 2, -1, 27], [-3, -6, 2, -61.5], [1, 1, 5, -21.5]]
# M = Matrix(M)
# A, B = M[:, :-1], M[:, -1]
# A = A.tolist()
# # print(A)
# # print(B)
# L, U = Crout_imp.Crout(A)
# B = Matrix(B)
# L = Matrix(L)
# U = Matrix(U)
# y = L.inv()*B
# x = U.inv()*y
# L = matrix2numpy(L)
# U = matrix2numpy(U)
# x = matrix2numpy(x)
# print(L)
# print(U)
# # print(y)
# print(x)
2*x1+3*x2-x3-2
4*x1+4*x2-x3+1
-2*x1-3*x2+4*x3-1