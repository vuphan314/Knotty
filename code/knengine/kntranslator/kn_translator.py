from kn_parser import is_termimal
from kntranslator import kn_lib

############################################################

def translate_recur(T: tuple) -> str:
    if is_termimal(T):
        return translate_terminal(T)
    elif is_funTerm(T):
        st = translate_recur(T[1])
        st2 = '('
        if not is_nullary(T):
            st2 += translate_recur(T[2])
        st2 += ')'
        return st + st2
    todo param number of tabs
    else:
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

def get_comma_separated_collection(T: tuple) -> str:
    st = translate_recur(T[1])
    for t in T[2:]:
        st2 = ', ' + translate_recur(t)
        st += st2
    return st

############################################################
# Knotty-function helper

def is_funTerm(T: tuple) -> bool:
    return T[0] in {'actFunTerm', 'formFunTerm'}

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
