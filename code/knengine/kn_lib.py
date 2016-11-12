'''Knotty library in Python.

Translate Knotty operations to SymPy operations.
'''

############################################################

import sympy as sp

############################################################

def write_tex_file(
    check_list: list, tex_path: str,
    write_mode: str
) -> None:
    tex_str = get_tex_str(check_list)
    with open(tex_path, write_mode) as tex_file:
        tex_file.write(tex_str)

def get_tex_str(check_list: list) -> str:
    tex_str = ''
    for check_pair in check_list:
        nam, ter = check_pair
        tex_str += r'''
\begin{{{env}}}
{nam} =
    {ter}
\end{{{env}}}

'''.format(env='dmath*', nam=nam, ter=ter)
    tex_str = add_tex_template(tex_str)
    return tex_str

def add_tex_template(tex_str: str) -> str:
    st1 = r'''
\documentclass[letterpaper, 10pt]{extarticle}

\usepackage[scale=0.9]{geometry}

\usepackage{amsmath}

\usepackage{breqn}

\begin{document}

'''
    st2 = r'''
\end{document}

'''
    return st1 + tex_str + st2

############################################################
# SymPy LaTeX

def sp_tex(a) -> str:
    return sp.latex(a)

############################################################

class SCC(sp.AtomicExpr):
    """Simple-Closed-Curve with slope p'/q' on torus."""
    pass

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

def gcd(a, b):
    return sp.gcd(a, b)

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
