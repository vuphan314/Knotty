'''Knotty library in Python.

Translate Knotty operations to SymPy operations.
'''

############################################################

import sympy as sp

############################################################

def get_tex(a) -> str:
    return sp.latex(a)

############################################################
# Knotty-variable

def make_var(st: str):
    sp.var(st)

############################################################
# imaginary unit

im = sp.I

############################################################
# conditional term

def condTerm(term1, bool_term, term2):
    return term1 if bool_term else term2

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
