import threading
import time
import tkinter as tk
from PIL import ImageTk, Image
from ttkwidgets import frames as tkwf
from ttkthemes import ThemedStyle
from tkinter import ttk, messagebox
# ----------------------------- Method Libraries --------------------------------
import Bisection
import Newton_Raphson
import Newton_Raphson_acc
import Secant
import Reg_falsi
import lagrange
import Lagrange_nofunc
import Newton_Divided
import Newton_Centered
import Newton_Forward
import Newton_Backward
import Three_Point
import Five_Point
import Composite_Trapezoidal
import Composite_Simpson
import Composite_Midpoint
import Euler
import M_euler
import Differential_MidPoint
import Heun
import Rk_4
import Jacobi
import Gauss_Siedel
import LU
import LDL
import Crout
import Cholesky
import Fwd_Bck_Differential
import Rk_2
import Rk_3
import Rk_4_DE
import Second_Deriv
import lagrange_v2


# -------------------------------------------------------------------------------


class nc_meta(tk.Tk):
    def __init__(self):
        # -------------- List Variables ----------------------------
        self.matrix = []
        self.entries = []
        # -------------- Tkinter Declaration ----------------------------
        tk.Tk.__init__(self)
        self.base = ttk.Frame(self)
        self.base.place(relheight=1, relwidth=1)
        # ------------------Integer Entry Fields------------------------
        self.entry_a = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_a, 'Value Input Field', 'Initial, a or x0', timeout=0.46)
        self.entry_b = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_b, 'Value Input Field', 'Final, b or x1', timeout=0.46)
        self.entry_c = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_c, 'Value Input Field', 'c or x2', timeout=0.46)
        self.entry_d = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_d, 'Value Input Field', 'd or x3', timeout=0.46)
        self.entry_e = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_e, 'Value Input Field', 'e or x4', timeout=0.46)
        self.entry_f = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_f, 'Value Input Field', 'f or x5', timeout=0.46)
        self.entries.append(self.entry_a)
        self.entries.append(self.entry_b)
        self.entries.append(self.entry_c)
        self.entries.append(self.entry_d)
        self.entries.append(self.entry_e)
        self.entries.append(self.entry_f)
        # -----------------------Iteration Values---------------------------------
        self.entry_iter = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_iter, 'Optional Input Field', 'Number of Iterations', timeout=0.46)
        self.entry_acc = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_acc, 'Optional Input Field', 'Accuracy of 10^-', timeout=0.46)
        self.entries.append(self.entry_iter)
        self.entries.append(self.entry_acc)
        # -----------------------Initial Values-----------------------------------
        self.entry_xi = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_xi, 'Optional Input Field', 'xi or f(x) - Given intermediate value', timeout=0.46)
        self.entry_h = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_h, 'Optional Input Field', 'h -> (b-a)/n', timeout=0.46)
        self.entry_n = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_n, 'Optional Input Field', 'n -> (b-a)/h', timeout=0.46)
        self.entries.append(self.entry_xi)
        self.entries.append(self.entry_h)
        self.entries.append(self.entry_n)
        # ------------------------- Function -----------------------------------
        self.entry_func1 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_func1, 'Function Input Field', 'Function 1\nConvert Equation to Expression before '
                                                               'entering', timeout=0.46)
        self.entry_func2 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_func2, 'Function Input Field', 'Function 2\nConvert Equation to Expression before '
                                                               'entering', timeout=0.46)
        self.entry_func3 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_func3, 'Function Input Field', 'Function 3\nConvert Equation to Expression before '
                                                               'entering', timeout=0.46)
        self.entry_func4 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_func4, 'Function Input Field', 'Function 4\nConvert Equation to Expression before '
                                                               'entering', timeout=0.46)
        self.entry_func5 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_func5, 'Function Input Field', 'Function 5\nConvert Equation to Expression before '
                                                               'entering', timeout=0.46)
        self.entry_func6 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_func6, 'Function Input Field', 'Function 6\nConvert Equation to Expression before '
                                                               'entering', timeout=0.46)
        self.entries.append(self.entry_func1)
        self.entries.append(self.entry_func2)
        self.entries.append(self.entry_func3)
        self.entries.append(self.entry_func4)
        self.entries.append(self.entry_func5)
        self.entries.append(self.entry_func6)
        # ------------------------- Function -----------------------------------
        self.entry_f1 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_f1, 'Function Value Input Field', 'F(x0)', timeout=0.46)
        self.entry_f2 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_f2, 'Function Value Input Field', 'F(x1)', timeout=0.46)
        self.entry_f3 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_f3, 'Function Value Input Field', 'F(x2)', timeout=0.46)
        self.entry_f4 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_f4, 'Function Value Input Field', 'F(x3)', timeout=0.46)
        self.entry_f5 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_f5, 'Function Value Input Field', 'F(x4)', timeout=0.46)
        self.entry_f6 = ttk.Entry(self.base, state='disabled')
        tkwf.Balloon(self.entry_f6, 'Function Value Input Field', 'F(x5)', timeout=0.46)
        self.entries.append(self.entry_f1)
        self.entries.append(self.entry_f2)
        self.entries.append(self.entry_f3)
        self.entries.append(self.entry_f4)
        self.entries.append(self.entry_f5)
        self.entries.append(self.entry_f6)
        # -------------------------- Extra Features --------------------------
        self.matrix_x = ttk.Combobox(self.base, state="readonly", width=1)
        self.matrix_x['values'] = ('3', '4', '5', '6')
        self.matrix_x.current(0)
        self.matrix_y = ttk.Combobox(self.base, state="readonly", width=1)
        self.matrix_y['values'] = ('3', '4', '5', '6', '7')
        self.matrix_y.current(0)
        self.matrix_choice = ttk.Button(self.base, text='Input Matrix', state='disabled',
                                        command=self.matrice)
        self.clear_matrix = ttk.Button(self.base, text="Reset Matrix", command=lambda: self.matrix.clear())
        self.check, self.simpson = tk.IntVar(), tk.IntVar()
        self.entry_excel = ttk.Entry(self.base, state='disabled')
        self.excel_print = ttk.Checkbutton(self.base, variable=self.check, text="Print table to Excel?",
                                           command=self.enable_excel)
        self.simpson_third = ttk.Checkbutton(self.base, variable=self.simpson, state='disabled',
                                             text="3/8?")
        tkwf.Balloon(self.simpson_third, 'Simpson Method', 'Use Simpson 3/8', timeout=0.46)
        # -------------------------- Method Variables --------------------------
        self.choice = tk.IntVar()
        # ------------------------- Method Checkboxes --------------------------
        self.bisect_cb = ttk.Radiobutton(self.base, variable=self.choice, value=1, text="Bisection",
                                         command=self.enable_simpson)
        tkwf.Balloon(self.bisect_cb, 'Methods', 'Bisection\nInputs Required:\nField x0/a, Field x1/b, Field function '
                                                '1\nEither Accuracy or Iteration Field', timeout=0.46)
        self.raphson_cb = ttk.Radiobutton(self.base, variable=self.choice, value=2, text="Raphson",
                                          command=self.enable_simpson)
        tkwf.Balloon(self.raphson_cb, 'Methods', 'Raphson\nInputs Required:\nField x0/a, Field function '
                                                 '1\nEither Accuracy or Iteration Field', timeout=0.46)
        self.secant_cb = ttk.Radiobutton(self.base, variable=self.choice, value=3, text="Secant",
                                         command=self.enable_simpson)
        tkwf.Balloon(self.secant_cb, 'Methods', 'Secant\nInputs Required:\nField x0/a, Field x1/b, Field function '
                                                '1,\nIteration Field', timeout=0.46)
        self.falsi_cb = ttk.Radiobutton(self.base, variable=self.choice, value=4, text="Falsi",
                                        command=self.enable_simpson)
        tkwf.Balloon(self.falsi_cb, 'Methods',
                     'Reguler Falsi\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1,\nIteration Field', timeout=0.46)
        self.lagrang_cb = ttk.Radiobutton(self.base, variable=self.choice, value=5, text="Lagrange",
                                          command=self.enable_simpson)
        tkwf.Balloon(self.lagrang_cb, 'Methods',
                     'Lagrange\nOption1: Field x0/a, Field x1/b, Field x2/c, Field function '
                     '1, Field xi, Optional: Field x3/d\nOption2: Field x0/a, Field x1/b, '
                     'Field x2/c, Field f(x0), Field f(x1), Field f(x2), Field xi, Optional: Field x3/d, '
                     'Field f(x3), Field x4/e, Field f(x4) ', width=700, timeout=0.46)
        self.uneq_lagrang_cb = ttk.Radiobutton(self.base, variable=self.choice, value=31, text="Unequal Lagrange",
                                               command=self.enable_simpson)
        tkwf.Balloon(self.uneq_lagrang_cb, 'Methods',
                     'Unequal Lagrange\nOption1: Field x0/a, Field x1/b, Field x2/c, Field function '
                     '1, Field xi, Optional: Field x3/d\nOption2: Field x0/a, Field x1/b, '
                     'Field x2/c, Field xi\nEither: Field f(x0), Field f(x1), Field f(x2) OR Field function 1',
                     width=700, timeout=0.46)
        self.divided_cb = ttk.Radiobutton(self.base, variable=self.choice, value=6, text="Divided Difference",
                                          command=self.enable_simpson)
        tkwf.Balloon(self.divided_cb, 'Methods',
                     'Divided Difference\nField x0/a, Field x1/b, '
                     'Field x2/c, Field x3/d, Field f(x0), Field f(x1), Field f(x2), Field f(x3), Field xi', width=700,
                     timeout=0.46)
        self.forward_cb = ttk.Radiobutton(self.base, variable=self.choice, value=7, text="Forward Difference",
                                          command=self.enable_simpson)
        tkwf.Balloon(self.forward_cb, 'Methods',
                     'Forward Difference\nField x0/a, Field x1/b, '
                     'Field x2/c, Field x3/d, Field x4/e, Field f(x0), Field f(x1), Field f(x2), Field f(x3), '
                     'Field f(x4), Field xi', width=700, timeout=0.46)
        self.backward_cb = ttk.Radiobutton(self.base, variable=self.choice, value=8, text="Backward Difference",
                                           command=self.enable_simpson)
        tkwf.Balloon(self.backward_cb, 'Methods',
                     'Backward Difference\nField x0/a, Field x1/b, '
                     'Field x2/c, Field x3/d, Field x4/e, Field f(x0), Field f(x1), Field f(x2), Field f(x3), '
                     'Field f(x4), Field xi', width=700, timeout=0.46)
        self.fwd_bck_cb = ttk.Radiobutton(self.base, variable=self.choice, value=26, text="Fwd/Bck (Ex 4.1)",
                                          command=self.enable_simpson)
        tkwf.Balloon(self.fwd_bck_cb, 'Methods',
                     'Forward and Backward (Exercise 4.1)\nField x0/a, Field x1/b, '
                     'Field x2/c, Field f(x0), Field f(x1), Field f(x2), Field xi', width=700, timeout=0.46)
        self.centered_cb = ttk.Radiobutton(self.base, variable=self.choice, value=9, text="Centered Difference",
                                           command=self.enable_simpson)
        tkwf.Balloon(self.centered_cb, 'Methods',
                     'Centered Difference\nField x0/a, Field x1/b, '
                     'Field x2/c, Field x3/d, Field x4/e, Field f(x0), Field f(x1), Field f(x2), Field f(x3), '
                     'Field f(x4), Field xi', width=700, timeout=0.46)
        self.threep_cb = ttk.Radiobutton(self.base, variable=self.choice, value=10, text="Three Point",
                                         command=self.enable_simpson)
        tkwf.Balloon(self.threep_cb, 'Methods',
                     'Three Point\nField x0/a, Field x1/b, '
                     'Field x2/c, Field x3/d, Field f(x0), Field f(x1), Field f(x2), Field f(x3)\nOptional: '
                     'Field x4/e, Field f(x4), Field x5/f, Field f(x5)', width=700, timeout=0.46)
        self.sec_deriv_cb = ttk.Radiobutton(self.base, variable=self.choice, value=30, text="Second Derivative",
                                            command=self.enable_simpson)
        tkwf.Balloon(self.sec_deriv_cb, 'Methods',
                     'Three Point\nField x0/a, Field x1/b, '
                     'Field x2/c, Field x3/d, Field f(x0), Field f(x1), Field f(x2), Field f(x3)\nOptional: '
                     'Field x4/e, Field f(x4), Field x5/f, Field f(x5)', width=700, timeout=0.46)
        self.fivep_cb = ttk.Radiobutton(self.base, variable=self.choice, value=11, text="Five Point",
                                        command=self.enable_simpson)
        tkwf.Balloon(self.fivep_cb, 'Methods',
                     'Five Point\nField x0/a, Field x1/b, '
                     'Field x2/c, Field x3/d, Field x4/e, Field f(x0), Field f(x1), Field f(x2), Field f(x3), '
                     'Field f(x4)', width=700, timeout=0.46)
        self.trapezoidal_cb = ttk.Radiobutton(self.base, variable=self.choice, value=12, text="Trapezoidal",
                                              command=self.enable_simpson)
        tkwf.Balloon(self.trapezoidal_cb, 'Methods',
                     'Trapezoidal\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1\nEither n or h Field', width=400, timeout=0.46)
        self.simpson_s_cb = ttk.Radiobutton(self.base, variable=self.choice, value=13, text="Simpson",
                                            command=self.enable_simpson)
        tkwf.Balloon(self.simpson_s_cb, 'Methods',
                     'Simpson\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1\nEither n or h Field', width=400, timeout=0.46)
        self.midpoint_cb = ttk.Radiobutton(self.base, variable=self.choice, value=14, text="Midpoint",
                                           command=self.enable_simpson)
        tkwf.Balloon(self.midpoint_cb, 'Methods',
                     'Midpoint\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1\nEither n or h Field', width=400, timeout=0.46)
        self.euler_cb = ttk.Radiobutton(self.base, variable=self.choice, value=15, text="Euler",
                                        command=self.enable_simpson)
        tkwf.Balloon(self.euler_cb, 'Methods',
                     'Euler\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1, Field xi\nEither n or h Field\nOptional: Field function 2', width=400, timeout=0.46)
        self.m_euler_cb = ttk.Radiobutton(self.base, variable=self.choice, value=16, text="Modified Euler",
                                          command=self.enable_simpson)
        tkwf.Balloon(self.m_euler_cb, 'Methods',
                     'Modified Euler\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1, Field xi\nEither n or h Field\nOptional: Field function 2', width=400, timeout=0.46)
        self.d_midpoint_cb = ttk.Radiobutton(self.base, variable=self.choice, value=17, text="Differential Midpoint",
                                             command=self.enable_simpson)
        tkwf.Balloon(self.d_midpoint_cb, 'Methods',
                     'Differential Midpoint\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1, Field xi\nEither n or h Field\nOptional: Field function 2', width=400, timeout=0.46)
        self.heun_cb = ttk.Radiobutton(self.base, variable=self.choice, value=18, text="Heun",
                                       command=self.enable_simpson)
        tkwf.Balloon(self.heun_cb, 'Methods',
                     'Heun\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1, Field xi\nEither n or h Field\nOptional: Field function 2', width=400, timeout=0.46)
        self.rk_4_cb = ttk.Radiobutton(self.base, variable=self.choice, value=19, text="Runge Kutta 4",
                                       command=self.enable_simpson)
        tkwf.Balloon(self.rk_4_cb, 'Methods',
                     'Runge Kutta order 4 (Mandatory: XDDDD)\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1, Field xi\nEither n or h Field\nOptional: Field function 2', width=400, timeout=0.46)
        self.rk_2_cb = ttk.Radiobutton(self.base, variable=self.choice, value=27, text="Runge Kutta 2",
                                       command=self.enable_simpson)
        tkwf.Balloon(self.rk_2_cb, 'Methods',
                     'Runge Kutta order 2 (Mandatory: XDDDD)\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1, Field xi\nEither n or h Field\nOptional: Field function 2', width=400, timeout=0.46)
        self.rk_3_cb = ttk.Radiobutton(self.base, variable=self.choice, value=28, text="Runge Kutta 3",
                                       command=self.enable_simpson)
        tkwf.Balloon(self.rk_3_cb, 'Methods',
                     'Runge Kutta order 3 (Mandatory: XDDDD)\nInputs Required:\nField x0/a, Field x1/b, Field function '
                     '1, Field xi\nEither n or h Field\nOptional: Field function 2', width=400, timeout=0.46)
        self.rk_4_de_cb = ttk.Radiobutton(self.base, variable=self.choice, value=29, text="Rk 4 for DE",
                                          command=self.enable_simpson)
        tkwf.Balloon(self.rk_4_de_cb, 'Methods',
                     'Runge Kutta order 4 DE (Mandatory: XDDDD)\nInputs Required:\nField x0/a, Field x1/b, Field x2/c, Field function '
                     '1, Field xi, Field function 2\nEither n or h Field', width=400, timeout=0.46)
        self.jacobi_cb = ttk.Radiobutton(self.base, variable=self.choice, value=20, text="Jacobi",
                                         command=self.enable_simpson)
        tkwf.Balloon(self.jacobi_cb, 'Methods',
                     'Jacobi\nInputs Required:\nField a, Field b, Field c, Field Function1, Field Function2, Field Function3'
                     '\nOptional: Field Function1, Function2, Function3, Function4, Function5, Function6', width=400,
                     timeout=0.46)
        self.gauss_cb = ttk.Radiobutton(self.base, variable=self.choice, value=21, text="Gauss",
                                        command=self.enable_simpson)
        tkwf.Balloon(self.gauss_cb, 'Methods',
                     'Gauss\nInputs Required:\nField a, Field b, Field c, Field Function1, Field Function2, Field Function3'
                     '\nOptional: Field Function1, Function2, Function3, Function4, Field Function5, Field Function6',
                     width=400, timeout=0.46)
        self.lu_cb = ttk.Radiobutton(self.base, variable=self.choice, value=22, text="Doolittle LU",
                                     command=self.enable_simpson)
        tkwf.Balloon(self.lu_cb, 'Methods',
                     'LU\nInputs Required:\nEither Matrix or Field Function1, Field Function2, Field Function3'
                     '\nOptional: Field Function4, Field Function5, Field Function6', width=700, timeout=0.46)
        self.ldl_cb = ttk.Radiobutton(self.base, variable=self.choice, value=23, text="LDL",
                                      command=self.enable_simpson)
        tkwf.Balloon(self.ldl_cb, 'Methods',
                     'LU\nInputs Required:\nEither Matrix or Field Function1, Field Function2, Field Function3'
                     '\nOptional: Field Function4, Field Function5, Field Function6', width=700, timeout=0.46)
        self.cholesky_cb = ttk.Radiobutton(self.base, variable=self.choice, value=24, text="Cholesky",
                                           command=self.enable_simpson)
        tkwf.Balloon(self.cholesky_cb, 'Methods',
                     'LU\nInputs Required:\nEither Matrix or Field Function1, Field Function2, Field Function3'
                     '\nOptional: Field Function4, Field Function5, Field Function6', width=700, timeout=0.46)
        self.crout_cb = ttk.Radiobutton(self.base, variable=self.choice, value=25, text="Crout",
                                        command=self.enable_simpson)
        tkwf.Balloon(self.crout_cb, 'Methods',
                     'LU\nInputs Required:\nEither Matrix or Field Function1, Field Function2, Field Function3'
                     '\nOptional: Field Function4, Field Function5, Field Function6', width=700, timeout=0.46)
        self.compute = ttk.Button(self.base, state='disabled', text='Calculate', command=self.go)
        # -------------------------- Extra Features --------------------------
        if self.choice.get() == 13:
            self.simpson_third.configure(state='normal')
        else:
            self.simpson_third.configure(state='disabled')
        self.exit_button = ttk.Button(self.base, text="Exit", command=self.exit_app)
        self.update_var = tk.IntVar()
        self.entry_completion = ttk.Progressbar(self.base, variable=self.update_var, length=165)
        self.first_flag = True
        # -------------------------- Theme Selection ----------------------------------------
        ttk.Label(self.base, text="Value Entry Fields:").place(relx=0.01, rely=0.03)
        ttk.Label(self.base, text="Value x0:").place(relx=0.02, rely=0.07)
        self.entry_a.place(relx=0.07, rely=0.06)
        ttk.Label(self.base, text="Value x1:").place(relx=0.22, rely=0.07)
        self.entry_b.place(relx=0.27, rely=0.06)
        ttk.Label(self.base, text="Value x2:").place(relx=0.02, rely=0.14)
        self.entry_c.place(relx=0.07, rely=0.13)
        ttk.Label(self.base, text="Value x3:").place(relx=0.22, rely=0.14)
        self.entry_d.place(relx=0.27, rely=0.13)
        ttk.Label(self.base, text="Value x4:").place(relx=0.02, rely=0.21)
        self.entry_e.place(relx=0.07, rely=0.20)
        ttk.Label(self.base, text="Value x5:").place(relx=0.22, rely=0.21)
        self.entry_f.place(relx=0.27, rely=0.20)
        ttk.Label(self.base, text="Iteration:").place(relx=0.42, rely=0.07)
        self.entry_iter.place(relx=0.47, rely=0.06)
        ttk.Label(self.base, text="10^-: ").place(relx=0.62, rely=0.07)
        self.entry_acc.place(relx=0.67, rely=0.06)
        ttk.Label(self.base, text="Value xi:").place(relx=0.42, rely=0.14)
        self.entry_xi.place(relx=0.47, rely=0.13)
        ttk.Label(self.base, text="Value h:").place(relx=0.62, rely=0.14)
        self.entry_h.place(relx=0.67, rely=0.13)
        ttk.Label(self.base, text="Value n:").place(relx=0.42, rely=0.21)
        self.entry_n.place(relx=0.47, rely=0.20)
        ttk.Label(self.base, text='Function Entry Fields: ').place(relx=0.01, rely=0.27)
        ttk.Label(self.base, text="Function 1:").place(relx=0.02, rely=0.31)
        self.entry_func1.place(relx=0.08, rely=0.30)
        ttk.Label(self.base, text="Function 2:").place(relx=0.22, rely=0.31)
        self.entry_func2.place(relx=0.28, rely=0.30)
        ttk.Label(self.base, text="Function 3:").place(relx=0.02, rely=0.38)
        self.entry_func3.place(relx=0.08, rely=0.37)
        ttk.Label(self.base, text="Function 4:").place(relx=0.22, rely=0.38)
        self.entry_func4.place(relx=0.28, rely=0.37)
        ttk.Label(self.base, text="Function 5:").place(relx=0.02, rely=0.45)
        self.entry_func5.place(relx=0.08, rely=0.44)
        ttk.Label(self.base, text="Function 6:").place(relx=0.22, rely=0.45)
        self.entry_func6.place(relx=0.28, rely=0.44)
        ttk.Separator(self.base, orient='vertical').place(relx=0.39, rely=0.27, relheight=0.24)
        ttk.Label(self.base, text='Function Value Fields: ').place(relx=0.41, rely=0.27)
        ttk.Label(self.base, text="Value f(x0):").place(relx=0.42, rely=0.31)
        self.entry_f1.place(relx=0.48, rely=0.30)
        ttk.Label(self.base, text="Value f(x1):").place(relx=0.64, rely=0.31)
        self.entry_f2.place(relx=0.70, rely=0.30)
        ttk.Label(self.base, text="Value f(x2):").place(relx=0.42, rely=0.38)
        self.entry_f3.place(relx=0.48, rely=0.37)
        ttk.Label(self.base, text="Value f(x3):").place(relx=0.64, rely=0.38)
        self.entry_f4.place(relx=0.70, rely=0.37)
        ttk.Label(self.base, text="Value f(x4):").place(relx=0.42, rely=0.45)
        self.entry_f5.place(relx=0.48, rely=0.44)
        ttk.Label(self.base, text="Value f(x5):").place(relx=0.64, rely=0.45)
        self.entry_f6.place(relx=0.70, rely=0.44)
        self.matrix_x.place(relx=0.02, rely=0.52)
        self.matrix_y.place(relx=0.06, rely=0.52)
        ttk.Label(self.base, text="X").place(relx=0.048, rely=0.54)
        self.matrix_choice.place(relx=0.02, rely=0.57)
        self.clear_matrix.place(relx=0.10, rely=0.57)
        ttk.Label(self.base, text="Excel File Name:").place(relx=0.19, rely=0.59)
        self.entry_excel.place(relx=0.27, rely=0.58)
        self.excel_print.place(relx=0.19, rely=0.53)
        self.simpson_third.place(relx=0.38, rely=0.71)
        ttk.Label(self.base, text='Methods: ').place(relx=0.01, rely=0.63)
        self.bisect_cb.place(relx=0.02, rely=0.66)
        self.raphson_cb.place(relx=0.02, rely=0.71)
        self.secant_cb.place(relx=0.02, rely=0.76)
        self.falsi_cb.place(relx=0.02, rely=0.81)
        self.lagrang_cb.place(relx=0.02, rely=0.86)
        self.divided_cb.place(relx=0.02, rely=0.91)
        ttk.Separator(self.base, orient='vertical').place(relx=0.15, rely=0.66, relheight=0.32)
        self.forward_cb.place(relx=0.16, rely=0.66)
        self.backward_cb.place(relx=0.16, rely=0.71)
        self.fwd_bck_cb.place(relx=0.16, rely=0.76)
        self.centered_cb.place(relx=0.16, rely=0.81)
        self.threep_cb.place(relx=0.16, rely=0.86)
        self.fivep_cb.place(relx=0.16, rely=0.91)
        ttk.Separator(self.base, orient='vertical').place(relx=0.29, rely=0.66, relheight=0.32)
        self.trapezoidal_cb.place(relx=0.30, rely=0.66)
        self.simpson_s_cb.place(relx=0.30, rely=0.71)
        self.midpoint_cb.place(relx=0.30, rely=0.76)
        self.euler_cb.place(relx=0.30, rely=0.81)
        self.m_euler_cb.place(relx=0.30, rely=0.86)
        self.d_midpoint_cb.place(relx=0.30, rely=0.91)
        ttk.Separator(self.base, orient='vertical').place(relx=0.43, rely=0.66, relheight=0.32)
        self.heun_cb.place(relx=0.44, rely=0.66)
        self.rk_4_cb.place(relx=0.44, rely=0.71)
        self.jacobi_cb.place(relx=0.44, rely=0.76)
        self.gauss_cb.place(relx=0.44, rely=0.81)
        self.lu_cb.place(relx=0.44, rely=0.86)
        self.ldl_cb.place(relx=0.44, rely=0.91)
        ttk.Separator(self.base, orient='vertical').place(relx=0.57, rely=0.66, relheight=0.32)
        self.cholesky_cb.place(relx=0.58, rely=0.66)
        self.crout_cb.place(relx=0.58, rely=0.71)
        self.sec_deriv_cb.place(relx=0.58, rely=0.76)
        self.uneq_lagrang_cb.place(relx=0.58, rely=0.81)
        self.rk_2_cb.place(relx=0.58, rely=0.86)
        self.rk_3_cb.place(relx=0.58, rely=0.91)
        ttk.Separator(self.base, orient='vertical').place(relx=0.71, rely=0.66, relheight=0.32)
        self.rk_4_de_cb.place(relx=0.72, rely=0.66)
        self.compute.place(relx=0.496, rely=0.52)
        self.exit_button.place(relx=0.92, rely=0.01)
        self.entry_completion.place(relx=0.47, rely=0.58)
        # -------------------------- Scrolled Frame ----------------------------------------------
        self.s_f = tkwf.ScrolledFrame(self.base, compound=tk.RIGHT, canvasheight=170)
        self.s_f.place(relx=0.72, rely=0.71)
        self.img1, self.img2, self.img3, self.img4, self.img5 = None, None, None, None, None
        # -------------------------- Threading ----------------------------------------------
        self.thread_flag = True
        self.t = threading.Thread(target=self.complete_entry)
        self.t.daemon = True

    # -------------------------- Extra Methods -------------------------------------
    @staticmethod
    def exit_app():
        if messagebox.askyesno('Exit', "Exit the application?"):
            messagebox.showinfo('Thanks', 'Program made by Nucleotic :)')
            on_closing()

    def reset(self):
        if self.first_flag:
            self.first_flag = False
            return
        cleared = True
        for e in self.entries:
            if e.get():
                cleared=False
        if not cleared:
            if messagebox.askyesno('NC', 'Clear All Entries?') == 1:
                for e in self.entries:
                    e.delete(0, 'end')
                    self.matrix.clear()
                    e.configure(state='disabled')
        else:
            for e in self.entries:
                e.configure(state='disabled')

    def enable_excel(self):
        if self.check.get():
            self.entry_excel.configure(state='normal')
        else:
            self.entry_excel.configure(state='disabled')

    def enable_simpson(self):
        if self.thread_flag:
            self.t.start()
            self.thread_flag = False
        if self.choice.get() == 13:
            self.simpson_third.configure(state='normal')
        else:
            self.simpson.set(0)
            self.simpson_third.configure(state='disabled')

    def matrice(self):
        x = int(self.matrix_x.get())
        y = int(self.matrix_y.get())
        mat = tk.Toplevel()
        mat.geometry('400x280')
        canv = ttk.Frame(mat)
        canv.place(relx=0, rely=0, relheight=0.85, relwidth=1)
        entry = {}
        for i in range(x):
            for j in range(y):
                index = (i, j)
                b = ttk.Entry(canv, width=4)
                b.grid(row=i, column=j, padx=(5, 5), pady=(5, 5))
                entry[index] = b
        for i in range(x):
            for j in range(y):
                index = (i, j)
                try:
                    entry[index].insert(0, self.matrix[i][j])
                except IndexError:
                    pass
        if y == 7:
            canv.grid_columnconfigure((0, 1, 2, 3, 4, 5, 6), weight=1)
        elif y == 6:
            canv.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        elif y == 5:
            canv.grid_columnconfigure((0, 1, 2, 3, 4), weight=1)
        elif y == 4:
            canv.grid_columnconfigure((0, 1, 2, 3), weight=1)
        else:
            canv.grid_columnconfigure((0, 1, 2), weight=1)
        ok = ttk.Button(mat, text="Set Values", command=lambda: self.set_matrix(x, y, entry, mat))
        ok.place(rely=0.85, relwidth=1, relheight=0.15)

    def set_matrix(self, x, y, entry, mat):
        self.matrix.clear()
        for i in range(x):
            current_row = []
            for j in range(y):
                index = (i, j)
                if entry[index].get():
                    current_row.append(entry[index].get())
                else:
                    current_row.append(int(0))
            self.matrix.append(current_row)
        mat.destroy()

    def complete_entry(self):
        while True:
            if self.choice.get() == 1:  # Bisection
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_iter.configure(state='normal')
                self.entry_acc.configure(state='normal')
                self.update_var.set(0)
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/Bisection.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                flag = [False, False, False, False]
                self.entry_completion['maximum'] = 4
                while self.choice.get() == 1:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_iter.get() and not self.entry_acc.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_acc.get() and not self.entry_iter.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_acc.get() and self.entry_iter.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_iter.get() and not self.entry_acc.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 2:  # Raphson
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_iter.configure(state='normal')
                self.entry_acc.configure(state='normal')
                flag = [False, False, False]
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/Raphson.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.update_var.set(0)
                self.entry_completion['maximum'] = 3
                while self.choice.get() == 2:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_func1.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_func1.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_iter.get() and not self.entry_acc.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif self.entry_acc.get() and not self.entry_iter.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif self.entry_acc.get() and self.entry_iter.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_iter.get() and not self.entry_acc.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 3:  # Secant
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_iter.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/Secant.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                flag = [False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 4
                while self.choice.get() == 3:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_iter.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_iter.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 4:  # Falsi
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_iter.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/Reg_Falsi.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                flag = [False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 4
                while self.choice.get() == 4:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_iter.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_iter.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 5:  # Lagrange
                q1 = messagebox.askyesno("Lagrange", "Will you be entering the equation/function?")
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/lagrange_1.png'))
                ttk.Label(self.s_f.interior, text='First Order').pack()
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                ttk.Label(self.s_f.interior, text='Second Order').pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/lagrange_2a.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/lagrange_2b.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img4 = ImageTk.PhotoImage(Image.open('Images/lagrange_2c.png'))
                ttk.Label(self.s_f.interior, image=self.img4).pack()
                if q1:
                    self.reset()
                    self.entry_a.configure(state='normal')
                    self.entry_b.configure(state='normal')
                    self.entry_c.configure(state='normal')
                    self.entry_d.configure(state='normal')
                    self.entry_e.configure(state='normal')
                    self.entry_xi.configure(state='normal')
                    self.entry_func1.configure(state='normal')
                    flag = [False, False, False, False, False]
                    self.update_var.set(0)
                    self.entry_completion['maximum'] = 5
                    while self.choice.get() == 5:
                        if self.entry_a.get() and not flag[0]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[0] = True
                        elif not self.entry_a.get() and flag[0]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[0] = False
                        if self.entry_b.get() and not flag[1]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[1] = True
                        elif not self.entry_b.get() and flag[1]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[1] = False
                        if self.entry_c.get() and not flag[2]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[2] = True
                        elif not self.entry_c.get() and flag[2]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[2] = False
                        if self.entry_func1.get() and not flag[3]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[3] = True
                        elif not self.entry_func1.get() and flag[3]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[3] = False
                        if self.entry_xi.get() and not flag[4]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[4] = True
                        elif not self.entry_xi.get() and flag[4]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[4] = False
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
                else:
                    self.reset()
                    self.entry_a.configure(state='normal')
                    self.entry_b.configure(state='normal')
                    self.entry_c.configure(state='normal')
                    self.entry_d.configure(state='normal')
                    self.entry_e.configure(state='normal')
                    self.entry_f1.configure(state='normal')
                    self.entry_f2.configure(state='normal')
                    self.entry_f3.configure(state='normal')
                    self.entry_f4.configure(state='normal')
                    self.entry_f5.configure(state='normal')
                    self.entry_xi.configure(state='normal')
                    flag = [False, False, False, False, False, False, False]
                    self.update_var.set(0)
                    self.entry_completion['maximum'] = 7
                    while self.choice.get() == 5:
                        if self.entry_a.get() and not flag[0]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[0] = True
                        elif not self.entry_a.get() and flag[0]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[0] = False
                        if self.entry_b.get() and not flag[1]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[1] = True
                        elif not self.entry_b.get() and flag[1]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[1] = False
                        if self.entry_c.get() and not flag[2]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[2] = True
                        elif not self.entry_c.get() and flag[2]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[2] = False
                        if self.entry_xi.get() and not flag[3]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[3] = True
                        elif not self.entry_xi.get() and flag[3]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[3] = False
                        if self.entry_f1.get() and not flag[4]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[4] = True
                        elif not self.entry_f1.get() and flag[4]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[4] = False
                        if self.entry_f2.get() and not flag[5]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[5] = True
                        elif not self.entry_f2.get() and flag[5]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[5] = False
                        if self.entry_f3.get() and not flag[6]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[6] = True
                        elif not self.entry_f3.get() and flag[6]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[6] = False
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
            elif self.choice.get() == 6:  # Divided Difference
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_d.configure(state='normal')
                self.entry_f1.configure(state='normal')
                self.entry_f2.configure(state='normal')
                self.entry_f3.configure(state='normal')
                self.entry_f4.configure(state='normal')
                self.entry_xi.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                ttk.Label(self.s_f.interior, text='f[xi, xj] Calculation Formula:').pack()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/newton_all.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/newton_all_2.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                ttk.Label(self.s_f.interior, text='Orders:').pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/div_a.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img4 = ImageTk.PhotoImage(Image.open('Images/div_b.png'))
                ttk.Label(self.s_f.interior, image=self.img4).pack()
                self.img5 = ImageTk.PhotoImage(Image.open('Images/div_c.png').resize((350, 19)))
                ttk.Label(self.s_f.interior, image=self.img5).pack()
                self.update_var.set(0)
                flag = [False, False, False, False, False, False, False, False, False]
                self.entry_completion['maximum'] = 9
                while self.choice.get() == 6:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_c.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_c.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_d.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_d.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    if self.entry_f1.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_f1.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_f2.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_f2.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    if self.entry_f3.get() and not flag[7]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[7] = True
                    elif not self.entry_f3.get() and flag[7]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[7] = False
                    if self.entry_f4.get() and not flag[8]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[8] = True
                    elif not self.entry_f4.get() and flag[8]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[8] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 7:  # Forward Difference
                self.reset()
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_d.configure(state='normal')
                self.entry_e.configure(state='normal')
                self.entry_f1.configure(state='normal')
                self.entry_f2.configure(state='normal')
                self.entry_f3.configure(state='normal')
                self.entry_f4.configure(state='normal')
                self.entry_f5.configure(state='normal')
                self.entry_xi.configure(state='normal')
                self.update_var.set(0)
                flag = [False, False, False, False, False, False, False, False, False, False, False]
                self.entry_completion['maximum'] = 11
                while self.choice.get() == 7:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_c.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_c.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_d.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_d.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    if self.entry_f1.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_f1.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_f2.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_f2.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    if self.entry_f3.get() and not flag[7]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[7] = True
                    elif not self.entry_f3.get() and flag[7]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[7] = False
                    if self.entry_f4.get() and not flag[8]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[8] = True
                    elif not self.entry_f4.get() and flag[8]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[8] = False
                    if self.entry_e.get() and not flag[9]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[9] = True
                    elif not self.entry_e.get() and flag[9]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[9] = False
                    if self.entry_f5.get() and not flag[10]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[10] = True
                    elif not self.entry_f5.get() and flag[10]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[10] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 8:  # Backward Difference
                self.reset()
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_d.configure(state='normal')
                self.entry_e.configure(state='normal')
                self.entry_f1.configure(state='normal')
                self.entry_f2.configure(state='normal')
                self.entry_f3.configure(state='normal')
                self.entry_f4.configure(state='normal')
                self.entry_f5.configure(state='normal')
                self.entry_xi.configure(state='normal')
                self.update_var.set(0)
                flag = [False, False, False, False, False, False, False, False, False, False, False]
                self.entry_completion['maximum'] = 11
                while self.choice.get() == 8:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_c.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_c.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_d.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_d.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    if self.entry_f1.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_f1.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_f2.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_f2.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    if self.entry_f3.get() and not flag[7]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[7] = True
                    elif not self.entry_f3.get() and flag[7]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[7] = False
                    if self.entry_f4.get() and not flag[8]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[8] = True
                    elif not self.entry_f4.get() and flag[8]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[8] = False
                    if self.entry_e.get() and not flag[9]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[9] = True
                    elif not self.entry_e.get() and flag[9]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[9] = False
                    if self.entry_f5.get() and not flag[10]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[10] = True
                    elif not self.entry_f5.get() and flag[10]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[10] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 9:  # Centered Difference
                self.reset()
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_d.configure(state='normal')
                self.entry_e.configure(state='normal')
                self.entry_f1.configure(state='normal')
                self.entry_f2.configure(state='normal')
                self.entry_f3.configure(state='normal')
                self.entry_f4.configure(state='normal')
                self.entry_f5.configure(state='normal')
                self.entry_xi.configure(state='normal')
                self.update_var.set(0)
                flag = [False, False, False, False, False, False, False, False, False, False, False]
                self.entry_completion['maximum'] = 11
                while self.choice.get() == 9:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_c.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_c.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_d.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_d.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    if self.entry_f1.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_f1.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_f2.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_f2.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    if self.entry_f3.get() and not flag[7]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[7] = True
                    elif not self.entry_f3.get() and flag[7]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[7] = False
                    if self.entry_f4.get() and not flag[8]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[8] = True
                    elif not self.entry_f4.get() and flag[8]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[8] = False
                    if self.entry_e.get() and not flag[9]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[9] = True
                    elif not self.entry_e.get() and flag[9]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[9] = False
                    if self.entry_f5.get() and not flag[10]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[10] = True
                    elif not self.entry_f5.get() and flag[10]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[10] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 10:  # Three Point
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_d.configure(state='normal')
                self.entry_e.configure(state='normal')
                self.entry_f.configure(state='normal')
                self.entry_f1.configure(state='normal')
                self.entry_f2.configure(state='normal')
                self.entry_f3.configure(state='normal')
                self.entry_f4.configure(state='normal')
                self.entry_f5.configure(state='normal')
                self.entry_f6.configure(state='normal')
                self.update_var.set(0)
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                ttk.Label(self.s_f.interior, text='End Point:').pack()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/three_epf.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                ttk.Label(self.s_f.interior, text='Mid Point:').pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/three_mpf.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                flag = [False, False, False, False, False, False, False, False]
                self.entry_completion['maximum'] = 8
                while self.choice.get() == 10:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_c.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_c.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_d.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_d.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_f1.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_f1.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_f2.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_f2.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    if self.entry_f3.get() and not flag[7]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[7] = True
                    elif not self.entry_f3.get() and flag[7]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[7] = False
                    if self.entry_f4.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_f4.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 11:  # Five point
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_d.configure(state='normal')
                self.entry_e.configure(state='normal')
                self.entry_f1.configure(state='normal')
                self.entry_f2.configure(state='normal')
                self.entry_f3.configure(state='normal')
                self.entry_f4.configure(state='normal')
                self.entry_f5.configure(state='normal')
                self.update_var.set(0)
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                ttk.Label(self.s_f.interior, text='End Point:').pack()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/five_epfa.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/five_epfb.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                ttk.Label(self.s_f.interior, text='Mid Point:').pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/five_mpf.png').resize((350, 47)))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                flag = [False, False, False, False, False, False, False, False, False, False]
                self.entry_completion['maximum'] = 10
                while self.choice.get() == 11:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_c.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_c.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_d.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_d.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_f1.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_f1.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_f2.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_f2.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    if self.entry_f3.get() and not flag[7]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[7] = True
                    elif not self.entry_f3.get() and flag[7]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[7] = False
                    if self.entry_f4.get() and not flag[8]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[8] = True
                    elif not self.entry_f4.get() and flag[8]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[8] = False
                    if self.entry_e.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_e.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    if self.entry_f5.get() and not flag[9]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[9] = True
                    elif not self.entry_f5.get() and flag[9]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[9] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 12:  # Trapezoidal
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/ctrap.png').resize((350, 43)))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                flag = [False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 4
                while self.choice.get() == 12:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 13:  # Simpson
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                flag = [False, False, False, False]
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                ttk.Label(self.s_f.interior, text='One-Third:').pack()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/csimpa.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/csimpb.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                ttk.Label(self.s_f.interior, text='Three-Eighth:').pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/csimp38a.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                self.img4 = ImageTk.PhotoImage(Image.open('Images/csimp38b.png'))
                ttk.Label(self.s_f.interior, image=self.img4).pack()
                self.update_var.set(0)
                self.entry_completion['maximum'] = 4
                while self.choice.get() == 13:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 14:  # Midpoint
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                flag = [False, False, False, False]
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/cmidpoint.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.update_var.set(0)
                self.entry_completion['maximum'] = 4
                while self.choice.get() == 14:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 15:  # euler
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                self.entry_xi.configure(state='normal')
                flag = [False, False, False, False, False]
                self.update_var.set(0)
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/Euler.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.entry_completion['maximum'] = 5
                while self.choice.get() == 15:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 16:  # Modified Euler
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                self.entry_xi.configure(state='normal')
                flag = [False, False, False, False, False]
                self.update_var.set(0)
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/Modified_euler.png').resize((350, 43)))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.entry_completion['maximum'] = 5
                while self.choice.get() == 16:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 17:  # Differential Midpoint
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                self.entry_xi.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/dmida.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/dmidb.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/dmidc.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                flag = [False, False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 5
                while self.choice.get() == 17:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 18:  # Heun
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                self.entry_xi.configure(state='normal')
                flag = [False, False, False, False, False]
                self.update_var.set(0)
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                ttk.Label(self.s_f.interior, text='Corrector:').pack()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/heun_correct.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                ttk.Label(self.s_f.interior, text='Predictor:').pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/heun_predict.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                self.entry_completion['maximum'] = 5
                while self.choice.get() == 18:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 19:  # Rk 4
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                self.entry_xi.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/rk_4_a.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/rk_4_b.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/rk_4_c.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                self.img4 = ImageTk.PhotoImage(Image.open('Images/rk_4_d.png'))
                ttk.Label(self.s_f.interior, image=self.img4).pack()
                self.img5 = ImageTk.PhotoImage(Image.open('Images/rk_4_e.png'))
                ttk.Label(self.s_f.interior, image=self.img5).pack()
                flag = [False, False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 5
                while self.choice.get() == 19:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 20:  # Jacobi
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_d.configure(state='normal')
                self.entry_e.configure(state='normal')
                self.entry_f.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_func3.configure(state='normal')
                self.entry_func4.configure(state='normal')
                self.entry_func5.configure(state='normal')
                self.entry_func6.configure(state='normal')
                self.entry_iter.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/j_g_1.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/j_g_2.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/j_g_3.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                self.img4 = ImageTk.PhotoImage(Image.open('Images/jacobi.png'))
                ttk.Label(self.s_f.interior, image=self.img4).pack()
                flag = [False, False, False, False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 7
                while self.choice.get() == 20:
                    if self.entry_func1.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_func1.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_func2.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_func2.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func3.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func3.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_iter.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_iter.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_a.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_a.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    if self.entry_b.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_b.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_c.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_c.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 21:  # Gauss Siedel
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_d.configure(state='normal')
                self.entry_e.configure(state='normal')
                self.entry_f.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_func3.configure(state='normal')
                self.entry_func4.configure(state='normal')
                self.entry_func5.configure(state='normal')
                self.entry_func6.configure(state='normal')
                self.entry_iter.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/j_g_1.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/j_g_2.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/j_g_3.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                self.img4 = ImageTk.PhotoImage(Image.open('Images/Gauss.png'))
                ttk.Label(self.s_f.interior, image=self.img4).pack()
                flag = [False, False, False, False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 7
                while self.choice.get() == 21:
                    if self.entry_func1.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_func1.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_func2.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_func2.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func3.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func3.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_iter.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_iter.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_a.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_a.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    if self.entry_b.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_b.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_c.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_c.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 22:  # LU
                self.reset()
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                q = messagebox.askyesno("NC", "Will you Enter Matrix?")
                if q == 1:
                    self.matrix_choice.configure(state='normal')
                    self.entry_completion['maximum'] = 1
                    while self.choice.get() == 22:
                        if self.matrix:
                            self.update_var.set(1)
                        else:
                            self.update_var.set(0)
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
                else:
                    self.entry_func1.configure(state='normal')
                    self.entry_func2.configure(state='normal')
                    self.entry_func3.configure(state='normal')
                    self.entry_func4.configure(state='normal')
                    self.entry_func5.configure(state='normal')
                    self.entry_func6.configure(state='normal')
                    flag = [False, False, False]
                    self.update_var.set(0)
                    self.entry_completion['maximum'] = 3
                    while self.choice.get() == 22:
                        if self.entry_func1.get() and not flag[0]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[0] = True
                        elif not self.entry_func1.get() and flag[0]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[0] = False
                        if self.entry_func2.get() and not flag[1]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[1] = True
                        elif not self.entry_func2.get() and flag[1]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[1] = False
                        if self.entry_func3.get() and not flag[2]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[2] = True
                        elif not self.entry_func3.get() and flag[2]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[2] = False
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
            elif self.choice.get() == 23:  # LDL
                self.reset()
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                q = messagebox.askyesno("NC", "Will you Enter Matrix?")
                if q == 1:
                    self.matrix_choice.configure(state='normal')
                    self.entry_completion['maximum'] = 1
                    while self.choice.get() == 23:
                        if self.matrix:
                            self.update_var.set(1)
                        else:
                            self.update_var.set(0)
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
                else:
                    self.entry_func1.configure(state='normal')
                    self.entry_func2.configure(state='normal')
                    self.entry_func3.configure(state='normal')
                    self.entry_func4.configure(state='normal')
                    self.entry_func5.configure(state='normal')
                    self.entry_func6.configure(state='normal')
                    flag = [False, False, False]
                    self.update_var.set(0)
                    self.entry_completion['maximum'] = 3
                    while self.choice.get() == 23:
                        if self.entry_func1.get() and not flag[0]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[0] = True
                        elif not self.entry_func1.get() and flag[0]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[0] = False
                        if self.entry_func2.get() and not flag[1]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[1] = True
                        elif not self.entry_func2.get() and flag[1]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[1] = False
                        if self.entry_func3.get() and not flag[2]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[2] = True
                        elif not self.entry_func3.get() and flag[2]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[2] = False
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
            elif self.choice.get() == 24:  # Cholesky
                self.reset()
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                q = messagebox.askyesno("NC", "Will you Enter Matrix?")
                if q == 1:
                    self.matrix_choice.configure(state='normal')
                    self.entry_completion['maximum'] = 1
                    while self.choice.get() == 24:
                        if self.matrix:
                            self.update_var.set(1)
                        else:
                            self.update_var.set(0)
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
                else:
                    self.entry_func1.configure(state='normal')
                    self.entry_func2.configure(state='normal')
                    self.entry_func3.configure(state='normal')
                    self.entry_func4.configure(state='normal')
                    self.entry_func5.configure(state='normal')
                    self.entry_func6.configure(state='normal')
                    flag = [False, False, False]
                    self.update_var.set(0)
                    self.entry_completion['maximum'] = 3
                    while self.choice.get() == 24:
                        if self.entry_func1.get() and not flag[0]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[0] = True
                        elif not self.entry_func1.get() and flag[0]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[0] = False
                        if self.entry_func2.get() and not flag[1]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[1] = True
                        elif not self.entry_func2.get() and flag[1]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[1] = False
                        if self.entry_func3.get() and not flag[2]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[2] = True
                        elif not self.entry_func3.get() and flag[2]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[2] = False
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
            elif self.choice.get() == 25:  # Crout
                self.reset()
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                q = messagebox.askyesno("NC", "Will you Enter Matrix?")
                if q == 1:
                    self.matrix_choice.configure(state='normal')
                    self.entry_completion['maximum'] = 1
                    while self.choice.get() == 25:
                        if self.matrix:
                            self.update_var.set(1)
                        else:
                            self.update_var.set(0)
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
                else:
                    self.entry_func1.configure(state='normal')
                    self.entry_func2.configure(state='normal')
                    self.entry_func3.configure(state='normal')
                    self.entry_func4.configure(state='normal')
                    self.entry_func5.configure(state='normal')
                    self.entry_func6.configure(state='normal')
                    flag = [False, False, False]
                    self.update_var.set(0)
                    self.entry_completion['maximum'] = 3
                    while self.choice.get() == 25:
                        if self.entry_func1.get() and not flag[0]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[0] = True
                        elif not self.entry_func1.get() and flag[0]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[0] = False
                        if self.entry_func2.get() and not flag[1]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[1] = True
                        elif not self.entry_func2.get() and flag[1]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[1] = False
                        if self.entry_func3.get() and not flag[2]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[2] = True
                        elif not self.entry_func3.get() and flag[2]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[2] = False
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
            elif self.choice.get() == 26:  # Ex 4.1
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_func3.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                ttk.Label(self.s_f.interior, text="Forward:").pack()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/fwd-diff.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                ttk.Label(self.s_f.interior, text="Backward:").pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/bckwd-diff.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                flag = [False, False, False, False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 6
                while self.choice.get() == 26:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_c.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_c.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_func1.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_func1.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_func2.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_func2.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    if self.entry_func3.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_func3.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 27:  # Rk 2
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                self.entry_xi.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/rk_2_a.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/rk_2_b.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/rk_2_c.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                flag = [False, False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 5
                while self.choice.get() == 27:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 28:  # Rk3
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                self.entry_xi.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/rk_3_a.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/rk_3_b.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/rk_3_c.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                self.img4 = ImageTk.PhotoImage(Image.open('Images/rk_3_d.png'))
                ttk.Label(self.s_f.interior, image=self.img4).pack()
                flag = [False, False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 5
                while self.choice.get() == 28:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 29:  # Rk 4 DE
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_func1.configure(state='normal')
                self.entry_func2.configure(state='normal')
                self.entry_n.configure(state='normal')
                self.entry_h.configure(state='normal')
                self.entry_xi.configure(state='normal')
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_k1.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_l1.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_k2.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img4 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_l2.png'))
                ttk.Label(self.s_f.interior, image=self.img4).pack()
                self.img5 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_k3.png'))
                ttk.Label(self.s_f.interior, image=self.img5).pack()
                img6 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_l3.png'))
                ttk.Label(self.s_f.interior, image=img6).pack()
                img7 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_k4.png'))
                ttk.Label(self.s_f.interior, image=img7).pack()
                img8 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_l4.png'))
                ttk.Label(self.s_f.interior, image=img8).pack()
                img9 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_a.png'))
                ttk.Label(self.s_f.interior, image=img9).pack()
                img10 = ImageTk.PhotoImage(Image.open('Images/rk_4_de_b.png'))
                ttk.Label(self.s_f.interior, image=img10).pack()
                flag = [False, False, False, False, False, False, False]
                self.update_var.set(0)
                self.entry_completion['maximum'] = 7
                while self.choice.get() == 29:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_func1.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_func1.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_n.get() and not self.entry_h.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and not self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif self.entry_h.get() and self.entry_n.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_n.get() and not self.entry_h.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_xi.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_xi.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    if self.entry_c.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_c.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_func2.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_func2.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 30:  # Second Derivative
                self.reset()
                self.entry_a.configure(state='normal')
                self.entry_b.configure(state='normal')
                self.entry_c.configure(state='normal')
                self.entry_d.configure(state='normal')
                self.entry_e.configure(state='normal')
                self.entry_f.configure(state='normal')
                self.entry_f1.configure(state='normal')
                self.entry_f2.configure(state='normal')
                self.entry_f3.configure(state='normal')
                self.entry_f4.configure(state='normal')
                self.entry_f5.configure(state='normal')
                self.entry_f6.configure(state='normal')
                self.update_var.set(0)
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                ttk.Label(self.s_f.interior, text="End Point")
                self.img1 = ImageTk.PhotoImage(Image.open('Images/sd_epf.png').resize((350, 43)))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                ttk.Label(self.s_f.interior, text="Mid Point")
                self.img3 = ImageTk.PhotoImage(Image.open('Images/sd_mpf.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                flag = [False, False, False, False, False, False, False, False]
                self.entry_completion['maximum'] = 8
                while self.choice.get() == 30:
                    if self.entry_a.get() and not flag[0]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[0] = True
                    elif not self.entry_a.get() and flag[0]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[0] = False
                    if self.entry_b.get() and not flag[1]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[1] = True
                    elif not self.entry_b.get() and flag[1]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[1] = False
                    if self.entry_c.get() and not flag[2]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[2] = True
                    elif not self.entry_c.get() and flag[2]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[2] = False
                    if self.entry_d.get() and not flag[3]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[3] = True
                    elif not self.entry_d.get() and flag[3]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[3] = False
                    if self.entry_f1.get() and not flag[5]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[5] = True
                    elif not self.entry_f1.get() and flag[5]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[5] = False
                    if self.entry_f2.get() and not flag[6]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[6] = True
                    elif not self.entry_f2.get() and flag[6]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[6] = False
                    if self.entry_f3.get() and not flag[7]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[7] = True
                    elif not self.entry_f3.get() and flag[7]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[7] = False
                    if self.entry_f4.get() and not flag[4]:
                        self.update_var.set(self.update_var.get() + 1)
                        flag[4] = True
                    elif not self.entry_f4.get() and flag[4]:
                        self.update_var.set(self.update_var.get() - 1)
                        flag[4] = False
                    self.update_idletasks()
                    time.sleep(0.2)
                    if self.entry_completion['maximum'] == self.entry_completion['value']:
                        self.compute.configure(state='normal')
                    else:
                        self.compute.configure(state='disabled')
            elif self.choice.get() == 31:  # Unequal Lagrange
                q1 = messagebox.askyesno("Lagrange", "Will you be entering the equation/function?")
                for w in self.s_f.interior.winfo_children():
                    w.destroy()
                self.img1 = ImageTk.PhotoImage(Image.open('Images/lagrange_v2_2a.png'))
                ttk.Label(self.s_f.interior, image=self.img1).pack()
                self.img3 = ImageTk.PhotoImage(Image.open('Images/lagrange_v2_2b.png'))
                ttk.Label(self.s_f.interior, image=self.img3).pack()
                self.img2 = ImageTk.PhotoImage(Image.open('Images/lagrange_v2_2c.png'))
                ttk.Label(self.s_f.interior, image=self.img2).pack()
                if q1:
                    self.reset()
                    self.entry_a.configure(state='normal')
                    self.entry_b.configure(state='normal')
                    self.entry_c.configure(state='normal')
                    self.entry_xi.configure(state='normal')
                    self.entry_func1.configure(state='normal')
                    flag = [False, False, False, False, False]
                    self.update_var.set(0)
                    self.entry_completion['maximum'] = 5
                    while self.choice.get() == 31:
                        if self.entry_a.get() and not flag[0]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[0] = True
                        elif not self.entry_a.get() and flag[0]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[0] = False
                        if self.entry_b.get() and not flag[1]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[1] = True
                        elif not self.entry_b.get() and flag[1]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[1] = False
                        if self.entry_c.get() and not flag[2]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[2] = True
                        elif not self.entry_c.get() and flag[2]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[2] = False
                        if self.entry_func1.get() and not flag[3]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[3] = True
                        elif not self.entry_func1.get() and flag[3]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[3] = False
                        if self.entry_xi.get() and not flag[4]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[4] = True
                        elif not self.entry_xi.get() and flag[4]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[4] = False
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')
                else:
                    self.reset()
                    self.entry_a.configure(state='normal')
                    self.entry_b.configure(state='normal')
                    self.entry_c.configure(state='normal')
                    self.entry_f1.configure(state='normal')
                    self.entry_f2.configure(state='normal')
                    self.entry_f3.configure(state='normal')
                    self.entry_xi.configure(state='normal')
                    flag = [False, False, False, False, False, False, False]
                    self.update_var.set(0)
                    self.entry_completion['maximum'] = 7
                    while self.choice.get() == 31:
                        if self.entry_a.get() and not flag[0]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[0] = True
                        elif not self.entry_a.get() and flag[0]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[0] = False
                        if self.entry_b.get() and not flag[1]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[1] = True
                        elif not self.entry_b.get() and flag[1]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[1] = False
                        if self.entry_c.get() and not flag[2]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[2] = True
                        elif not self.entry_c.get() and flag[2]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[2] = False
                        if self.entry_xi.get() and not flag[3]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[3] = True
                        elif not self.entry_xi.get() and flag[3]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[3] = False
                        if self.entry_f1.get() and not flag[4]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[4] = True
                        elif not self.entry_f1.get() and flag[4]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[4] = False
                        if self.entry_f2.get() and not flag[5]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[5] = True
                        elif not self.entry_f2.get() and flag[5]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[5] = False
                        if self.entry_f3.get() and not flag[6]:
                            self.update_var.set(self.update_var.get() + 1)
                            flag[6] = True
                        elif not self.entry_f3.get() and flag[6]:
                            self.update_var.set(self.update_var.get() - 1)
                            flag[6] = False
                        self.update_idletasks()
                        time.sleep(0.2)
                        if self.entry_completion['maximum'] == self.entry_completion['value']:
                            self.compute.configure(state='normal')
                        else:
                            self.compute.configure(state='disabled')

    # -------------------- Calculation Method -------------------------------------------------
    def go(self):
        excel = self.entry_excel.get()
        if self.choice.get() == 1:
            if excel == '':
                excel = 'bisection'
            try:
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                ans = Bisection.bisection(a, b, self.entry_func1.get(), self.entry_acc.get(),
                                          self.entry_iter.get(), excel, self.check.get())
                if ans != -1 and ans is not None:
                    messagebox.showinfo("Bisection", ans)
                elif ans == 1 and ans is not None:
                    messagebox.showerror("Bisection", "Root does not exist")
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 2:
            if excel == '':
                excel = 'raphson'
            try:
                ans = None
                a = float(self.entry_a.get())
                if self.entry_acc.get():
                    acc = int(self.entry_acc.get())
                    ans = Newton_Raphson_acc.raphson(a, self.entry_func1.get(),
                                                     acc, excel, self.check.get())
                elif self.entry_iter.get():
                    iterr = int(self.entry_iter.get())
                    ans = Newton_Raphson.raphson(a, self.entry_func1.get(),
                                                 iterr, excel, self.check.get())
                if ans is not None:
                    messagebox.showinfo("Raphson", ans)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 3:
            if excel == '':
                excel = 'secant'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                iterr = int(self.entry_iter.get())
                ans = Secant.secant(a, b, self.entry_func1.get(),
                                    iterr, excel, self.check.get())
                if ans is not None:
                    messagebox.showinfo("Secant", ans)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 4:
            if excel == '':
                excel = 'falsi'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                iterr = int(self.entry_iter.get())
                ans = Reg_falsi.reg_falsi(a, b, self.entry_func1.get(),
                                          iterr, excel, self.check.get())
                if ans != -1 and ans is not None:
                    messagebox.showinfo("Reg_Falsi", ans)
                elif ans == -1 and ans is not None:
                    messagebox.showerror('Reg Falsi', 'Root Doesnt Exist')
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 5:
            if excel == '':
                excel = 'Lagrange'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                xi = float(self.entry_xi.get())
                if self.entry_func1.get():
                    ans = lagrange.lagrange(a, b, c, self.entry_d.get(), self.entry_e.get(),
                                            xi, self.entry_func1.get(), excel, self.check.get())
                elif not self.entry_func1.get():
                    fa = float(self.entry_f1.get())
                    fb = float(self.entry_f2.get())
                    fc = float(self.entry_f3.get())
                    ans = Lagrange_nofunc.lagrange(a, b, c, self.entry_d.get(), self.entry_e.get(), fa, fb, fc,
                                                   self.entry_f4.get(), self.entry_f5.get(), xi, excel,
                                                   self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Lagrange", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 6:
            if excel == '':
                excel = 'Divided_Difference'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                d = float(self.entry_d.get())
                xi = float(self.entry_xi.get())
                fa = float(self.entry_f1.get())
                fb = float(self.entry_f2.get())
                fc = float(self.entry_f3.get())
                fd = float(self.entry_f4.get())
                ans = Newton_Divided.divided(a, b, c, d, self.entry_e.get(), fa, fb, fc, fd,
                                             self.entry_f5.get(), xi, excel,
                                             self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Divided_Difference", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 7:
            if excel == '':
                excel = 'Forward_Difference'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                d = float(self.entry_d.get())
                xi = float(self.entry_xi.get())
                fa = float(self.entry_f1.get())
                fb = float(self.entry_f2.get())
                fc = float(self.entry_f3.get())
                fd = float(self.entry_f4.get())
                ans = Newton_Forward.forward(a, b, c, d, self.entry_e.get(), fa, fb, fc, fd,
                                             self.entry_f5.get(), xi, excel,
                                             self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Forward_Difference", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 8:
            if excel == '':
                excel = 'Backward_Difference'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                d = float(self.entry_d.get())
                xi = float(self.entry_xi.get())
                fa = float(self.entry_f1.get())
                fb = float(self.entry_f2.get())
                fc = float(self.entry_f3.get())
                fd = float(self.entry_f4.get())
                ans = Newton_Backward.backward(a, b, c, d, self.entry_e.get(), fa, fb, fc, fd,
                                               self.entry_f5.get(), xi, excel,
                                               self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Backward_Difference", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 9:
            if excel == '':
                excel = 'Centered_Difference'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                d = float(self.entry_d.get())
                e = float(self.entry_e.get())
                xi = float(self.entry_xi.get())
                fa = float(self.entry_f1.get())
                fb = float(self.entry_f2.get())
                fc = float(self.entry_f3.get())
                fd = float(self.entry_f4.get())
                fe = float(self.entry_f5.get())
                ans = Newton_Centered.center(a, b, c, d, e, fa, fb, fc, fd,
                                             fe, xi, excel,
                                             self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Centered_Difference", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 10:
            if excel == '':
                excel = 'Three Point'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                d = float(self.entry_d.get())
                fa = float(self.entry_f1.get())
                fb = float(self.entry_f2.get())
                fc = float(self.entry_f3.get())
                fd = float(self.entry_f4.get())
                ans = Three_Point.three_point(a, b, c, d, self.entry_e.get(), self.entry_f.get(), fa, fb, fc, fd,
                                              self.entry_f5.get(), self.entry_f6.get(), excel,
                                              self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Three Point", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 11:
            if excel == '':
                excel = 'Five Point'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                d = float(self.entry_d.get())
                e = float(self.entry_e.get())
                fa = float(self.entry_f1.get())
                fb = float(self.entry_f2.get())
                fc = float(self.entry_f3.get())
                fd = float(self.entry_f4.get())
                fe = float(self.entry_f5.get())
                ans = Five_Point.five_point(a, b, c, d, e, fa, fb, fc, fd,
                                            fe, excel,
                                            self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Five Point", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 12:
            if excel == '':
                excel = 'Trapezoidal'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                ans = Composite_Trapezoidal.trapezoidal(a, b, self.entry_n.get(), self.entry_h.get(),
                                                        self.entry_func1.get(), excel,
                                                        self.check.get())
                if ans is not None:
                    messagebox.showinfo("Composite Trapezoidal", ans)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 13:
            if excel == '':
                excel = 'Simpson'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                ans = Composite_Simpson.simpson(a, b, self.entry_n.get(), self.entry_h.get(),
                                                self.entry_func1.get(), self.simpson.get(), excel,
                                                self.check.get())
                if ans is not None:
                    messagebox.showinfo("Composite Simpson", ans)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 14:
            if excel == '':
                excel = 'Midpoint'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                ans = Composite_Midpoint.midpoint(a, b, self.entry_n.get(), self.entry_h.get(),
                                                  self.entry_func1.get(), excel,
                                                  self.check.get())
                if ans is not None:
                    messagebox.showinfo("Composite Midpoint", ans)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 15:
            if excel == '':
                excel = 'Euler'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                xi = float(self.entry_xi.get())
                ans = Euler.euler(a, b, xi, self.entry_n.get(), self.entry_h.get(),
                                  self.entry_func1.get(), self.entry_func2.get(),
                                  excel,
                                  self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Euler", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 16:
            if excel == '':
                excel = 'Modified Euler'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                xi = float(self.entry_xi.get())
                ans = M_euler.euler(a, b, xi, self.entry_n.get(), self.entry_h.get(),
                                    self.entry_func1.get(), self.entry_func2.get(),
                                    excel,
                                    self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Modified Euler", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 17:
            if excel == '':
                excel = 'Diff Midpoint'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                xi = float(self.entry_xi.get())
                ans = Differential_MidPoint.midpoint(a, b, xi, self.entry_n.get(), self.entry_h.get(),
                                                     self.entry_func1.get(), self.entry_func2.get(),
                                                     excel,
                                                     self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Diff Midpoint", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 18:
            if excel == '':
                excel = 'Heun'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                xi = float(self.entry_xi.get())
                ans = Heun.heun(a, b, xi, self.entry_n.get(), self.entry_h.get(),
                                self.entry_func1.get(), self.entry_func2.get(),
                                excel,
                                self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Heun", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 19:
            if excel == '':
                excel = 'Rk4'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                xi = float(self.entry_xi.get())
                ans = Rk_4.rk_4(a, b, xi, self.entry_n.get(), self.entry_h.get(),
                                self.entry_func1.get(), self.entry_func2.get(),
                                excel,
                                self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Rk 4", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 20:
            if excel == '':
                excel = 'Jacobi'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                iterr = int(self.entry_iter.get())
                ans = Jacobi.jacobi(a, b, c, self.entry_d.get(), self.entry_e.get(), self.entry_f.get(),
                                    self.entry_func1.get(), self.entry_func2.get(), self.entry_func3.get(),
                                    self.entry_func4.get(), self.entry_func5.get(), self.entry_func6.get(),
                                    iterr, excel,
                                    self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Jacobi", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 21:
            if excel == '':
                excel = 'Gauss'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                iterr = int(self.entry_iter.get())
                ans = Gauss_Siedel.gauss(a, b, c, self.entry_d.get(), self.entry_e.get(), self.entry_f.get(),
                                         self.entry_func1.get(), self.entry_func2.get(), self.entry_func3.get(),
                                         self.entry_func4.get(), self.entry_func5.get(), self.entry_func6.get(),
                                         iterr, excel,
                                         self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Gauss", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 22:
            if excel == '':
                excel = 'Dolittle'
            try:
                LU.lu(self.entry_func1.get(), self.entry_func2.get(), self.entry_func3.get(),
                      self.entry_func4.get(), self.entry_func5.get(), self.entry_func6.get(),
                      self.matrix, excel,
                      self.check.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 23:
            if excel == '':
                excel = 'LDL'
            try:
                LDL.ldl(self.entry_func1.get(), self.entry_func2.get(), self.entry_func3.get(),
                        self.entry_func4.get(), self.entry_func5.get(), self.entry_func6.get(),
                        self.matrix, excel,
                        self.check.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 24:
            if excel == '':
                excel = 'Cholesky'
            try:
                Cholesky.cholesky(self.entry_func1.get(), self.entry_func2.get(), self.entry_func3.get(),
                                        self.entry_func4.get(), self.entry_func5.get(), self.entry_func6.get(),
                                        self.matrix, excel,
                                        self.check.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 25:
            if excel == '':
                excel = 'Crout'
            try:
                Crout.crout(self.entry_func1.get(), self.entry_func2.get(), self.entry_func3.get(),
                                  self.entry_func4.get(), self.entry_func5.get(), self.entry_func6.get(),
                                  self.matrix, excel,
                                  self.check.get())
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 26:
            if excel == '':
                excel = 'Fwd_bckwd'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                fa = float(self.entry_f1.get())
                fb = float(self.entry_f2.get())
                fc = float(self.entry_f3.get())
                ans = Fwd_Bck_Differential.f_b_d(a, b, c, fa, fb, fc, excel, self.check.get())
                if ans is not None:
                    messagebox.showinfo("Ex4.1", ans)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 27:
            if excel == '':
                excel = 'Rk2'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                xi = float(self.entry_xi.get())
                ans = Rk_2.rk_2(a, b, xi, self.entry_n.get(), self.entry_h.get(),
                                self.entry_func1.get(), self.entry_func2.get(),
                                excel,
                                self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Rk 2", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 28:
            if excel == '':
                excel = 'Rk3'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                xi = float(self.entry_xi.get())
                ans = Rk_3.rk_3(a, b, xi, self.entry_n.get(), self.entry_h.get(),
                                self.entry_func1.get(), self.entry_func2.get(),
                                excel,
                                self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Rk 3", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 29:
            if excel == '':
                excel = 'Rk4_De'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                xi = float(self.entry_xi.get())
                ans = Rk_4_DE.rk_4(a, b, c, xi, self.entry_n.get(), self.entry_h.get(),
                                   self.entry_func1.get(), self.entry_func2.get(),
                                   excel,
                                   self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Rk 4 for DE", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 30:
            if excel == '':
                excel = 'Second_Deriv'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                d = float(self.entry_d.get())
                fa = float(self.entry_f1.get())
                fb = float(self.entry_f2.get())
                fc = float(self.entry_f3.get())
                fd = float(self.entry_f4.get())
                ans = Second_Deriv.sec_deriv(a, b, c, d, self.entry_e.get(), self.entry_f.get(), fa, fb, fc, fd,
                                             self.entry_f5.get(), self.entry_f6.get(), excel,
                                             self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Second Derivative", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")
        elif self.choice.get() == 31:
            if excel == '':
                excel = 'Lagrange_v2'
            try:
                ans = None
                a = float(self.entry_a.get())
                b = float(self.entry_b.get())
                c = float(self.entry_c.get())
                xi = float(self.entry_xi.get())
                ans = lagrange_v2.lagrange(a, b, c, xi, self.entry_func1.get(), self.entry_f1, self.entry_f2.get(),
                                               self.entry_f3.get(),
                                               excel,
                                               self.check.get())
                if ans is not None:
                    for answer in ans:
                        messagebox.showinfo("Lagrange V2", answer)
            except ValueError:
                messagebox.showerror("Error", "Invalid Value in Numerical Field")


def on_closing():
    root.kill_threads = True
    time.sleep(0.2)
    root.destroy()


if __name__ == '__main__':
    root = nc_meta()
    root.title('Nucleotic\'s NC')
    root.state('zoomed')
    root.geometry('1250x750')
    style = ThemedStyle(root)
    root.protocol('WM_DELETE_WINDOW', on_closing)
    style.set_theme('breeze')
    root.mainloop()
