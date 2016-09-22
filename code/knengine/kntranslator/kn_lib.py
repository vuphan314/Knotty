import sympy

im = sympy.I

def kn_eq(a, b):
    diff = sympy.simplify(a - b)
    return diff == 0
