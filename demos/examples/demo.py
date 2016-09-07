from .. import lib

########## ########## ########## ########## ########## ##########
# tests

'''
copy and paste the block below into the Python interpreter to test:

c.pp()

(pp: pretty-print)
'''

########## ########## ########## ########## ########## ##########
# variable declarations

x = lib.Poly.Var()

########## ########## ########## ########## ########## ##########
# function definitions

'''
each function
- intakes `Var` parameters;
- returns an instance of the class `Poly`
'''

def c():
    return lib.Poly(0)

def T(n, x):
    return \
        lib.Poly(2) if lib.eq(lib.Poly(n), lib.Poly(0)) else
        lib.Poly(x) if lib.eq(lib.Poly(n), lib.Poly(1)) else
        lib.subtr(lib.mult(lib.Poly(x), T(n - 2, x)), T(n - 2, x))
