import kn_lib

check_list = []



def S(n, x):
    return (1 if kn_lib.opEq(n, 0) else (x if kn_lib.opEq(n, 1) else kn_lib.bMinus(kn_lib.opMult(x, S(kn_lib.bMinus(n, 1), x)), S(kn_lib.bMinus(n, 2), x))))

x = kn_lib.make_vars('x')


check_list.append(('S2', kn_lib.sp_tex(S(2, x))))


check_list.append(('S3', kn_lib.sp_tex(S(3, x))))


check_list.append(('S4', kn_lib.sp_tex(S(4, x))))


check_list.append(('S5', kn_lib.sp_tex(S(5, x))))


kn_lib.write_tex_file(check_list, r'../examples/poly_S.tex', 'w')

syntax_tree = \
  ('kn_root',
    ('funStat',
      ('formFunTerm',
        ('kn_id', 'S'),
        ('formParams',
          ('kn_id', 'n'),
          ('kn_id', 'x')
        )
      ),
      ('funBody',
        ('retCl',
          ('condTerm',
            ('kn_num', '1'),
            ('opEq',
              ('kn_id', 'n'),
              ('kn_num', '0')
            ),
            ('condTerm',
              ('kn_id', 'x'),
              ('opEq',
                ('kn_id', 'n'),
                ('kn_num', '1')
              ),
              ('bMinus',
                ('opMult',
                  ('kn_id', 'x'),
                  ('actFunTerm',
                    ('kn_id', 'S'),
                    ('actParams',
                      ('bMinus',
                        ('kn_id', 'n'),
                        ('kn_num', '1')
                      ),
                      ('kn_id', 'x')
                    )
                  )
                ),
                ('actFunTerm',
                  ('kn_id', 'S'),
                  ('actParams',
                    ('bMinus',
                      ('kn_id', 'n'),
                      ('kn_num', '2')
                    ),
                    ('kn_id', 'x')
                  )
                )
              )
            )
          )
        )
      )
    ),
    ('unknownStat',
      ('knVars',
        ('kn_id', 'x')
      )
    ),
    ('checkStat',
      ('kn_id', 'S2'),
      ('actFunTerm',
        ('kn_id', 'S'),
        ('actParams',
          ('kn_num', '2'),
          ('kn_id', 'x')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'S3'),
      ('actFunTerm',
        ('kn_id', 'S'),
        ('actParams',
          ('kn_num', '3'),
          ('kn_id', 'x')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'S4'),
      ('actFunTerm',
        ('kn_id', 'S'),
        ('actParams',
          ('kn_num', '4'),
          ('kn_id', 'x')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'S5'),
      ('actFunTerm',
        ('kn_id', 'S'),
        ('actParams',
          ('kn_num', '5'),
          ('kn_id', 'x')
        )
      )
    )
  )

lexing_sequence = [('key_fun', 'function'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '1'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '0'), ('key_else', 'else'), ('kn_id', 'x'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '1'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_unknown', 'unknown'), ('kn_id', 'x'), ('key_check', 'check'), ('kn_id', 'S2'), ('colon_eq', ':='), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'S3'), ('colon_eq', ':='), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '3'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'S4'), ('colon_eq', ':='), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '4'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'S5'), ('colon_eq', ':='), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '5'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')')]
