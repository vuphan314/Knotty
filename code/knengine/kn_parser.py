import sys
import os

from debugger import *
from genparser.src.astgen.parsing import lexer, parser

def get_output_str(input_path: str) -> str:
    output_list = get_output_tree(input_path)
    output_str = str(output_list) + '\n'
    return output_str

def get_output_tree(input_path: str) -> list:
    """Return parse-tree (possibly None)."""
    lexed_parsed = kn_parse(input_path)
    parsed = lexed_parsed['parsed']
    return parsed

def kn_parse(input_path: str) -> dict:
    """Return lexing sequence and ast."""
    lexicon_file = 'kn_lexicon.txt'
    grammar_file = 'kn_grammar.txt'

    lexicon_file = complete_path(lexicon_file)
    grammar_file = complete_path(grammar_file)

    lexer_inst = lexer.Lexer(lexicon_file)
    allowed_terminals = lexer_inst.lexicon_dict.keys()
    parser_inst = parser.Parser(grammar_file, allowed_terminals)

    lexed = lexer_inst.get_lexing_sequence_from_file(input_path)

    parsed = parser_inst.get_ast(lexed)
    if parsed is not None:
        parsed = list(parsed)

    lexed_parsed = {'lexed': lexed, 'parsed': parsed}
    return lexed_parsed

def complete_path(incomplete_path: str) -> str:
    """Add current directory to file name.

    Idea of Evgenii Balai.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    complete_path = os.path.join(current_dir, incomplete_path)
    return complete_path

if __name__ == '__main__':
    input_path = sys.argv[1]
    output_str = get_output_str(input_path)
    print(output_str)
