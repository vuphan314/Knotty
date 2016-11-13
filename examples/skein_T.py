import kn_lib

check_list = []



def T(n, x):
    return (2 if kn_lib.opEq(n, 0) else (x if kn_lib.opEq(n, 1) else kn_lib.bMinus(kn_lib.opMult(x, T(kn_lib.bMinus(n, 1), x)), T(kn_lib.bMinus(n, 2), x))))

def skein(p, q):
    n = kn_lib.gcd(p, q)
    p2 = kn_lib.opDiv(p, n)
    q2 = kn_lib.opDiv(q, n)
    curve = kn_lib.SCC(p2, q2)
    return T(n, curve)

t = kn_lib.make_vars('t')

def productToSum(p, q, r, s):
    determinant = kn_lib.bMinus(kn_lib.opMult(p, s), kn_lib.opMult(q, r))
    sk1 = skein(kn_lib.opPlus(p, r), kn_lib.opPlus(q, s))
    sk2 = skein(kn_lib.bMinus(p, r), kn_lib.bMinus(q, s))
    return kn_lib.opPlus(kn_lib.opMult(kn_lib.opExp(t, determinant), sk1), kn_lib.opMult(kn_lib.opExp(t, kn_lib.uMinus(determinant)), sk2))

x = kn_lib.make_vars('x')


check_list.append(('T2x', kn_lib.sp_tex(T(2, x))))


check_list.append(('skeinP2Q2', kn_lib.sp_tex(skein(2, 2))))

def product2211():
    return kn_lib.opMult(skein(2, 2), skein(1, 1))

def sum2211():
    return productToSum(2, 2, 1, 1)


check_list.append(('lhs', kn_lib.sp_tex(product2211())))


check_list.append(('rhs', kn_lib.sp_tex(sum2211())))


check_list.append(('lhsEqualRhs', kn_lib.sp_tex(kn_lib.opEq(product2211(), sum2211()))))


kn_lib.write_tex_file(check_list, r'../examples/skein_T.tex', 'w')

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
            ('kn_id', 'curve'),
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
              ('kn_id', 'curve')
            )
          )
        )
      )
    ),
    ('varStat',
      ('knVars',
        ('kn_id', 't')
      )
    ),
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'productToSum'),
        ('formParams',
          ('kn_id', 'p'),
          ('kn_id', 'q'),
          ('kn_id', 'r'),
          ('kn_id', 's')
        )
      ),
      ('defBody',
        ('letCls',
          ('letCl',
            ('kn_id', 'determinant'),
            ('bMinus',
              ('opMult',
                ('kn_id', 'p'),
                ('kn_id', 's')
              ),
              ('opMult',
                ('kn_id', 'q'),
                ('kn_id', 'r')
              )
            )
          ),
          ('letCl',
            ('kn_id', 'sk1'),
            ('actFunTerm',
              ('kn_id', 'skein'),
              ('actParams',
                ('opPlus',
                  ('kn_id', 'p'),
                  ('kn_id', 'r')
                ),
                ('opPlus',
                  ('kn_id', 'q'),
                  ('kn_id', 's')
                )
              )
            )
          ),
          ('letCl',
            ('kn_id', 'sk2'),
            ('actFunTerm',
              ('kn_id', 'skein'),
              ('actParams',
                ('bMinus',
                  ('kn_id', 'p'),
                  ('kn_id', 'r')
                ),
                ('bMinus',
                  ('kn_id', 'q'),
                  ('kn_id', 's')
                )
              )
            )
          )
        ),
        ('retCl',
          ('opPlus',
            ('opMult',
              ('opExp',
                ('kn_id', 't'),
                ('kn_id', 'determinant')
              ),
              ('kn_id', 'sk1')
            ),
            ('opMult',
              ('opExp',
                ('kn_id', 't'),
                ('uMinus',
                  ('kn_id', 'determinant')
                )
              ),
              ('kn_id', 'sk2')
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
    ),
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'product2211')
      ),
      ('defBody',
        ('retCl',
          ('opMult',
            ('actFunTerm',
              ('kn_id', 'skein'),
              ('actParams',
                ('kn_num', '2'),
                ('kn_num', '2')
              )
            ),
            ('actFunTerm',
              ('kn_id', 'skein'),
              ('actParams',
                ('kn_num', '1'),
                ('kn_num', '1')
              )
            )
          )
        )
      )
    ),
    ('defStat',
      ('formFunTerm',
        ('kn_id', 'sum2211')
      ),
      ('defBody',
        ('retCl',
          ('actFunTerm',
            ('kn_id', 'productToSum'),
            ('actParams',
              ('kn_num', '2'),
              ('kn_num', '2'),
              ('kn_num', '1'),
              ('kn_num', '1')
            )
          )
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'lhs'),
      ('actFunTerm',
        ('kn_id', 'product2211')
      )
    ),
    ('checkStat',
      ('kn_id', 'rhs'),
      ('actFunTerm',
        ('kn_id', 'sum2211')
      )
    ),
    ('checkStat',
      ('kn_id', 'lhsEqualRhs'),
      ('opEq',
        ('actFunTerm',
          ('kn_id', 'product2211')
        ),
        ('actFunTerm',
          ('kn_id', 'sum2211')
        )
      )
    )
  )

lexing_sequence = [('key_def', 'define'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '2'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '0'), ('key_else', 'else'), ('kn_id', 'x'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '1'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_def', 'define'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'n'), ('key_be', 'be'), ('kn_id', 'gcd'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'p2'), ('key_be', 'be'), ('kn_id', 'p'), ('op_div', '/'), ('kn_id', 'n'), ('key_let', 'let'), ('kn_id', 'q2'), ('key_be', 'be'), ('kn_id', 'q'), ('op_div', '/'), ('kn_id', 'n'), ('key_let', 'let'), ('kn_id', 'curve'), ('key_be', 'be'), ('kn_id', 'SCC'), ('l_paren', '('), ('kn_id', 'p2'), ('kn_comma', ','), ('kn_id', 'q2'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('kn_comma', ','), ('kn_id', 'curve'), ('r_paren', ')'), ('key_var', 'vary'), ('kn_id', 't'), ('key_def', 'define'), ('kn_id', 'productToSum'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('kn_comma', ','), ('kn_id', 'r'), ('kn_comma', ','), ('kn_id', 's'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'determinant'), ('key_be', 'be'), ('kn_id', 'p'), ('op_mult', '*'), ('kn_id', 's'), ('op_minus', '-'), ('kn_id', 'q'), ('op_mult', '*'), ('kn_id', 'r'), ('key_let', 'let'), ('kn_id', 'sk1'), ('key_be', 'be'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('op_plus', '+'), ('kn_id', 'r'), ('kn_comma', ','), ('kn_id', 'q'), ('op_plus', '+'), ('kn_id', 's'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'sk2'), ('key_be', 'be'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('op_minus', '-'), ('kn_id', 'r'), ('kn_comma', ','), ('kn_id', 'q'), ('op_minus', '-'), ('kn_id', 's'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 't'), ('op_exp', '^'), ('kn_id', 'determinant'), ('op_mult', '*'), ('kn_id', 'sk1'), ('op_plus', '+'), ('kn_id', 't'), ('op_exp', '^'), ('op_minus', '-'), ('kn_id', 'determinant'), ('op_mult', '*'), ('kn_id', 'sk2'), ('key_var', 'vary'), ('kn_id', 'x'), ('key_check', 'check'), ('kn_id', 'T2x'), ('key_pri', 'print'), ('kn_id', 'T'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'skeinP2Q2'), ('key_pri', 'print'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('r_paren', ')'), ('key_def', 'define'), ('kn_id', 'product2211'), ('l_paren', '('), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('r_paren', ')'), ('op_mult', '*'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '1'), ('kn_comma', ','), ('kn_num', '1'), ('r_paren', ')'), ('key_def', 'define'), ('kn_id', 'sum2211'), ('l_paren', '('), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'productToSum'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '1'), ('kn_comma', ','), ('kn_num', '1'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'lhs'), ('key_pri', 'print'), ('kn_id', 'product2211'), ('l_paren', '('), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'rhs'), ('key_pri', 'print'), ('kn_id', 'sum2211'), ('l_paren', '('), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'lhsEqualRhs'), ('key_pri', 'print'), ('kn_id', 'product2211'), ('l_paren', '('), ('r_paren', ')'), ('op_eq', '='), ('kn_id', 'sum2211'), ('l_paren', '('), ('r_paren', ')')]
