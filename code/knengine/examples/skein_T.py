
lexing_sequence = [('key_def', 'define'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '2'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '0'), ('key_else', 'else'), ('kn_id', 'x'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '1'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_def', 'define'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'n'), ('key_be', 'be'), ('kn_id', 'gcd'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'p2'), ('key_be', 'be'), ('kn_id', 'p'), ('op_div', '/'), ('kn_id', 'n'), ('key_let', 'let'), ('kn_id', 'q2'), ('key_be', 'be'), ('kn_id', 'q'), ('op_div', '/'), ('kn_id', 'n'), ('key_let', 'let'), ('kn_id', 'c'), ('key_be', 'be'), ('kn_id', 'SCC'), ('l_paren', '('), ('kn_id', 'p2'), ('kn_comma', ','), ('kn_id', 'q2'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('kn_comma', ','), ('kn_id', 'c'), ('r_paren', ')'), ('key_var', 'vary'), ('kn_id', 'x'), ('key_check', 'check'), ('kn_id', 'T2x'), ('key_pri', 'print'), ('kn_id', 'T'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'skeinP2Q2'), ('key_pri', 'print'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('r_paren', ')')]

syntax_tree = \
  ('knStats',
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'T'),
        ('formParams',
          ('kn_id', 'n'),
          ('kn_id', 'x')
        )
      ),
      ('defBody',
        ('retCl',
          ('condTerm',
            ('kn_num', '2'),
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
                    ('kn_id', 'T'),
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
                  ('kn_id', 'T'),
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
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'skein'),
        ('formParams',
          ('kn_id', 'p'),
          ('kn_id', 'q')
        )
      ),
      ('defBody',
        ('letCls',
          ('letCl',
            ('kn_id', 'n'),
            ('actFunTerm',
              ('kn_id', 'gcd'),
              ('actParams',
                ('kn_id', 'p'),
                ('kn_id', 'q')
              )
            )
          ),
          ('letCl',
            ('kn_id', 'p2'),
            ('opDiv',
              ('kn_id', 'p'),
              ('kn_id', 'n')
            )
          ),
          ('letCl',
            ('kn_id', 'q2'),
            ('opDiv',
              ('kn_id', 'q'),
              ('kn_id', 'n')
            )
          ),
          ('letCl',
            ('kn_id', 'c'),
            ('actFunTerm',
              ('kn_id', 'SCC'),
              ('actParams',
                ('kn_id', 'p2'),
                ('kn_id', 'q2')
              )
            )
          )
        ),
        ('retCl',
          ('actFunTerm',
            ('kn_id', 'T'),
            ('actParams',
              ('kn_id', 'n'),
              ('kn_id', 'c')
            )
          )
        )
      )
    ),
    ('varStat',
      ('knVars',
        ('kn_id', 'x')
      )
    ),
    ('checkStat',
      ('kn_id', 'T2x'),
      ('actFunTerm',
        ('kn_id', 'T'),
        ('actParams',
          ('kn_num', '2'),
          ('kn_id', 'x')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'skeinP2Q2'),
      ('actFunTerm',
        ('kn_id', 'skein'),
        ('actParams',
          ('kn_num', '2'),
          ('kn_num', '2')
        )
      )
    )
  )

import kn_lib

check_list = []



def T(n, x):
    return (2 if kn_lib.opEq(n, 0) else (x if kn_lib.opEq(n, 1) else kn_lib.bMinus(kn_lib.opMult(x, T(kn_lib.bMinus(n, 1), x)), T(kn_lib.bMinus(n, 2), x))))

def skein(p, q):
    n = kn_lib.gcd(p, q)
    p2 = kn_lib.opDiv(p, n)
    q2 = kn_lib.opDiv(q, n)
    c = kn_lib.SCC(p2, q2)
    return T(n, c)

x = kn_lib.make_vars('x')


check_list.append(('T2x', kn_lib.sp_tex(T(2, x))))


check_list.append(('skeinP2Q2', kn_lib.sp_tex(skein(2, 2))))


kn_lib.write_tex_file(check_list, r'examples/skein_T.tex', 'w')
