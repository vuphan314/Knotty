
parse_tree = \
    ('knStats',
        ('varStat',
            ('knVars',
                ('kn_id', 'x'),
                ('kn_id', 'y')
            )
        ),
        ('checkStat',
            ('kn_id', 't'),
            ('opMult',
                ('kn_id', 'x'),
                ('kn_id', 'x')
            )
        )
    )

import kn_lib


Knotty_checks = {}



x, y = kn_lib.make_vars('x, y')


Knotty_checks[t] = kn_lib.get_tex(kn_lib.opMult(x, x))


check_string = ''

for check_name in Knotty_checks:
    check_string += (
            check_name + ' = ' '$$ ' +
            Knotty_checks[check_name] + ' $$'
        )

def write_tex(tex_name: str) -> None:
    with open(tex_name) as tex_file:
        tex_file.write(check_string)

write_tex()
