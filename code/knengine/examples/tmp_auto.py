
import sympy

import kn_lib

Knotty_checks = {}



kn_lib.make_var(x, y)

Knotty_checks['t'] = kn_lib.get_tex(kn_lib.opMult(x, x))


check_string = ''

for check_name in Knotty_checks:
    check_string += (
        check_name + ' = ' '$$ ' +
        Knotty_checks[check_name] + ' $$')


with open('bla.txt') as myfile:
    myfile.write(check_string)
