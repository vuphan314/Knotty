from debugtools.debug_tool import *
import kn_lib
import kn_parsing

############################################################

def translate_tree(
    syntax_tree: tuple, tex_path: str, write_mode: str
) -> str:
    st = (
        kn_lib_import + '\n' +
        init_check_list() + '\n\n' +
        translate_recur(syntax_tree) +
        call_write_tex(tex_path, write_mode)
    )
    return st

def translate_recur(T: tuple) -> str:
    if isinstance(T, str):
        return T
    elif kn_parsing.is_leaf(T):
        return translate_leaf(T)
    elif T[0] == 'condTerm':
        a, boo, b = [translate_recur(t) for t in T[1:]]
        st = '(' + a + ' if ' + boo + ' else ' + b + ')'
        return st
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
# leaf translation

def translate_leaf(T: tuple) -> str:
    st = T[1]
    if st in kn_lib_attributes:
        st = call_kn_lib(st)
    return st

############################################################
# Knotty-variable translation

def translate_varStat(T):
    vars = translate_recur(T[1])
    st = (
        vars + ' = ' + apply_recur(
            call_kn_lib('make_vars'),
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
# Knotty-constant translation

def translate_constStat(T):
    const, ter = [translate_recur(t) for t in T[1:]]
    st = const + ' = ' + ter + '\n\n'
    return st

############################################################
# Knotty-function translation

def translate_funStat(T):
    fun, ter = [translate_recur(t) for t in T[1:]]
    st = 'def ' + fun + ':' '\n' + ter
    return st

def translate_funTerm(T):
    return apply_recur(T[1], list(T[2:]))

py_tab = ' ' * 4

def translate_letCl(T):
    tmp, ter = [translate_recur(t) for t in T[1:]]
    st = py_tab + tmp + ' = ' + ter + '\n'
    return st

def translate_retCl(T):
    ter = translate_recur(T[1])
    st = py_tab + 'return ' + ter + '\n\n'
    return st

############################################################
# Knotty-check translation

def translate_checkStat(T):
    nam, ter = [translate_recur(t) for t in T[1:]]
    ter = apply_recur(call_kn_lib('sp_tex'), [ter])
    st = '''
check_list.append(('{}', {}))

'''.format(nam, ter)
    return st

def init_check_list() -> str:
    st = '''
check_list = []

'''
    return st

def call_write_tex(tex_path: str, write_mode: str) -> str:
    st = '''
kn_lib.write_tex_file(check_list, r'{}', '{}')
'''.format(tex_path, write_mode)
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

def call_kn_lib(name: str) -> str:
    return kn_lib_name + '.' + name

kn_lib_import = 'import ' + kn_lib_name

############################################################
# helper dictionaries

str_helper_dict = {
    'unknownStat': translate_varStat,
    'constStat': translate_constStat,
    'funStat': translate_funStat,
    'letCl': translate_letCl,
    'retCl': translate_retCl,
    'checkStat': translate_checkStat
}

fs = frozenset

set_helper_dict = {
    fs({'actFunTerm', 'formFunTerm'}):
        translate_funTerm,
    fs({'knVars', 'knTerms', 'actParams', 'formParams'}):
        translate_collection,
    fs(kn_lib_attributes):
        translate_kn_lib
}
