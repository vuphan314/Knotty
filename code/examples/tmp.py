
parse_tree = \
  ('knStats',
    ('varStat',
      ('knVars',
        ('kn_id', 't'),
        ('kn_id', 'x'),
        ('kn_id', 'y')
      )
    ),
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'X'),
        ('formParams',
          ('kn_id', 'i')
        )
      ),
      ('defBody',
        ('retCl',
          ('condTerm',
            ('bMinus',
              ('uMinus',
                ('opExp',
                  ('kn_id', 't'),
                  ('kn_num', '2')
                )
              ),
              ('opExp',
                ('kn_id', 't'),
                ('uMinus',
                  ('kn_num', '2')
                )
              )
            ),
            ('opEq',
              ('kn_id', 'i'),
              ('kn_num', '0')
            ),
            ('condTerm',
              ('bMinus',
                ('opMult',
                  ('uMinus',
                    ('opExp',
                      ('kn_id', 't'),
                      ('kn_num', '2')
                    )
                  ),
                  ('opExp',
                    ('kn_id', 'x'),
                    ('kn_num', '2')
                  )
                ),
                ('opMult',
                  ('opExp',
                    ('kn_id', 't'),
                    ('kn_num', '4')
                  ),
                  ('kn_id', 'y')
                )
              ),
              ('opEq',
                ('kn_id', 'i'),
                ('kn_num', '1')
              ),
              ('bMinus',
                ('bMinus',
                  ('opMult',
                    ('opMult',
                      ('opExp',
                        ('kn_id', 't'),
                        ('kn_num', '2')
                      ),
                      ('kn_id', 'y')
                    ),
                    ('actFunTerm',
                      ('kn_id', 'X'),
                      ('actParams',
                        ('bMinus',
                          ('kn_id', 'i'),
                          ('kn_num', '1')
                        )
                      )
                    )
                  ),
                  ('opMult',
                    ('opExp',
                      ('kn_id', 't'),
                      ('kn_num', '4')
                    ),
                    ('actFunTerm',
                      ('kn_id', 'X'),
                      ('actParams',
                        ('bMinus',
                          ('kn_id', 'i'),
                          ('kn_num', '2')
                        )
                      )
                    )
                  )
                ),
                ('opMult',
                  ('opMult',
                    ('kn_num', '2'),
                    ('opExp',
                      ('kn_id', 't'),
                      ('kn_num', '2')
                    )
                  ),
                  ('opExp',
                    ('kn_id', 'x'),
                    ('kn_num', '2')
                  )
                )
              )
            )
          )
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X6'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '6')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X7'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '7')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X8'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '8')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X9'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '9')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X10'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '10')
        )
      )
    )
  )

import kn_lib

check_list = []



t, x, y = kn_lib.make_vars('t, x, y')

def X(i):
    return (kn_lib.bMinus(kn_lib.uMinus(kn_lib.opExp(t, 2)), kn_lib.opExp(t, kn_lib.uMinus(2))) if kn_lib.opEq(i, 0) else (kn_lib.bMinus(kn_lib.opMult(kn_lib.uMinus(kn_lib.opExp(t, 2)), kn_lib.opExp(x, 2)), kn_lib.opMult(kn_lib.opExp(t, 4), y)) if kn_lib.opEq(i, 1) else kn_lib.bMinus(kn_lib.bMinus(kn_lib.opMult(kn_lib.opMult(kn_lib.opExp(t, 2), y), X(kn_lib.bMinus(i, 1))), kn_lib.opMult(kn_lib.opExp(t, 4), X(kn_lib.bMinus(i, 2)))), kn_lib.opMult(kn_lib.opMult(2, kn_lib.opExp(t, 2)), kn_lib.opExp(x, 2)))))


check_list.append(('X6', kn_lib.sp_tex(X(6))))


check_list.append(('X7', kn_lib.sp_tex(X(7))))


check_list.append(('X8', kn_lib.sp_tex(X(8))))


check_list.append(('X9', kn_lib.sp_tex(X(9))))


check_list.append(('X10', kn_lib.sp_tex(X(10))))


kn_lib.write_tex(check_list, r'examples/tmp.tex')
