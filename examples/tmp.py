import kn_lib

check_list = []



def allTrue(booleanFunction, currentIndex, baseIndex):
    return (kn_lib.opLess(currentIndex, baseIndex) or (booleanFunction(currentIndex) and allTrue(booleanFunction, kn_lib.bMinus(currentIndex, 1), baseIndex)))

def f(x):
    return kn_lib.opGr(x, 0)


check_list.append(('c', kn_lib.sp_tex(allTrue(f, 4, 1))))


kn_lib.write_tex_file(check_list, r'../examples/tmp.tex', 'w')

syntax_tree = \
  ('kn_root',
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'allTrue'),
        ('formParams',
          ('kn_id', 'booleanFunction'),
          ('kn_id', 'currentIndex'),
          ('kn_id', 'baseIndex')
        )
      ),
      ('funBody',
        ('retCl',
          ('opOr',
            ('opLess',
              ('kn_id', 'currentIndex'),
              ('kn_id', 'baseIndex')
            ),
            ('opAnd',
              ('actFunExpr',
                ('kn_id', 'booleanFunction'),
                ('actParams',
                  ('kn_id', 'currentIndex')
                )
              ),
              ('actFunExpr',
                ('kn_id', 'allTrue'),
                ('actParams',
                  ('kn_id', 'booleanFunction'),
                  ('bMinus',
                    ('kn_id', 'currentIndex'),
                    ('kn_num', '1')
                  ),
                  ('kn_id', 'baseIndex')
                )
              )
            )
          )
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'f'),
        ('formParams',
          ('kn_id', 'x')
        )
      ),
      ('funBody',
        ('retCl',
          ('opGr',
            ('kn_id', 'x'),
            ('kn_num', '0')
          )
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'c'),
      ('actFunExpr',
        ('kn_id', 'allTrue'),
        ('actParams',
          ('kn_id', 'f'),
          ('kn_num', '4'),
          ('kn_num', '1')
        )
      )
    )
  )

lexing_sequence = [('key_fun', 'function'), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'booleanFunction'), ('kn_comma', ','), ('kn_id', 'currentIndex'), ('kn_comma', ','), ('kn_id', 'baseIndex'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'currentIndex'), ('op_less', '<'), ('kn_id', 'baseIndex'), ('op_or', 'or'), ('kn_id', 'booleanFunction'), ('l_paren', '('), ('kn_id', 'currentIndex'), ('r_paren', ')'), ('op_and', 'and'), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'booleanFunction'), ('kn_comma', ','), ('kn_id', 'currentIndex'), ('op_minus', '-'), ('kn_num', '1'), ('kn_comma', ','), ('kn_id', 'baseIndex'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'f'), ('l_paren', '('), ('kn_id', 'x'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'x'), ('op_gr', '>'), ('kn_num', '0'), ('key_check', 'check'), ('kn_id', 'c'), ('colon_eq', ':='), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'f'), ('kn_comma', ','), ('kn_num', '4'), ('kn_comma', ','), ('kn_num', '1'), ('r_paren', ')')]
