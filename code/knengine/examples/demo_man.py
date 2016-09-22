import sys
sys.path.insert(0, '../kntranslator/')

import sympy

import kn_lib

def T(n, x):
    return \
        2 if kn_lib.kn_eq(n, 0) else \
        x if kn_lib.kn_eq(n, 1) else \
        x * T(n - 1, x) - T(n - 2, x)

sympy.var('x')

def test1():
    return T(2, x)

def test2():
    return T(2, kn_lib.im * x)

def get_output_string():
    tests = test1, test2
    st = '\n'
    for test in tests:
        st2 = str(test())
        st += 'def ' + test.__name__ + ' return ' + st2 + '\n\n'
    return st

if __name__ == '__main__':
    st = get_output_string()
    print(st)
    input('(`Enter` to quit.)' '\n')
