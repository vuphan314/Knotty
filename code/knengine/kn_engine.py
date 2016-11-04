'''Knotty engine (source).'''

############################################################

TAG_NAME = 'v1.2.0'
TAG_DATE = '2016-10-26'

############################################################

import argparse
import os
import sys

from vu_toolkit.vu_debugger import *
import kn_parser
import kn_translator

############################################################

def write_output_files(
    kn_path: str, force: bool, keep: bool
) -> list:
    """Write Python file and then TeX file.

    Return check_list to be used by kn_tester.
    """

    py_path, tex_path = [
        append_base_path(kn_path, ext)
        for ext in ['.py', '.tex']
    ]

    syntax_dict = kn_parser.parse_file(kn_path)

    write_mode = 'w' if force else 'x'

    py_str = (
        write_py_parsed(syntax_dict) +
        write_py_translated(
            syntax_dict, tex_path, write_mode
        )
    )

    # write .py
    with open(py_path, write_mode) as py_file:
        py_file.write(py_str)

    # write .tex
    check_list = import_py_module(py_path).check_list

    # remove .py
    if not keep:
        os.remove(py_path)

    msg = '''
OVERWROTE/created file {}.
'''.format(tex_path)
    print(msg)

    return check_list

############################################################
# helper writers

def write_py_parsed(syntax_dict: dict) -> str:
    lexing_sequence = syntax_dict['lexing_sequence']
    syntax_str = syntax_dict['syntax_str']

    st = r'''
lexing_sequence = {}

syntax_tree = \
{}
'''.format(lexing_sequence, syntax_str)

    return st

def write_py_translated(
    syntax_dict: dict, tex_path: str, write_mode: str
) -> str:
    syntax_tree = syntax_dict['syntax_tree']
    st = kn_translator.translate_tree(
        syntax_tree, tex_path, write_mode
    )
    return st

def import_py_module(py_path: str):
    py_dir, py_module_name = os.path.split(py_path)
    py_module_name = os.path.splitext(py_module_name)[0]

    sys.path.insert(0, py_dir)
    py_module = __import__(py_module_name)

    return py_module # <class 'module'>

############################################################
# miscellaneous

def append_base_path(
    kn_path: str, base_appendage: str
) -> str:
    """Return output path.

    (Base path appended with output ext.)
    """
    base_path = os.path.splitext(kn_path)[0]
    appended_path = base_path + base_appendage
    return appended_path

############################################################

class ArgvParser(argparse.ArgumentParser):
    """Parse argument vector."""
    def __init__(self):
        super().__init__()

        self.add_argument('Knotty_file')

        self.add_argument(
            '-f', '--force', action='store_true',
            help='OVERWRITE existing .py and .tex files'
        )

        self.add_argument(
            '-k', '--keep', action='store_true',
            help='keep .py file'
        )

############################################################

def printWelcome():
    st = '''
Knotty engine {} built {}
'''.format(TAG_NAME, TAG_DATE)
    print(st)

printWelcome()

############################################################

def main() -> None:
    argv_parser = ArgvParser()
    if len(sys.argv) == 1:
        argv_parser.print_help()
    else:
        parsed_argv = argv_parser.parse_args()

        kn_path = parsed_argv.Knotty_file
        force = parsed_argv.force
        keep = parsed_argv.keep

        write_output_files(kn_path, force, keep)

if __name__ == '__main__':
    main()
