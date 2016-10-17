
parse_tree = \
  ('knStats',
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'sgn'),
        ('formParams',
          ('kn_id', 'x')
        )
      ),
      ('defBody',
        ('retCl',
          ('condTerm',
            ('condTerm',
              ('kn_num', '1'),
              ('opGr',
                ('kn_id', 'x'),
                ('kn_num', '0')
              ),
              ('kn_num', '0')
            ),
            ('opEq',
              ('kn_id', 'x'),
              ('kn_num', '0')
            ),
            ('uMinus',
              ('kn_num', '1')
            )
          )
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'ch'),
      ('actFunTerm',
        ('kn_id', 'sgn'),
        ('actParams',
          ('kn_num', '6')
        )
      )
    )
  )

import kn_lib

check_list = []



def sgn(x):
    return ((1 if kn_lib.opGr(x, 0) else 0) if kn_lib.opEq(x, 0) else kn_lib.uMinus(1))


check_list.append(('ch', kn_lib.sp_tex(sgn(6))))


kn_lib.write_tex(check_list, r'examples/tmp.tex')
