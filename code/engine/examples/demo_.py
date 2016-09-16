import sympy

def T(n, x):
    ret_n_0 = 2
    ret_n_1 = x
    return \
        ret_n_0 if lib.eq(n, 0) else \
        ret_n_1 if lib.eq(n, 1) else \
        x * T(n - 1, x) - T(n - 2, x)

x = sympy.Symbol('x')

def test1():
    return T(2, x)

def test2():
    return T(2, lib.im * x)

def runTests():
    tests = test1, test2
    st = '\n'
    for test in tests:
        st2 = str(test())
        st += 'def ' + test.__name__ + ' ret ' + st2 + '\n\n'
    return st

if __name__ == '__main__':
    import sys
    sys.path.append('../translator/')
    import lib

    st = runTests()
    print(st)
    input('`Enter` to quit')
