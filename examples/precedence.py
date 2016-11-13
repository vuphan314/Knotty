
parse_tree = \
  ('knStats',
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'correctSign'),
        ('formParams',
          ('kn_id', 'x')
        )
      ),
      ('defBody',
        ('retCl',
          ('condTerm',
            ('kn_num', '1'),
            ('opGr',
              ('kn_id', 'x'),
              ('kn_num', '0')
            ),
            ('condTerm',
              ('kn_num', '0'),
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
      )
    ),
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'incorrectSign'),
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
      ('kn_id', 'correctResult'),
      ('actFunTerm',
        ('kn_id', 'correctSign'),
        ('actParams',
          ('kn_num', '2')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'incorrectResult'),
      ('actFunTerm',
        ('kn_id', 'incorrectSign'),
        ('actParams',
          ('kn_num', '2')
        )
      )
    )
  )

import kn_lib

check_list = []



def correctSign(x):
    return (1 if kn_lib.opGr(x, 0) else (0 if kn_lib.opEq(x, 0) else kn_lib.uMinus(1)))

def incorrectSign(x):
    return ((1 if kn_lib.opGr(x, 0) else 0) if kn_lib.opEq(x, 0) else kn_lib.uMinus(1))


check_list.append(('correctResult', kn_lib.sp_tex(correctSign(2))))


check_list.append(('incorrectResult', kn_lib.sp_tex(incorrectSign(2))))


kn_lib.write_tex(check_list, r'examples/precedence.tex')
