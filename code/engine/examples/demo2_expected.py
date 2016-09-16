import sympy

def eq(a, b):
    diff = sympy.simplify(a - b)
    return diff == 0

def T(n, x):
    ret_n_0 = 2
    ret_n_1 = x
    return \
        ret_n_0 if eq(n, 0) else \
        ret_n_1 if eq(n, 1) else \
        x * T(n - 1, x) - T(n - 2, x)

x = sympy.Symbol('x')

def test1():
    return T(2, x)

def test2():
    return T(2, sympy.I * x)

if __name__ == '__main__':
    tests = test1, test2
    st = ''
    for test in tests:
        st += 'def ' test.__name__ + ' ret ' + test()
