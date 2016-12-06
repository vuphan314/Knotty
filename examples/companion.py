import kn_lib

check_list = []



x, y = kn_lib.make_vars('x, y')

c = (2 if kn_lib.true else (0 if kn_lib.false else kn_lib.opExp(x, 2)))

def f():
    return 0

def g(x):
    fun = f
    y = kn_lib.opEq(1, 1)
    return (y or fun())


check_list.append(('ccc', kn_lib.sp_tex(kn_lib.opPlus(c, 1))))


check_list.append(('imaginaryUnitSquared', kn_lib.sp_tex((kn_lib.opExp(kn_lib.i, 2) if (kn_lib.true or kn_lib.opNot(kn_lib.false)) else 1))))

def c1():
    return 1


check_list.append(('cc', kn_lib.sp_tex(c1())))

def f1(x):
    return kn_lib.opExp(x, kn_lib.uMinus(2))

def compose(fa, fb, x):
    return fa(fb(x))


check_list.append(('cccc1a2', kn_lib.sp_tex(compose(f1, f1, kn_lib.i))))

x = kn_lib.make_vars('x')


check_list.append(('f1x', kn_lib.sp_tex(f1(x))))

def f3(x, y):
    z1 = kn_lib.opDiv(1, x)
    z2 = (kn_lib.opDiv(x, y) if kn_lib.opEq(f1(kn_lib.opMod(x, y)), kn_lib.opDiv(5, 2)) else (1 if kn_lib.opEq(c1(), 3) else z1))
    return (kn_lib.opMod(z1, z2) if kn_lib.opEq(z1, 4) else (3 if kn_lib.false else kn_lib.opExp(kn_lib.i, 3)))

y, z = kn_lib.make_vars('y, z')


check_list.append(('t1', kn_lib.sp_tex((kn_lib.opPlus(kn_lib.opMod(y, z), f3(kn_lib.opMod(y, z), kn_lib.opPlus(kn_lib.uMinus(x), 2))) if kn_lib.true else 0))))

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


check_list.append(('skein22', kn_lib.sp_tex(skein(2, 2))))

def product2211():
    return kn_lib.opMult(skein(2, 2), skein(1, 1))

def sum2211():
    return productToSum(2, 2, 1, 1)


check_list.append(('lhs', kn_lib.sp_tex(product2211())))


check_list.append(('rhs', kn_lib.sp_tex(sum2211())))


check_list.append(('lhsEqualRhs', kn_lib.sp_tex(kn_lib.opEq(product2211(), sum2211()))))


kn_lib.write_tex_file(check_list, r'../examples/companion.tex', 'w')

syntax_tree = \
  ('kn_root',
    ('unknownStat',
      ('knUnknowns',
        ('kn_id', 'x'),
        ('kn_id', 'y')
      )
    ),
    ('constStat',
      ('kn_id', 'c'),
      ('condTerm',
        ('kn_num', '2'),
        ('key_truth', 'true'),
        ('condTerm',
          ('kn_num', '0'),
          ('key_truth', 'false'),
          ('opExp',
            ('kn_id', 'x'),
            ('kn_num', '2')
          )
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'f')
      ),
      ('funBody',
        ('retCl',
          ('kn_num', '0')
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'g'),
        ('formParams',
          ('kn_id', 'x')
        )
      ),
      ('funBody',
        ('letCls',
          ('letCl',
            ('kn_id', 'fun'),
            ('kn_id', 'f')
          ),
          ('letCl',
            ('kn_id', 'y'),
            ('opEq',
              ('kn_num', '1'),
              ('kn_num', '1')
            )
          )
        ),
        ('retCl',
          ('opOr',
            ('kn_id', 'y'),
            ('actFunExpr',
              ('kn_id', 'fun')
            )
          )
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'ccc'),
      ('opPlus',
        ('kn_id', 'c'),
        ('kn_num', '1')
      )
    ),
    ('checkStat',
      ('kn_id', 'imaginaryUnitSquared'),
      ('condTerm',
        ('opExp',
          ('kn_num', 'i'),
          ('kn_num', '2')
        ),
        ('opOr',
          ('key_truth', 'true'),
          ('opNot',
            ('key_truth', 'false')
          )
        ),
        ('kn_num', '1')
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'c1')
      ),
      ('funBody',
        ('retCl',
          ('kn_num', '1')
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'cc'),
      ('actFunExpr',
        ('kn_id', 'c1')
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'f1'),
        ('formParams',
          ('kn_id', 'x')
        )
      ),
      ('funBody',
        ('retCl',
          ('opExp',
            ('kn_id', 'x'),
            ('uMinus',
              ('kn_num', '2')
            )
          )
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'compose'),
        ('formParams',
          ('kn_id', 'fa'),
          ('kn_id', 'fb'),
          ('kn_id', 'x')
        )
      ),
      ('funBody',
        ('retCl',
          ('actFunExpr',
            ('kn_id', 'fa'),
            ('actParams',
              ('actFunExpr',
                ('kn_id', 'fb'),
                ('actParams',
                  ('kn_id', 'x')
                )
              )
            )
          )
        )
      )
    ),
    ('checkStat',
      ('kn_id', 'cccc1a2'),
      ('actFunExpr',
        ('kn_id', 'compose'),
        ('actParams',
          ('kn_id', 'f1'),
          ('kn_id', 'f1'),
          ('kn_num', 'i')
        )
      )
    ),
    ('unknownStat',
      ('knUnknowns',
        ('kn_id', 'x')
      )
    ),
    ('checkStat',
      ('kn_id', 'f1x'),
      ('actFunExpr',
        ('kn_id', 'f1'),
        ('actParams',
          ('kn_id', 'x')
        )
      )
    ),
    ('funStat',
      ('formFunExpr',
        ('kn_id', 'f3'),
        ('formParams',
          ('kn_id', 'x'),
          ('kn_id', 'y')
        )
      ),
      ('funBody',
        ('letCls',
          ('letCl',
            ('kn_id', 'z1'),
            ('opDiv',
              ('kn_num', '1'),
              ('kn_id', 'x')
            )
          ),
          ('letCl',
            ('kn_id', 'z2'),
            ('condTerm',
              ('opDiv',
                ('kn_id', 'x'),
                ('kn_id', 'y')
              ),
              ('opEq',
                ('actFunExpr',
                  ('kn_id', 'f1'),
                  ('actParams',
                    ('opMod',
                      ('kn_id', 'x'),
                      ('kn_id', 'y')
                    )
                  )
                ),
                ('opDiv',
                  ('kn_num', '5'),
                  ('kn_num', '2')
                )
              ),
              ('condTerm',
                ('kn_num', '1'),
                ('opEq',
                  ('actFunExpr',
                    ('kn_id', 'c1')
                  ),
                  ('kn_num', '3')
                ),
                ('kn_id', 'z1')
              )
            )
          )
        ),
        ('retCl',
          ('condTerm',
            ('opMod',
              ('kn_id', 'z1'),
              ('kn_id', 'z2')
            ),
            ('opEq',
              ('kn_id', 'z1'),
              ('kn_num', '4')
            ),
            ('condTerm',
              ('kn_num', '3'),
              ('key_truth', 'false'),
              ('opExp',
                ('kn_num', 'i'),
                ('kn_num', '3')
              )
            )
          )
        )
      )
    ),
    ('unknownStat',
      ('knUnknowns',
        ('kn_id', 'y'),
        ('kn_id', 'z')
      )
    ),
    ('checkStat',
      ('kn_id', 't1'),
      ('condTerm',
        ('opPlus',
          ('opMod',
            ('kn_id', 'y'),
            ('kn_id', 'z')
          ),
          ('actFunExpr',
            ('kn_id', 'f3'),
            ('actParams',
              ('opMod',
                ('kn_id', 'y'),
                ('kn_id', 'z')
              ),
              ('opPlus',
                ('uMinus',
                  ('kn_id', 'x')
                ),
                ('kn_num', '2')
              )
            )
          )
        ),
        ('key_truth', 'true'),
        ('kn_num', '0')
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
    ('unknownStat',
      ('knUnknowns',
        ('kn_id', 't')
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
    ('unknownStat',
      ('knUnknowns',
        ('kn_id', 'x')
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
    )
  )

lexing_sequence = [('key_unknown', 'unknown'), ('kn_id', 'x'), ('kn_comma', ','), ('kn_id', 'y'), ('key_const', 'constant'), ('kn_id', 'c'), ('colon_eq', ':='), ('kn_num', '2'), ('key_if', 'if'), ('key_truth', 'true'), ('key_else', 'else'), ('kn_num', '0'), ('key_if', 'if'), ('key_truth', 'false'), ('key_else', 'else'), ('kn_id', 'x'), ('op_exp', '^'), ('kn_num', '2'), ('key_fun', 'function'), ('kn_id', 'f'), ('l_paren', '('), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '0'), ('key_fun', 'function'), ('kn_id', 'g'), ('l_paren', '('), ('kn_id', 'x'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'fun'), ('colon_eq', ':='), ('kn_id', 'f'), ('key_let', 'let'), ('kn_id', 'y'), ('colon_eq', ':='), ('kn_num', '1'), ('op_eq', '='), ('kn_num', '1'), ('key_ret', 'return'), ('kn_id', 'y'), ('op_or', 'or'), ('kn_id', 'fun'), ('l_paren', '('), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'ccc'), ('colon_eq', ':='), ('kn_id', 'c'), ('op_plus', '+'), ('kn_num', '1'), ('key_check', 'check'), ('kn_id', 'imaginaryUnitSquared'), ('colon_eq', ':='), ('kn_num', 'i'), ('op_exp', '^'), ('kn_num', '2'), ('key_if', 'if'), ('key_truth', 'true'), ('op_or', 'or'), ('op_not', 'not'), ('key_truth', 'false'), ('key_else', 'else'), ('kn_num', '1'), ('key_fun', 'function'), ('kn_id', 'c1'), ('l_paren', '('), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '1'), ('key_check', 'check'), ('kn_id', 'cc'), ('colon_eq', ':='), ('kn_id', 'c1'), ('l_paren', '('), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'f1'), ('l_paren', '('), ('kn_id', 'x'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'x'), ('op_exp', '^'), ('op_minus', '-'), ('kn_num', '2'), ('key_fun', 'function'), ('kn_id', 'compose'), ('l_paren', '('), ('kn_id', 'fa'), ('kn_comma', ','), ('kn_id', 'fb'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'fa'), ('l_paren', '('), ('kn_id', 'fb'), ('l_paren', '('), ('kn_id', 'x'), ('r_paren', ')'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'cccc1a2'), ('colon_eq', ':='), ('kn_id', 'compose'), ('l_paren', '('), ('kn_id', 'f1'), ('kn_comma', ','), ('kn_id', 'f1'), ('kn_comma', ','), ('kn_num', 'i'), ('r_paren', ')'), ('key_unknown', 'unknown'), ('kn_id', 'x'), ('key_check', 'check'), ('kn_id', 'f1x'), ('colon_eq', ':='), ('kn_id', 'f1'), ('l_paren', '('), ('kn_id', 'x'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'f3'), ('l_paren', '('), ('kn_id', 'x'), ('kn_comma', ','), ('kn_id', 'y'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'z1'), ('colon_eq', ':='), ('kn_num', '1'), ('op_div', '/'), ('kn_id', 'x'), ('key_let', 'let'), ('kn_id', 'z2'), ('colon_eq', ':='), ('kn_id', 'x'), ('op_div', '/'), ('kn_id', 'y'), ('key_if', 'if'), ('kn_id', 'f1'), ('l_paren', '('), ('kn_id', 'x'), ('op_mod', '%'), ('kn_id', 'y'), ('r_paren', ')'), ('op_eq', '='), ('kn_num', '5'), ('op_div', '/'), ('kn_num', '2'), ('key_else', 'else'), ('kn_num', '1'), ('key_if', 'if'), ('kn_id', 'c1'), ('l_paren', '('), ('r_paren', ')'), ('op_eq', '='), ('kn_num', '3'), ('key_else', 'else'), ('kn_id', 'z1'), ('key_ret', 'return'), ('kn_id', 'z1'), ('op_mod', '%'), ('kn_id', 'z2'), ('key_if', 'if'), ('kn_id', 'z1'), ('op_eq', '='), ('kn_num', '4'), ('key_else', 'else'), ('kn_num', '3'), ('key_if', 'if'), ('key_truth', 'false'), ('key_else', 'else'), ('kn_num', 'i'), ('op_exp', '^'), ('kn_num', '3'), ('key_unknown', 'unknown'), ('kn_id', 'y'), ('kn_comma', ','), ('kn_id', 'z'), ('key_check', 'check'), ('kn_id', 't1'), ('colon_eq', ':='), ('kn_id', 'y'), ('op_mod', '%'), ('kn_id', 'z'), ('op_plus', '+'), ('kn_id', 'f3'), ('l_paren', '('), ('kn_id', 'y'), ('op_mod', '%'), ('kn_id', 'z'), ('kn_comma', ','), ('op_minus', '-'), ('kn_id', 'x'), ('op_plus', '+'), ('kn_num', '2'), ('r_paren', ')'), ('key_if', 'if'), ('key_truth', 'true'), ('key_else', 'else'), ('kn_num', '0'), ('key_fun', 'function'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_num', '2'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '0'), ('key_else', 'else'), ('kn_id', 'x'), ('key_if', 'if'), ('kn_id', 'n'), ('op_eq', '='), ('kn_num', '1'), ('key_else', 'else'), ('kn_id', 'x'), ('op_mult', '*'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '1'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('op_minus', '-'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('op_minus', '-'), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'n'), ('colon_eq', ':='), ('kn_id', 'gcd'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'p2'), ('colon_eq', ':='), ('kn_id', 'p'), ('op_div', '/'), ('kn_id', 'n'), ('key_let', 'let'), ('kn_id', 'q2'), ('colon_eq', ':='), ('kn_id', 'q'), ('op_div', '/'), ('kn_id', 'n'), ('key_let', 'let'), ('kn_id', 'curve'), ('colon_eq', ':='), ('kn_id', 'SCC'), ('l_paren', '('), ('kn_id', 'p2'), ('kn_comma', ','), ('kn_id', 'q2'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'T'), ('l_paren', '('), ('kn_id', 'n'), ('kn_comma', ','), ('kn_id', 'curve'), ('r_paren', ')'), ('key_unknown', 'unknown'), ('kn_id', 't'), ('key_fun', 'function'), ('kn_id', 'productToSum'), ('l_paren', '('), ('kn_id', 'p'), ('kn_comma', ','), ('kn_id', 'q'), ('kn_comma', ','), ('kn_id', 'r'), ('kn_comma', ','), ('kn_id', 's'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'determinant'), ('colon_eq', ':='), ('kn_id', 'p'), ('op_mult', '*'), ('kn_id', 's'), ('op_minus', '-'), ('kn_id', 'q'), ('op_mult', '*'), ('kn_id', 'r'), ('key_let', 'let'), ('kn_id', 'sk1'), ('colon_eq', ':='), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('op_plus', '+'), ('kn_id', 'r'), ('kn_comma', ','), ('kn_id', 'q'), ('op_plus', '+'), ('kn_id', 's'), ('r_paren', ')'), ('key_let', 'let'), ('kn_id', 'sk2'), ('colon_eq', ':='), ('kn_id', 'skein'), ('l_paren', '('), ('kn_id', 'p'), ('op_minus', '-'), ('kn_id', 'r'), ('kn_comma', ','), ('kn_id', 'q'), ('op_minus', '-'), ('kn_id', 's'), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 't'), ('op_exp', '^'), ('kn_id', 'determinant'), ('op_mult', '*'), ('kn_id', 'sk1'), ('op_plus', '+'), ('kn_id', 't'), ('op_exp', '^'), ('op_minus', '-'), ('kn_id', 'determinant'), ('op_mult', '*'), ('kn_id', 'sk2'), ('key_unknown', 'unknown'), ('kn_id', 'x'), ('key_check', 'check'), ('kn_id', 'T2x'), ('colon_eq', ':='), ('kn_id', 'T'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_id', 'x'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'skein22'), ('colon_eq', ':='), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'product2211'), ('l_paren', '('), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('r_paren', ')'), ('op_mult', '*'), ('kn_id', 'skein'), ('l_paren', '('), ('kn_num', '1'), ('kn_comma', ','), ('kn_num', '1'), ('r_paren', ')'), ('key_fun', 'function'), ('kn_id', 'sum2211'), ('l_paren', '('), ('r_paren', ')'), ('key_ret', 'return'), ('kn_id', 'productToSum'), ('l_paren', '('), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '2'), ('kn_comma', ','), ('kn_num', '1'), ('kn_comma', ','), ('kn_num', '1'), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'lhs'), ('colon_eq', ':='), ('kn_id', 'product2211'), ('l_paren', '('), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'rhs'), ('colon_eq', ':='), ('kn_id', 'sum2211'), ('l_paren', '('), ('r_paren', ')'), ('key_check', 'check'), ('kn_id', 'lhsEqualRhs'), ('colon_eq', ':='), ('kn_id', 'product2211'), ('l_paren', '('), ('r_paren', ')'), ('op_eq', '='), ('kn_id', 'sum2211'), ('l_paren', '('), ('r_paren', ')')]
