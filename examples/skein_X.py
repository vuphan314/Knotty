import kn_lib

check_list = []



t, x, y = kn_lib.make_vars('t, x, y')


check_list.append(('X0', kn_lib.sp_tex(X(0))))


check_list.append(('X1', kn_lib.sp_tex(X(1))))


check_list.append(('X2', kn_lib.sp_tex(X(2))))


check_list.append(('X3', kn_lib.sp_tex(X(3))))


check_list.append(('X4', kn_lib.sp_tex(X(4))))


check_list.append(('X5', kn_lib.sp_tex(X(5))))


kn_lib.write_tex_file(check_list, r'../examples/skein_X.tex', 'w')

syntax_tree = \
  ('kn_root',
    ('unknownStat',
      ('knVars',
        ('kn_id', 't'),
        ('kn_id', 'x'),
        ('kn_id', 'y')
      )
    ),
    ('checkStat',
      ('kn_id', 'X0'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '0')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X1'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '1')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X2'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '2')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X3'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '3')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X4'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '4')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'X5'),
      ('actFunTerm',
        ('kn_id', 'X'),
        ('actParams',
          ('kn_num', '5')
        )
      )
    )
  )

lexing_sequence = [('key_unknown', 'unknown'), ('kn_id', 't'), ('kn_comma', ','), ('kn_id', 'x'), ('kn_comma', ','), ('kn_id', 'y'), ('key_fun', 'function'), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', 'i'), ('r_paren', ')'), ('key_ret', 'return'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '2'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('op_minus', '-'), ('kn_num', '2'), ('key_if', 'if'), ('kn_num', 'i'), ('op_eq', '='), ('kn_num', '0'), ('key_else', 'else'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'x'), ('op_exp', '^'), ('kn_num', '2'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '4'), ('op_mult', '*'), ('kn_id', 'y'), ('key_if', 'if'), ('kn_num', 'i'), ('op_eq', '='), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'y'), ('op_mult', '*'), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', 'i'), ('op_minus', '-'), ('kn_num', '1'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '4'), ('op_mult', '*'), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', 'i'), ('op_minus', '-'), ('kn_num', '2'), ('r_paren', ')'), ('op_minus', '-'), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'x'), ('op_exp', '^'), ('kn_num', '2'), ('key_check', 'check'), ('kn_id', 'X0'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '0'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X1'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '1'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X2'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '2'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X3'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '3'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X4'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '4'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'X5'), ('colon_eq', ':='), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', '5'), ('r_paren', ')')]
