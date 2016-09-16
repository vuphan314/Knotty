import sympy

def eq(a, b):
    diff = sympy.simplify(a - b)
    return diff == 0
