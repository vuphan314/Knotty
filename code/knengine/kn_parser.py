from debugger import *
from genparser.src.astgen.parsing import lexer, parser
import os
def kn_parse(input_path: str) -> dict:
    """Return lexing sequence and ast."""
    # knparser_path = 'knparser/' # working dir: knengine/
    knparser_path = '' # working dir: knengine/
    lexicon_file = knparser_path + 'kn_lexicon.txt'
    grammar_file = knparser_path + 'kn_grammar.txt'


    lexicon_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), lexicon_file)
    grammar_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), grammar_file)

    lexer_inst = lexer.Lexer(lexicon_file)
    allowed_terminals = lexer_inst.lexicon_dict.keys()
    parser_inst = parser.Parser(grammar_file, allowed_terminals)

    lexed = lexer_inst.get_lexing_sequence_from_file(input_path)

    parsed = parser_inst.get_ast(lexed)
    if parsed is not None:
        parsed = list(parsed)

    lexed_parsed = {'lexed': lexed, 'parsed': parsed}
    return lexed_parsed
