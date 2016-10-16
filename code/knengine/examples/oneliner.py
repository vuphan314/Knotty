
parse_tree = \
    ('knStats',
        ('defStat',
            ('formFunTerm',
                ('kn_id', 'c')
            ),
            ('defBody',
                ('letCls',
                    ('letCl',
                        ('kn_id', 'tmp'),
                        ('kn_num', '1')
                    )
                ),
                ('retCl',
                    ('condTerm',
                        ('kn_id', 'tmp'),
                        ('key_truth', 'true'),
                        ('kn_num', '0')
                    )
                )
            )
        )
    )

import kn_lib

Knotty_checks = {}



def c():
    tmp = 1
    return kn_lib.condTerm(tmp, kn_lib.true, 0)


check_string = ''

for check_name in Knotty_checks:
    check_string += (
            check_name + ' = \n\t'
            '$$ ' + Knotty_checks[check_name] + ' $$'
            '\n\n'
        )

kn_lib.write_tex(check_string, r'examples\oneliner.tex')
