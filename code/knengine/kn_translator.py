import sympy

from debugger import *
import kn_parser
import kn_lib

############################################################
# top

def kn_translate(T) -> str:
    st = kn_lib_import + '\n\n'
    st += init_check_dict() + '\n\n'
    st += translate_recur(T)
    st += write_check_dict()
    return st

def translate_recur(T: tuple) -> str:
    if isinstance(T, str):
        return T
    elif kn_parser.is_termimal(T):
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
    return T[1]

############################################################
# Knotty-variable translation

def translate_varStat(T):
    vars = translate_recur(T[1])
    st = (
        vars + ' = ' + apply_recur(
            call_kn_lib('make_var'),
            [vars],
            sep_pair = "''"
            ) + '\n\n'
        )
    return st

############################################################
# collection translation

def translate_collection(T: tuple) -> str:
    st = translate_recur(T[1])
    for t in T[2:]:
        st += ', ' + translate_recur(t)
    return st

############################################################
# Knotty-function translation

def translate_defStat(T):
    fun, trm = [translate_recur(T[i]) for i in range(1, 3)]
    st = 'def ' + fun + ':\n' + trm
    return st

def translate_funTerm(T):
    return apply_recur(T[1], list(T[2:]))

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
# Knotty-check translation

def translate_checkStat(T):
    key, value = [translate_recur(t) for t in T[1:]]
    value = apply_recur(call_kn_lib('get_tex'), [value])
    st = '''
Knotty_checks[{key}] = {value}

'''.format(key = key, value = value)
    return st

def init_check_dict() -> str:
    st = '''
Knotty_checks = {}

'''
    return st

# write_tex = 'write_tex'

def write_check_dict() -> str:
    st = '''
check_string = ''

for check_name in Knotty_checks:
    check_string += (
        check_name + ' = ' '$$ ' +
        Knotty_checks[check_name] + ' $$')

def write_tex(tex_name: str) -> None:
    with open(tex_name) as tex_file:
        tex_file.write(check_string)

write_tex()
print('asddsaasd')
'''
    return st

############################################################
# recursion helper

def apply_recur(
        fun_name, param_seq = [], sep_pair = ''
        ) -> str:
    st = ''
    if isinstance(param_seq, tuple):
        st += translate_recur(param_seq)
    elif param_seq: # non-empty list
        st += translate_recur(param_seq[0])
        for param in param_seq[1:]:
            st += ', ' + translate_recur(param)

    if sep_pair:
        st = sep_pair[0] + st + sep_pair[1]
    st = '(' + st + ')'
    st = translate_recur(fun_name)+ st
    return st

def recur_str(py_fun, T: tuple) -> str:
    st = ''
    for t in T[1:]:
        st += py_fun(t)
    return st

############################################################
# Knotty-library helper

def translate_kn_lib(T):
    return apply_recur(call_kn_lib(T[0]), list(T[1:]))

kn_lib_attributes = dir(kn_lib)
kn_lib_attributes = {
        name for name in kn_lib_attributes
        if not name.startswith('_')
    }

kn_lib_name = kn_lib.__name__

kn_lib_import = 'import ' + kn_lib_name

def call_kn_lib(name: str) -> str:
    return kn_lib_name + '.' + name

############################################################
# helper dictionaries

str_helper_dict = {
    'varStat': translate_varStat,
    'defStat': translate_defStat,
    'letCl': translate_letCl,
    'retCl': translate_retCl,
    'checkStat': translate_checkStat}

fs = frozenset

set_helper_dict = {
    fs({'actFunTerm', 'formFunTerm'}):
        translate_funTerm,
    fs({'knVars', 'knTerms', 'actParams', 'formParams'}):
        translate_collection,
    fs(kn_lib_attributes):
        translate_kn_lib}
