
parse_tree = \
  ('knStats',
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'fact'),
        ('formParams',
          ('kn_id', 'n')
        )
      ),
      ('defBody',
        ('retCl',
          ('condTerm',
            ('kn_num', '1'),
            ('opEq',
              ('kn_id', 'n'),
              ('kn_num', '0')
            ),
            ('opMult',
              ('kn_id', 'n'),
              ('actFunTerm',
                ('kn_id', 'fact'),
                ('actParams',
                  ('bMinus',
                    ('kn_id', 'n'),
                    ('kn_num', '1')
                  )
                )
              )
            )
          )
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'ch3'),
      ('actFunTerm',
        ('kn_id', 'fact'),
        ('actParams',
          ('kn_num', '3')
        )
      )
    )
  )

import kn_lib

check_list = []



def fact(n):
    return 1 if kn_lib.opEq(n, 0) else kn_lib.opMult(n, fact(kn_lib.bMinus(n, 1)))


check_list.append(('ch3', kn_lib.sp_tex(fact(3))))


kn_lib.write_tex(check_list, r'examples/tmp.tex')
