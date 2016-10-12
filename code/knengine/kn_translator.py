import sympy

import kn_parser
import kn_lib

############################################################
# top

def kn_translate(T):
    st = sympy_import + '\n\n'
    st += kn_lib_import + '\n\n'
    st2 = translate_recur(T)
    return st + st2

def translate_recur(T: tuple) -> str:
    if kn_parser.is_termimal(T):
        return translate_terminal(T)
    else:
        st = T[0]
        if st in str_helper_dict:
            return str_helper_dict[st](T)
        else:
            for se in set_helper_dict:
                if st in se:
                    return set_helper_dict[se](T)
            return recur_str(translate_recur, T)

############################################################
# termimal translation

def translate_terminal(T: tuple) -> str:
    st = T[1]
    if is_in_kn_lib(st):
        st = call_kn_lib(st)
    return st

############################################################
# collection translation

def translate_collection(T: tuple) -> str:
    st = translate_recur(T[1])
    for t in T[2:]:
        st2 = ', ' + translate_recur(t)
        st += st2
    return st

############################################################
# Knotty-variable translation

def translate_varStat(T):
    vars = translate_recur(T[1])
    st = call_sympy('var') + "('" + vars + "')" '\n\n'
    return st

############################################################
# Knotty-function translation

def translate_defStat(T):
    fun, trm = [translate_recur(T[i]) for i in range(1, 3)]
    st = 'def ' + fun + ':\n' + trm
    return st

def translate_funTerm(T):
    st = translate_recur(T[1])
    st2 = '('
    if not is_nullary(T):
        st2 += translate_recur(T[2])
    st2 += ')'
    return st + st2

def is_nullary(T: tuple) -> bool:
    return len(T) == 2

tab = ' ' * 4

def translate_letCl(T):
    tmp, trm = [translate_recur(T[i]) for i in range(1, 3)]
    st = tab + tmp + ' = ' + trm + '\n'
    return st

def translate_retCl(T):
    trm = translate_recur(T[1])
    st = tab + 'return ' + trm + '\n\n'
    return st

############################################################
# helper dictionaries

str_helper_dict = {
    'varStat': translate_varStat,
    'defStat': translate_defStat,
    'letCl': translate_letCl,
    'retCl': translate_retCl}

fs = frozenset

set_helper_dict = {
    fs({'actFunTerm', 'formFunTerm'}):
        translate_funTerm,
    fs({'knVars', 'knTerms', 'actParams', 'formParams'}):
        translate_collection}

############################################################
# recursion helper

def recur_str(py_fun, T: tuple) -> str:
    st = ''
    for t in T[1:]:
        st += py_fun(t)
    return st

############################################################
# Knotty-library helper

kn_lib_names = dir(kn_lib)
kn_lib_names = {
    name for name in kn_lib_names if name[0] != '_'}

def is_in_kn_lib(name: str) -> bool:
    return name in kn_lib_names

kn_lib_alias = 'kl'
sympy_alias = 'sp'

kn_lib_import = (
    'import ' + kn_lib.__name__ + ' as ' + kn_lib_alias)    
sympy_import = (
    'import ' + sympy.__name__ + ' as ' + sympy_alias)

def call_kn_lib(name: str) -> str:
    return kn_lib_alias + '.' + name
def call_sympy(name: str) -> str:
    return sympy_alias + '.' + name
