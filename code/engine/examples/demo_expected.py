from translator import lib

n = lib.Constant('n')

x = lib.Variable('x')

# T: Val * Val -> Val
def T(n, x):
    return \
        lib.Val(2) if lib.equal(n, lib.Val(0)) else \
        x if lib.equal(n, lib.Val(1)) else \
        lib.subtr(lib.mult(x, T(lib.subtr(n, lib.Val(1)))), T(lib.subtr(n, lib.Val(2))))

# test1: Val -> Val
def test1(x):
    n = lib.Constant(2)
    val = T(n, x)
    return val

# test2: void -> str
def test2():
    x = lib.mult(lib.imaginaryUnit, x)
    val = test1(x)
    return val
