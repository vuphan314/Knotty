from kn_parser import is_termimal
from kntranslator import kn_lib

############################################################

bool_helper_tuple = (
    is_termimal,
    is_funTerm,
    is_collection)

str_helper_tuple = (
    translate_terminal,
    translate_funTerm,
    translate_collection)

helper_pairs = dict(zip(bool_helper_tuple, str_helper_tuple))

def translate_recur(T: tuple) -> str:
    for bool_helper in bool_helper_tuple:
        if bool_helper(T):
            str_helper = helper_pairs[bool_helper]
            return str_helper(T)
    return recur_str(translate_recur, T)

############################################################
# termimal translation

def translate_terminal(T: tuple) -> str:
    st = T[1]
    if is_in_lib(st):
        st = call_lib(st)
    return st

############################################################
# collection helper

def is_collection(T: tuple) -> bool:
    return T[0] in {
        'knVars', 'knTerms', 'actParams', 'formParams'}

def translate_collection(T: tuple) -> str:
    st = translate_recur(T[1])
    for t in T[2:]:
        st2 = ', ' + translate_recur(t)
        st += st2
    return st

############################################################
# Knotty-function helper

def is_funTerm(T: tuple) -> bool:
    return T[0] in {'actFunTerm', 'formFunTerm'}

def translate_funTerm(T):
    st = translate_recur(T[1])
    st2 = '('
    if not is_nullary(T):
        st2 += translate_recur(T[2])
    st2 += ')'
    return st + st2

def is_nullary(T: tuple) -> bool:
    return len(T) == 2

############################################################
# recursion helper

def recur_str(f: function, T: tuple) -> str:
    st = ''
    for t in T[1:]:
        st += f(t)
    return st

############################################################
# Knotty-library helper

lib_names = dir(kn_lib)
lib_names = {name for name in lib_names if name[0] != '_'}

def is_in_lib(name: str) -> bool:
    return name in lib_names

lib_alias = 'l'

def call_lib(name: str) -> str:
    return lib_alias + '.' + name
