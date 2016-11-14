import os
import re
import sys

from genparser.src.astgen.parsing import ast, lexer, parser
from vu_toolkit.vu_debugger import *
import kn_handler

############################################################

def parse_file(kn_path: str) -> dict:
    """Return lexing_sequence, syntax_tree, syntax_str."""

    kn_parser_inst = KnParser(kn_path)

    syntax_dict = {
        'lexing_sequence':kn_parser_inst.lexing_sequence
    }

    syntax_tree = get_syntax_tree(
        kn_parser_inst.syntax_list
    )
    syntax_str = get_syntax_str(syntax_tree)

    syntax_dict.update(
        syntax_tree=syntax_tree, syntax_str=syntax_str
    )

    return syntax_dict

############################################################
# invoke Evgenii's generic parser

class KnParser:
    """Parse Knotty program."""

    def __init__(self, kn_path: str):
        self.kn_strs = KnPreprocessor(
            kn_path
        ).get_preprocessed()

        self.lexing_sequence = []
        self.syntax_list = ['kn_root']

        lexicon_file, grammar_file = map(
            self.get_complete_path,
            ['kn_lexicon.txt', 'kn_grammar.txt']
        )

        self.lexer_inst = lexer.Lexer(lexicon_file)
        self.parser_inst = parser.Parser(
            grammar_file,
            self.lexer_inst.lexicon_dict.keys()
        )

        self.parse_preprocessed()

    def parse_preprocessed(self):
        """Add to `lexing_sequence`, `syntax_list`.

        Of `self`.
        """

        for st in self.kn_strs:
            lex_list = self.get_spaceless_lexing_sequence(
                self.lexer_inst.get_lexing_sequence(st)
            )
            self.lexing_sequence.extend(lex_list)

            ast_inst = self.parser_inst.get_ast(lex_list)
            if ast_inst is not None:
                self.syntax_list.extend(
                    ast_inst.children_list()
                )

    @staticmethod
    def get_spaceless_lexing_sequence(
        lexing_sequence: list
    ) -> list:
        lis = [
            tup for tup in lexing_sequence
            if tup[0] != 'spaces'
        ]
        return lis

    def get_syntax_dict(kn_path: str) -> dict:
        """Return lexing_sequence and syntax_AST."""

        syntax_dict = {
            'lexing_sequence': lexing_sequence,
            'syntax_AST': syntax_AST
        }
        return syntax_dict

    @staticmethod
    def get_complete_path(incomplete_path: str) -> str:
        """Add current directory to file name."""

        current_dir = os.path.dirname(
            os.path.abspath(__file__)
        )
        complete_path = os.path.join(
            current_dir, incomplete_path
        )
        return complete_path

############################################################

class KnPreprocessor:
    """Trim comments and split into statements."""

    def __init__(self, kn_path):
        with open(kn_path) as kn_file:
            st = kn_file.read()
        self.kn_str = st
        self.kn_strs = []

    def get_preprocessed(self) -> list:
        self.kn_str = self.get_uncommented(self.kn_str)
        self.split_into_statements()
        return self.kn_strs

    def get_uncommented(self, kn_str: str) -> str:
        """Recursively trim comments."""

        comment_start = re.search(r'/\*', kn_str)
        if comment_start is None:
            return kn_str
        else:
            comment_end = re.compile(r'\*/').search(
                kn_str, comment_start.end()
            )
            if comment_end is None:
                raise kn_handler.PreprocessingError(
                    'Unclosed comment.'
                )
            else:
                left_half = kn_str[:comment_start.start()]
                right_half = kn_str[comment_end.end():]
                right_half = self.get_uncommented(right_half)
                st = left_half + right_half
                return st

    def split_into_statements(self) -> None:
        """Add to `self.kn_strs`.

        Leave `self.kn_str` intact.
        """

        stmt_keywords = re.compile(
            r'\b(vary|define|check)\b'
        )
        st = self.kn_str # immutable str
        first_stmt = stmt_keywords.search(st)
        if first_stmt is not None:
            if not self.is_all_space(
                st[:first_stmt.start()]
            ):
                raise kn_handler.PreprocessingError(
                    'Nonspace character found '
                    'before first statement keyword.'
                )
            else:
                current_stmt = first_stmt
                done = False
                while not done: # shorten `st`
                    next_stmt = stmt_keywords.search(
                        st, current_stmt.end()
                    )
                    if next_stmt is None:
                        self.kn_strs.append(st.strip())
                        done = True
                    else:
                        splitting_index = next_stmt.start()
                        self.kn_strs.append(
                            st[:splitting_index].strip()
                        )
                        st = st[splitting_index:]

    @staticmethod
    def is_all_space(st: str) -> bool:
        return st == '' or st.isspace()

############################################################
# list to tree

def get_syntax_tree(syntax_list: list) -> tuple:
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
# tree to str

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
