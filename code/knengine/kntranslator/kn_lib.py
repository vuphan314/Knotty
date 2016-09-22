import sympy

im = sympy.I

def eq(a, b):
    diff = sympy.simplify(a - b)
    return diff == 0
