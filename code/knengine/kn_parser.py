import os
import sys

from debugger import *
from genparser.src.astgen.parsing import ast, lexer, parser

############################################################
# top

def parse_file(kn_path: str) -> dict:
    parse_dict = get_parse_dict(kn_path)

    lex_list = parse_dict['lex_list']
    parse_dict['lex_list'] = trim_lex_list(lex_list)

    parse_AST = parse_dict.pop('parse_AST')

    parse_tuple = get_parse_tuple(parse_AST)
    parse_str = get_parse_str(parse_tuple)

    parse_dict['parse_tuple'] = parse_tuple
    parse_dict['parse_str'] = parse_str

    return parse_dict

############################################################
# invoke Evgenii's generic parser

def get_parse_dict(kn_path: str) -> dict:
    """Return lex_list and parse_AST."""
    lexicon_file = 'kn_lexicon.txt'
    grammar_file = 'kn_grammar.txt'

    lexicon_file = get_complete_path(lexicon_file)
    grammar_file = get_complete_path(grammar_file)

    lexer_instance = lexer.Lexer(lexicon_file)
    allowed_terminals = lexer_instance.lexicon_dict.keys()
    parser_instance = parser.Parser(
        grammar_file, allowed_terminals
    )

    lex_list = lexer_instance.get_lexing_sequence_from_file(
        kn_path
    )
    parse_AST = parser_instance.get_ast(lex_list)

    parse_dict = {
        'lex_list': lex_list, 'parse_AST': parse_AST
    }
    return parse_dict

def get_complete_path(incomplete_path: str) -> str:
    """Add current directory to file name."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    complete_path = os.path.join(
        current_dir, incomplete_path
    )
    return complete_path

############################################################

def trim_lex_list(lex_list: list) -> list:
    lis = [tup for tup in lex_list if tup[0] != 'spaces']
    return lis

############################################################
# AST to tuple

def get_parse_tuple(parse_AST: ast.AST) -> tuple:
    parse_list = list(parse_AST)
    parse_tuple = convert_list_to_tuple(parse_list)
    return parse_tuple

def convert_list_to_tuple(T: list) -> tuple:
    if is_leaf(T):
        return T
    else:
        T2 = T[0],
        for t in T[1:]:
            T2 += convert_list_to_tuple(t),
        return T2

############################################################
# tuple to str

def get_parse_str(parse_tuple: tuple) -> str:
    parse_str = convert_tuple_to_str(parse_tuple) + '\n'
    return parse_str

def convert_tuple_to_str(T: tuple, tab_count=1) -> str:
    tree_tab = ' ' * 2
    tabs = tree_tab * tab_count
    st = tabs
    if is_leaf(T):
        st += str(T)
    else:
        st += "('" + T[0] + "'"
        for t in T[1:]:
            st2 = ',\n'
            st2 += convert_tuple_to_str(
                t, tab_count=tab_count+1
            )
            st += st2
        st += '\n' + tabs + ')'
    return st

############################################################

def is_leaf(T: tuple) -> bool:
    boo = (
        isinstance(T, tuple) and
        len(T) == 2 and
        isinstance(T[1], str)
    )
    return boo
