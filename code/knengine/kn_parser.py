import sys
import os

from debugger import *
from genparser.src.astgen.parsing import lexer, parser

############################################################
# top

def kn_parse(input_path: str) -> dict:
    parse_tuple = get_parse_tuple(input_path)
    parse_str = get_parse_str(parse_tuple)
    parse_dict = {
            'parse_tuple': parse_tuple,
            'parse_str': parse_str
        }
    return parse_dict

############################################################
# call Evgenii's generic parser

def get_parse_tuple(input_path: str) -> tuple:
    """Return parse-tree as tuple."""
    lexed_parsed = get_parse_dict(input_path)
    parsed = lexed_parsed['parsed']
    return parsed

def get_parse_dict(input_path: str) -> dict:
    """Return lexing sequence and ast."""
    lexicon_file = 'kn_lexicon.txt'
    grammar_file = 'kn_grammar.txt'

    lexicon_file = get_complete_path(lexicon_file)
    grammar_file = get_complete_path(grammar_file)

    lexer_inst = lexer.Lexer(lexicon_file)
    allowed_terminals = lexer_inst.lexicon_dict.keys()
    parser_inst = parser.Parser(grammar_file, allowed_terminals)

    lexed = lexer_inst.get_lexing_sequence_from_file(input_path)

    parsed = parser_inst.get_ast(lexed)
    parsed = list(parsed)
    parsed = convert_list_to_tuple(parsed)

    lexed_parsed = {'lexed': lexed, 'parsed': parsed}
    return lexed_parsed

def convert_list_to_tuple(T: list) -> tuple:
    if isinstance(T, tuple):
        return T
    else: # list
        T2 = T[0],
        for t in T[1:]:
            T2 += convert_list_to_tuple(t),
        return T2

def get_complete_path(incomplete_path: str) -> str:
    """Add current directory to file name.

    Idea of Evgenii Balai.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    complete_path = os.path.join(current_dir, incomplete_path)
    return complete_path

############################################################
# pretty string of tree

def get_parse_str(parse_tuple: str) -> str:
    parse_str = convert_tuple_to_str(parse_tuple) + '\n'
    return parse_str

def convert_tuple_to_str(T: tuple, tab_count = 1) -> str:
    tabs = tree_tab * tab_count
    st = tabs
    if is_termimal(T):
        st += str(T)
    else:
        st += "('" + T[0] + "'"
        for t in T[1:]:
            st2 = ',\n'
            st2 += convert_tuple_to_str(
                    t, tab_count = tab_count + 1
                )
            st += st2
        st += '\n' + tabs + ')'
    return st

tree_tab = ' ' * 2

def is_termimal(T: tuple) -> bool:
    boo = (
        isinstance(T, tuple) and
        len(T) > 1 and
        isinstance(T[1], str)
        )
    return boo

############################################################

if __name__ == '__main__':
    input_path = sys.argv[1]
    parse_str = get_parse_str(input_path)
    print(parse_str)
