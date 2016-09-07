from .. import lib

########## ########## ########## ########## ########## ##########
# constant tests

'''
copy and paste into the Python interpreter to test constants:

pp(c)

(pp: pretty-print)
'''

########## ########## ########## ########## ########## ##########
# variable declarations

x = Var()

########## ########## ########## ########## ########## ##########
# function definitions

# each function returns an instance of the class `Knot`

def c():
    return lib.Knot(0)

def T(n, x):
    lib.Knot(2) if n = 0 else
    lib.Knot(x) if n = 1 else
    lib.subtr(lib.mult(lib.Knot(x), T(n - 2, x)), T(n - 2, x))
