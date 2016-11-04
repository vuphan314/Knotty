
lexing_sequence = [('key_check', 'check'), ('kn_id', 'ch'), ('key_pri', 'print'), ('key_truth', 'true'), ('key_if', 'if'), ('kn_num', 'im'), ('op_exp', '^'), ('kn_num', '2'), ('op_eq', '='), ('op_minus', '-'), ('kn_num', '1'), ('key_else', 'else'), ('key_truth', 'false')]

syntax_tree = \
  ('knStats',
    ('checkStat',
      ('kn_id', 'ch'),
      ('condTerm',
        ('key_truth', 'true'),
        ('opEq',
          ('opExp',
            ('kn_num', 'im'),
            ('kn_num', '2')
          ),
          ('uMinus',
            ('kn_num', '1')
          )
        ),
        ('key_truth', 'false')
      )
    )
  )

import kn_lib

check_list = []




check_list.append(('ch', kn_lib.sp_tex((kn_lib.true if kn_lib.opEq(kn_lib.opExp(kn_lib.im, 2), kn_lib.uMinus(1)) else kn_lib.false))))


kn_lib.write_tex_file(check_list, r'examples/oneliner.tex', 'w')
