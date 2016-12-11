import kn_lib

check_list = []



t, x = kn_lib.make_vars('t, x')

def T(n, x):
    return (2 if kn_lib.opEq(n, 0) else (x if kn_lib.opEq(n, 1) else kn_lib.bMinus(kn_lib.opMult(x, T(kn_lib.bMinus(n, 1), x)), T(kn_lib.bMinus(n, 2), x))))


check_list.append(('T2x', kn_lib.sp_tex(T(2, x))))

def skein(p, q):
    n = kn_lib.gcd(p, q)
    p2 = kn_lib.opDiv(p, n)
    q2 = kn_lib.opDiv(q, n)
    curve = kn_lib.SCC(p2, q2)
    return T(n, curve)


check_list.append(('skein22', kn_lib.sp_tex(skein(2, 2))))

def productToSum(p, q, r, s):
    determinant = kn_lib.bMinus(kn_lib.opMult(p, s), kn_lib.opMult(q, r))
    sk1 = skein(kn_lib.opPlus(p, r), kn_lib.opPlus(q, s))
    sk2 = skein(kn_lib.bMinus(p, r), kn_lib.bMinus(q, s))
    return kn_lib.opPlus(kn_lib.opMult(kn_lib.opExp(t, determinant), sk1), kn_lib.opMult(kn_lib.opExp(t, kn_lib.uMinus(determinant)), sk2))

def product2211():
    return kn_lib.opMult(skein(2, 2), skein(1, 1))

def sum2211():
    return productToSum(2, 2, 1, 1)


check_list.append(('lhs', kn_lib.sp_tex(product2211())))


check_list.append(('rhs', kn_lib.sp_tex(sum2211())))


check_list.append(('lhsEqualRhs', kn_lib.sp_tex(kn_lib.opEq(product2211(), sum2211()))))

def allTrue(booleanFunction, currentIndex, baseIndex):
    return (kn_lib.opLess(currentIndex, baseIndex) or (booleanFunction(currentIndex) and allTrue(booleanFunction, kn_lib.bMinus(currentIndex, 1), baseIndex)))

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


kn_lib.write_tex_file(check_list, r'../examples/paperTorus.tex', 'w')

syntax_tree = \
  ('kn_root',
    ('unknownStat',
      ('knUnknowns',
        ('kn_id', 't'),
        ('kn_id', 'x')
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'T'),
        ('formParams',
          ('kn_id', 'n'),
          ('kn_id', 'x')
        )
      ),
      ('funBody',
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
                  ('actFunExpr',
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
                ('actFunExpr',
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
    ('checkStat',
      ('kn_id', 'T2x'),
      ('actFunExpr',
        ('kn_id', 'T'),
        ('actParams',
          ('kn_num', '2'),
          ('kn_id', 'x')
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'skein'),
        ('formParams',
          ('kn_id', 'p'),
          ('kn_id', 'q')
        )
      ),
      ('funBody',
        ('letCls',
          ('letCl',
            ('kn_id', 'n'),
            ('actFunExpr',
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
            ('actFunExpr',
              ('kn_id', 'SCC'),
              ('actParams',
                ('kn_id', 'p2'),
                ('kn_id', 'q2')
              )
            )
          )
        ),
        ('retCl',
          ('actFunExpr',
            ('kn_id', 'T'),
            ('actParams',
              ('kn_id', 'n'),
              ('kn_id', 'curve')
            )
          )
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'skein22'),
      ('actFunExpr',
        ('kn_id', 'skein'),
        ('actParams',
          ('kn_num', '2'),
          ('kn_num', '2')
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'productToSum'),
        ('formParams',
          ('kn_id', 'p'),
          ('kn_id', 'q'),
          ('kn_id', 'r'),
          ('kn_id', 's')
        )
      ),
      ('funBody',
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
            ('actFunExpr',
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
            ('actFunExpr',
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
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'product2211')
      ),
      ('funBody',
        ('retCl',
          ('opMult',
            ('actFunExpr',
              ('kn_id', 'skein'),
              ('actParams',
                ('kn_num', '2'),
                ('kn_num', '2')
              )
            ),
            ('actFunExpr',
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
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'sum2211')
      ),
      ('funBody',
        ('retCl',
          ('actFunExpr',
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
      ('actFunExpr',
        ('kn_id', 'product2211')
      )
    ),
    ('checkStat',
      ('kn_id', 'rhs'),
      ('actFunExpr',
        ('kn_id', 'sum2211')
      )
    ),
    ('checkStat',
      ('kn_id', 'lhsEqualRhs'),
      ('opEq',
        ('actFunExpr',
          ('kn_id', 'product2211')
        ),
        ('actFunExpr',
          ('kn_id', 'sum2211')
        )
      )
    ),
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

lexing_sequence = [('key_unknown', 'unknown'), ('kn_id', 't'), ('kn_comma', ','), ('kn_id', 'x'), ('key_fun', 'function'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '2'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '0'), ('key_else', 'else'), ('kn_id', 'x'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '1'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'T2x'), ('colon_eq', ':='), ('kn_id', 'T'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'n'), ('colon_eq', ':='), ('kn_id', 'gcd'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'p2'), ('colon_eq', ':='), ('kn_id', 'p'), ('op_div', '/'), ('kn_id', 'n'), ('key_let', 'let'), ('kn_id', 'q2'), ('colon_eq', ':='), ('kn_id', 'q'), ('op_div', '/'), ('kn_id', 'n'), ('key_let', 'let'), ('kn_id', 'curve'), ('colon_eq', ':='), ('kn_id', 'SCC'), ('l_paren', '('), ('kn_id', 'p2'), ('kn_comma', ','), ('kn_id', 'q2'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('kn_comma', ','), ('kn_id', 'curve'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'skein22'), ('colon_eq', ':='), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'productToSum'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('kn_comma', ','), ('kn_id', 'r'), ('kn_comma', ','), ('kn_id', 's'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'determinant'), ('colon_eq', ':='), ('kn_id', 'p'), ('op_mult', '*'), ('kn_id', 's'), ('op_minus', '-'), ('kn_id', 'q'), ('op_mult', '*'), ('kn_id', 'r'), ('key_let', 'let'), ('kn_id', 'sk1'), ('colon_eq', ':='), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('op_plus', '+'), ('kn_id', 'r'), ('kn_comma', ','), ('kn_id', 'q'), ('op_plus', '+'), ('kn_id', 's'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'sk2'), ('colon_eq', ':='), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('op_minus', '-'), ('kn_id', 'r'), ('kn_comma', ','), ('kn_id', 'q'), ('op_minus', '-'), ('kn_id', 's'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 't'), ('op_exp', '^'), ('kn_id', 'determinant'), ('op_mult', '*'), ('kn_id', 'sk1'), ('op_plus', '+'), ('kn_id', 't'), ('op_exp', '^'), ('op_minus', '-'), ('kn_id', 'determinant'), ('op_mult', '*'), ('kn_id', 'sk2'), ('key_fun', 'function'), ('kn_id', 'product2211'), ('l_paren', '('), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('r_paren', ')'), ('op_mult', '*'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '1'), ('kn_comma', ','), ('kn_num', '1'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'sum2211'), ('l_paren', '('), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'productToSum'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '1'), ('kn_comma', ','), ('kn_num', '1'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'lhs'), ('colon_eq', ':='), ('kn_id', 'product2211'), ('l_paren', '('), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'rhs'), ('colon_eq', ':='), ('kn_id', 'sum2211'), ('l_paren', '('), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'lhsEqualRhs'), ('colon_eq', ':='), ('kn_id', 'product2211'), ('l_paren', '('), ('r_paren', ')'), ('op_eq', '='), ('kn_id', 'sum2211'), ('l_paren', '('), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'booleanFunction'), ('kn_comma', ','), ('kn_id', 'currentIndex'), ('kn_comma', ','), ('kn_id', 'baseIndex'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'currentIndex'), ('op_less', '<'), ('kn_id', 'baseIndex'), ('op_or', 'or'), ('kn_id', 'booleanFunction'), ('l_paren', '('), ('kn_id', 'currentIndex'), ('r_paren', ')'), ('op_and', 'and'), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'booleanFunction'), ('kn_comma', ','), ('kn_id', 'currentIndex'), ('op_minus', '-'), ('kn_num', '1'), ('kn_comma', ','), ('kn_id', 'baseIndex'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '1'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '0'), ('key_else', 'else'), ('kn_id', 'x'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '1'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '2'), ('r_paren', ')'), ('key_if', 'if'), ('kn_id', 'n'), ('op_gr', '>'), ('kn_num', '0'), ('key_else', 'else'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_plus', '+'), ('kn_num', '1'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_plus', '+'), ('kn_num', '2'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'equalityS'), ('l_paren', '('), ('kn_id', 'n'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'S'), ('l_paren', '('), ('op_minus', '-'), ('kn_id', 'n'), ('r_paren', ')'), ('op_eq', '='), ('op_minus', '-'), ('kn_id', 'S'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '2'), ('r_paren', ')'), ('key_const', 'constant'), ('kn_id', 'nMax'), ('colon_eq', ':='), ('kn_num', '5'), ('key_const', 'constant'), ('kn_id', 'nMin'), ('colon_eq', ':='), ('op_minus', '-'), ('kn_id', 'nMax'), ('key_check', 'check'), ('kn_id', 'verifiedEqualityS'), ('colon_eq', ':='), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'equalityS'), ('kn_comma', ','), ('kn_id', 'nMax'), ('kn_comma', ','), ('kn_id', 'nMin'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'sumS'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'k'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '0'), ('key_if', 'if'), ('kn_id', 'k'), ('op_less', '<'), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'p'), ('op_minus', '-'), ('kn_num', '4'), ('op_mult', '*'), ('kn_id', 'k'), ('op_minus', '-'), ('kn_num', '2'), ('r_paren', ')'), ('op_plus', '+'), ('kn_id', 'sumS'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'k'), ('op_minus', '-'), ('kn_num', '1'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'sumEqualRatio'), ('l_paren', '('), ('kn_id', 'p'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'sumS'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'p'), ('op_minus', '-'), ('kn_num', '1'), ('r_paren', ')'), ('op_eq', '='), ('op_minus', '-'), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '2'), ('op_mult', '*'), ('kn_id', 'p'), ('op_minus', '-'), ('kn_num', '3'), ('r_paren', ')'), ('op_div', '/'), ('kn_id', 'S'), ('l_paren', '('), ('kn_num', '1'), ('r_paren', ')'), ('key_const', 'constant'), ('kn_id', 'pMax'), ('colon_eq', ':='), ('kn_num', '5'), ('key_const', 'constant'), ('kn_id', 'pMin'), ('colon_eq', ':='), ('kn_num', '1'), ('key_check', 'check'), ('kn_id', 'verifiedSumEqualRatio'), ('colon_eq', ':='), ('kn_id', 'allTrue'), ('l_paren', '('), ('kn_id', 'sumEqualRatio'), ('kn_comma', ','), ('kn_id', 'pMax'), ('kn_comma', ','), ('kn_id', 'pMin'), ('r_paren', ')')]
