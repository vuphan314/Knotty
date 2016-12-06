import kn_lib

check_list = []



def allTrue(booleanFunction, currentIndex, baseIndex):
    return (kn_lib.opLess(currentIndex, baseIndex) or (booleanFunction(currentIndex) and allTrue(booleanFunction, kn_lib.bMinus(currentIndex, 1), baseIndex)))

x = kn_lib.make_vars('x')

def S(n):
    return (1 if kn_lib.opEq(n, 0) else (x if kn_lib.opEq(n, 1) else (kn_lib.bMinus(kn_lib.opMult(x, S(kn_lib.bMinus(n, 1))), S(kn_lib.bMinus(n, 2))) if kn_lib.opGr(n, 0) else kn_lib.bMinus(kn_lib.opMult(x, S(kn_lib.opPlus(n, 1))), S(kn_lib.opPlus(n, 2))))))

def equalityS(n):
    return kn_lib.opEq(S(kn_lib.uMinus(n)), kn_lib.uMinus(S(kn_lib.bMinus(n, 2))))

nMax = 5

nMin = kn_lib.uMinus(nMax)


check_list.append(('verifiedEqualityS', kn_lib.sp_tex(allTrue(equalityS, nMax, nMin))))

def sumS(p, k):
    return (0 if kn_lib.opLess(k, 1) else kn_lib.opPlus(S(kn_lib.bMinus(kn_lib.bMinus(kn_lib.opMult(2, p), kn_lib.opMult(4, k)), 2)), sumS(p, kn_lib.bMinus(k, 1))))

def sumEqualRatio(p):
    return kn_lib.opEq(sumS(p, kn_lib.bMinus(p, 1)), kn_lib.opDiv(kn_lib.uMinus(S(kn_lib.bMinus(kn_lib.opMult(2, p), 3))), S(1)))

pMax = 5

pMin = 1


check_list.append(('verifiedSumEqualRatio', kn_lib.sp_tex(allTrue(sumEqualRatio, pMax, pMin))))


kn_lib.write_tex_file(check_list, r'../examples/poly_S.tex', 'w')

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
    ('unknownStat',
      ('knUnknowns',
        ('kn_id', 'x')
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'S'),
        ('formParams',
          ('kn_id', 'n')
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
              ('condTerm',
                ('bMinus',
                  ('opMult',
                    ('kn_id', 'x'),
                    ('actFunExpr',
                      ('kn_id', 'S'),
                      ('actParams',
                        ('bMinus',
                          ('kn_id', 'n'),
                          ('kn_num', '1')
                        )
                      )
                    )
                  ),
                  ('actFunExpr',
                    ('kn_id', 'S'),
                    ('actParams',
                      ('bMinus',
                        ('kn_id', 'n'),
                        ('kn_num', '2')
                      )
                    )
                  )
                ),
                ('opGr',
                  ('kn_id', 'n'),
                  ('kn_num', '0')
                ),
                ('bMinus',
                  ('opMult',
                    ('kn_id', 'x'),
                    ('actFunExpr',
                      ('kn_id', 'S'),
                      ('actParams',
                        ('opPlus',
                          ('kn_id', 'n'),
                          ('kn_num', '1')
                        )
                      )
                    )
                  ),
                  ('actFunExpr',
                    ('kn_id', 'S'),
                    ('actParams',
                      ('opPlus',
                        ('kn_id', 'n'),
                        ('kn_num', '2')
                      )
                    )
                  )
                )
              )
            )
          )
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'equalityS'),
        ('formParams',
          ('kn_id', 'n')
        )
      ),
      ('funBody',
        ('retCl',
          ('opEq',
            ('actFunExpr',
              ('kn_id', 'S'),
              ('actParams',
                ('uMinus',
                  ('kn_id', 'n')
                )
              )
            ),
            ('uMinus',
              ('actFunExpr',
                ('kn_id', 'S'),
                ('actParams',
                  ('bMinus',
                    ('kn_id', 'n'),
                    ('kn_num', '2')
                  )
                )
              )
            )
          )
        )
      )
    ),
    ('constStat',
      ('kn_id', 'nMax'),
      ('kn_num', '5')
    ),
    ('constStat',
      ('kn_id', 'nMin'),
      ('uMinus',
        ('kn_id', 'nMax')
      )
    ),
    ('checkStat',
      ('kn_id', 'verifiedEqualityS'),
      ('actFunExpr',
        ('kn_id', 'allTrue'),
        ('actParams',
          ('kn_id', 'equalityS'),
          ('kn_id', 'nMax'),
          ('kn_id', 'nMin')
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'sumS'),
        ('formParams',
          ('kn_id', 'p'),
          ('kn_id', 'k')
        )
      ),
      ('funBody',
        ('retCl',
          ('condTerm',
            ('kn_num', '0'),
            ('opLess',
              ('kn_id', 'k'),
              ('kn_num', '1')
            ),
            ('opPlus',
              ('actFunExpr',
                ('kn_id', 'S'),
                ('actParams',
                  ('bMinus',
                    ('bMinus',
                      ('opMult',
                        ('kn_num', '2'),
                        ('kn_id', 'p')
                      ),
                      ('opMult',
                        ('kn_num', '4'),
                        ('kn_id', 'k')
                      )
                    ),
                    ('kn_num', '2')
                  )
                )
              ),
              ('actFunExpr',
                ('kn_id', 'sumS'),
                ('actParams',
                  ('kn_id', 'p'),
                  ('bMinus',
                    ('kn_id', 'k'),
                    ('kn_num', '1')
                  )
                )
              )
            )
          )
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'sumEqualRatio'),
        ('formParams',
          ('kn_id', 'p')
        )
      ),
      ('funBody',
        ('retCl',
          ('opEq',
            ('actFunExpr',
              ('kn_id', 'sumS'),
              ('actParams',
                ('kn_id', 'p'),
                ('bMinus',
                  ('kn_id', 'p'),
                  ('kn_num', '1')
                )
              )
            ),
            ('opDiv',
              ('uMinus',
                ('actFunExpr',
                  ('kn_id', 'S'),
                  ('actParams',
                    ('bMinus',
                      ('opMult',
                        ('kn_num', '2'),
                        ('kn_id', 'p')
                      ),
                      ('kn_num', '3')
                    )
                  )
                )
              ),
              ('actFunExpr',
                ('kn_id', 'S'),
                ('actParams',
                  ('kn_num', '1')
                )
              )
            )
          )
        )
      )
    ),
    ('constStat',
      ('kn_id', 'pMax'),
      ('kn_num', '5')
    ),
    ('constStat',
      ('kn_id', 'pMin'),
      ('kn_num', '1')
    ),
    ('checkStat',
      ('kn_id', 'verifiedSumEqualRatio'),
      ('actFunExpr',
        ('kn_id', 'allTrue'),
        ('actParams',
          ('kn_id', 'sumEqualRatio'),
          ('kn_id', 'pMax'),
          ('kn_id', 'pMin')
        )
      )
    )
  )

lexing_sequence = [('key_fun', 'function'), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'booleanFunction'), ('kn_comma', ','), ('kn_id', 'currentIndex'), ('kn_comma', ','), ('kn_id', 'baseIndex'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'currentIndex'), ('op_less', '<'), ('kn_id', 'baseIndex'), ('op_or', 'or'), ('kn_id', 'booleanFunction'), ('l_paren', '('), ('kn_id', 'currentIndex'), ('r_paren', ')'), ('op_and', 'and'), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'booleanFunction'), ('kn_comma', ','), ('kn_id', 'currentIndex'), ('op_minus', '-'), ('kn_num', '1'), ('kn_comma', ','), ('kn_id', 'baseIndex'), ('r_paren', ')'), ('key_unknown', 'unknown'), ('kn_id', 'x'), ('key_fun', 'function'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '1'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '0'), ('key_else', 'else'), ('kn_id', 'x'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '1'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '2'), ('r_paren', ')'), ('key_if', 'if'), ('kn_id', 'n'), ('op_gr', '>'), ('kn_num', '0'), ('key_else', 'else'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_plus', '+'), ('kn_num', '1'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_plus', '+'), ('kn_num', '2'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'equalityS'), ('l_paren', '('), ('kn_id', 'n'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'S'), ('l_paren', '('), ('op_minus', '-'), ('kn_id', 'n'), ('r_paren', ')'), ('op_eq', '='), ('op_minus', '-'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '2'), ('r_paren', ')'), ('key_const', 'constant'), ('kn_id', 'nMax'), ('colon_eq', ':='), ('kn_num', '5'), ('key_const', 'constant'), ('kn_id', 'nMin'), ('colon_eq', ':='), ('op_minus', '-'), ('kn_id', 'nMax'), ('key_check', 'check'), ('kn_id', 'verifiedEqualityS'), ('colon_eq', ':='), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'equalityS'), ('kn_comma', ','), ('kn_id', 'nMax'), ('kn_comma', ','), ('kn_id', 'nMin'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'sumS'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'k'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '0'), ('key_if', 'if'), ('kn_id', 'k'), ('op_less', '<'), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'p'), ('op_minus', '-'), ('kn_num', '4'), ('op_mult', '*'), ('kn_id', 'k'), ('op_minus', '-'), ('kn_num', '2'), ('r_paren', ')'), ('op_plus', '+'), ('kn_id', 'sumS'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'k'), ('op_minus', '-'), ('kn_num', '1'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'sumEqualRatio'), ('l_paren', '('), ('kn_id', 'p'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'sumS'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'p'), ('op_minus', '-'), ('kn_num', '1'), ('r_paren', ')'), ('op_eq', '='), ('op_minus', '-'), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'p'), ('op_minus', '-'), ('kn_num', '3'), ('r_paren', ')'), ('op_div', '/'), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '1'), ('r_paren', ')'), ('key_const', 'constant'), ('kn_id', 'pMax'), ('colon_eq', ':='), ('kn_num', '5'), ('key_const', 'constant'), ('kn_id', 'pMin'), ('colon_eq', ':='), ('kn_num', '1'), ('key_check', 'check'), ('kn_id', 'verifiedSumEqualRatio'), ('colon_eq', ':='), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'sumEqualRatio'), ('kn_comma', ','), ('kn_id', 'pMax'), ('kn_comma', ','), ('kn_id', 'pMin'), ('r_paren', ')')]
