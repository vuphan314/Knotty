import os
import sys

from vu_toolkit.vu_debugger import *
from genparser.src.astgen.parsing import ast, lexer, parser

############################################################

def parse_file(kn_path: str) -> dict:
    syntax_dict = get_syntax_dict(kn_path)

    syntax_dict['lexing_sequence'] = trim_lexing_sequence(
        syntax_dict['lexing_sequence']
    )

    syntax_AST = syntax_dict.pop('syntax_AST')
    syntax_tree = get_syntax_tree(syntax_AST)
    syntax_dict['syntax_tree'] = syntax_tree

    syntax_str = get_syntax_str(syntax_tree)
    syntax_dict['syntax_str'] = syntax_str

    return syntax_dict

############################################################
# invoke Evgenii's generic parser

def get_syntax_dict(kn_path: str) -> dict:
    """Return lexing_sequence and syntax_AST."""
    lexicon_file = 'kn_lexicon.txt'
    grammar_file = 'kn_grammar.txt'

    lexicon_file = get_complete_path(lexicon_file)
    grammar_file = get_complete_path(grammar_file)

    lexer_instance = lexer.Lexer(lexicon_file)
    allowed_terminals = lexer_instance.lexicon_dict.keys()
    parser_instance = parser.Parser(
        grammar_file, allowed_terminals
    )

    lexing_sequence = (
        lexer_instance.get_lexing_sequence_from_file(
            kn_path
        )
    )
    syntax_AST = parser_instance.get_ast(lexing_sequence)

    syntax_dict = {
        'lexing_sequence': lexing_sequence,
        'syntax_AST': syntax_AST
    }
    return syntax_dict

def get_complete_path(incomplete_path: str) -> str:
    """Add current directory to file name."""
    current_dir = os.path.dirname(os.path.abspath(__file__))
    complete_path = os.path.join(
        current_dir, incomplete_path
    )
    return complete_path

############################################################

def trim_lexing_sequence(lexing_sequence: list) -> list:
    lis = [
        tup for tup in lexing_sequence if tup[0] != 'spaces'
    ]
    return lis

############################################################
# AST to tuple

def get_syntax_tree(syntax_AST: ast.AST) -> tuple:
    if syntax_AST is None:
        syntax_list = ['None']
    else:
        syntax_list = list(syntax_AST)
    syntax_tree = convert_syntax_list_to_tree(syntax_list)
    return syntax_tree

def convert_syntax_list_to_tree(T: list) -> tuple:
    if is_leaf(T):
        return T
    else:
        T2 = T[0],
        for t in T[1:]:
            T2 += convert_syntax_list_to_tree(t),
        return T2

############################################################
# tuple to str

def get_syntax_str(syntax_tree: tuple) -> str:
    syntax_str = convert_syntax_tree_to_str(syntax_tree)
    return syntax_str

def convert_syntax_tree_to_str(
    T: tuple, tab_count=1
) -> str:
    tree_tab = ' ' * 2
    tabs = tree_tab * tab_count
    st = tabs
    if is_leaf(T):
        st += str(T)
    else:
        st += "('" + T[0] + "'"
        for t in T[1:]:
            st2 = ',\n'
            st2 += convert_syntax_tree_to_str(
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
