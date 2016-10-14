
import sympy

import kn_lib

Knotty_checks = {}



Knotty_checks['t'] = sympy.latex(1)

check_string = ''
for check_name in Knotty_checks:
    check_string += check_name + ' is $$ ' + Knotty_checks[check_name] + ' $$'
