import sympy

############################################################
# imaginary unit

im = sympy.I

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
    diff = sympy.simplify(a - b)
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
