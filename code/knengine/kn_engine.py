'''Knotty engine (source).'''

############################################################

import os
import sys

from debugger import *
import kn_parser
import kn_translator

############################################################

def write_output_files(kn_path: str) -> list:
    """Write Python file and then TeX file.

    Return check_list to be used by kn_tester.
    """
    
    py_path, tex_path = [
        append_base_path(kn_path, ext)
        for ext in ['.py', '.tex']
    ]

    syntax_dict = kn_parser.parse_file(kn_path)
    
    py_str = write_py_parsed(syntax_dict)
    py_str += write_py_translated(
        syntax_dict, tex_path
    )

    # write .py
    with open(py_path, 'w') as py_file:
        py_file.write(py_str)

    # write .tex
    py_module = import_py_module(py_path)

    msg = '''
OVERWROTE/created files {}, {}.
'''.format(py_path, tex_path)
    print(msg)

    return py_module.check_list

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
    syntax_dict: dict, tex_path: str
) -> str:
    syntax_tree = syntax_dict['syntax_tree']
    st = kn_translator.translate_tree(
        syntax_tree, tex_path
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

def main() -> None:
    kn_path = sys.argv[1]
    write_output_files(kn_path)

if __name__ == '__main__':
    main()
