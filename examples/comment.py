import kn_lib

check_list = []



x, y = kn_lib.make_vars('x, y')


check_list.append(('ch', kn_lib.sp_tex(kn_lib.opEq(kn_lib.opExp(kn_lib.opPlus(x, y), 2), kn_lib.opPlus(kn_lib.opPlus(kn_lib.opExp(x, 2), kn_lib.opMult(kn_lib.opMult(2, x), y)), kn_lib.opExp(y, 2))))))


kn_lib.write_tex_file(check_list, r'../examples/comment.tex', 'w')
    
syntax_tree = \
  ('knStats',
    ('varStat',
      ('knVars',
        ('kn_id', 'x'),
        ('kn_id', 'y')
      )
    ),
    ('checkStat',
      ('kn_id', 'ch'),
      ('opEq',
        ('opExp',
          ('opPlus',
            ('kn_id', 'x'),
            ('kn_id', 'y')
          ),
          ('kn_num', '2')
        ),
        ('opPlus',
          ('opPlus',
            ('opExp',
              ('kn_id', 'x'),
              ('kn_num', '2')
            ),
            ('opMult',
              ('opMult',
                ('kn_num', '2'),
                ('kn_id', 'x')
              ),
              ('kn_id', 'y')
            )
          ),
          ('opExp',
            ('kn_id', 'y'),
            ('kn_num', '2')
          )
        )
      )
    )
  )

lexing_sequence = [('key_var', 'vary'), ('kn_id', 'x'), ('kn_comma', ','), ('kn_id', 'y'), ('key_check', 'check'), ('kn_id', 'ch'), ('key_pri', 'print'), ('l_paren', '('), ('kn_id', 'x'), ('op_plus', '+'), ('kn_id', 'y'), ('r_paren', ')'), ('op_exp', '^'), ('kn_num', '2'), ('op_eq', '='), ('kn_id', 'x'), ('op_exp', '^'), ('kn_num', '2'), ('op_plus', '+'), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'y'), ('op_plus', '+'), ('kn_id', 'y'), ('op_exp', '^'), ('kn_num', '2')]
