import sys
import os

from debugger import *
from genparser.src.astgen.parsing import lexer, parser

def get_output_str(input_path: str) -> str:
    output_tree = get_output_tree(input_path)
    if output_tree is None:
        output_str = str(None)
    else:
        output_str = convert_tuple_to_str(output_tree) + '\n'
    return output_str

def convert_tuple_to_str(T: tuple, tab_count = 0) -> str:
    tabs = my_tab * tab_count
    st = tabs
    if is_termimal(T):
        st += str(T)
    else:
        st += "('" + T[0] + "'"
        for t in T[1:]:
            st2 = ',\n'
            st2 += convert_tuple_to_str(t, tab_count = tab_count + 1)
            st += st2
        st += '\n' + tabs + ')'
    return st

my_tab = '  '

def is_termimal(T: tuple) -> bool:
    return isinstance(T[1], str)

def get_output_tree(input_path: str) -> tuple:
    """Return parse-tree as None/tuple."""
    lexed_parsed = kn_parse(input_path)
    parsed = lexed_parsed['parsed']
    return parsed

def kn_parse(input_path: str) -> dict:
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
    if parsed is not None:
        parsed = list(parsed)
        parsed = convert_list_to_tuple(parsed)

    lexed_parsed = {'lexed': lexed, 'parsed': parsed}
    return lexed_parsed

def get_complete_path(incomplete_path: str) -> str:
    """Add current directory to file name.

    Idea of Evgenii Balai.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    complete_path = os.path.join(current_dir, incomplete_path)
    return complete_path

def convert_list_to_tuple(T: list) -> tuple:
    if isinstance(T, tuple):
        return T
    else: # list
        T2 = T[0],
        for t in T[1:]:
            T2 += convert_list_to_tuple(t),
        return T2

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_str = get_output_str(input_path)
    print(output_str)
