'''Knotty library in Python.

Translate Knotty operations to SymPy operations.
'''

############################################################

import sympy as sp

############################################################
# TeX output

def write_tex(tex_str: str, tex_path: str) -> None:
    tex_str = make_latex(tex_str)
    with open(tex_path, 'w') as tex_file:
        tex_file.write(tex_str)

def make_latex(tex_str: str) -> str:
    st1 = r'''
\documentclass{article}

\usepackage{amsmath}

\begin{document}

'''
    st2 = r'''
\end{document}

'''
    return st1 + tex_str + st2

############################################################
# SymPy LaTeX

def get_tex(a) -> str:
    return sp.latex(a)

############################################################
# Knotty-variable

def make_vars(st: str):
    return sp.symbols(st)

############################################################
# imaginary unit

im = sp.I

############################################################
# Knotty-bools

true = True
false = False

############################################################
# boolean operations

def opOr(a, b):
    return a or b

def opAnd(a, b):
    return a and b

def opNot(a):
    return not a

############################################################
# comparison boolean operations

def opEq(a, b):
    diff = sp.simplify(a - b)
    return diff == 0

def opUneq(a, b):
    return not opEq(a, b)

def opGr(a, b):
    return a > b

def opLess(a, b):
    return a < b

def grEq(a, b):
    return opOr(opGr(a, b), opEq(a, b))

def lessEq(a, b):
    return opOr(opLess(a, b), opEq(a, b))

############################################################
# arithmetic operations

def opPlus(a, b):
    return a + b

def bMinus(a, b):
    return opPlus(a, uMinus(b))

def opMult(a, b):
    return a * b

def opDiv(a, b):
    return a / b

def opMod(a, b):
    return a % b

def uMinus(a):
    return -a

def opExp(a, b):
    return a ** b
