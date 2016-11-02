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
    
    Return check-list to be used by unit-tester.
    """
    py_path, tex_path = [
        append_base_path(kn_path, ext)
        for ext in ['.py', '.tex']
    ]

    parse_dict = kn_parser.kn_parse(kn_path)
    out_str = write_py_parsed(parse_dict)
    out_str += write_py_translated(
        parse_dict, tex_path
    )

    # write .py
    with open(py_path, 'w') as py_file:
        py_file.write(out_str)

    # write .tex
    py_module = import_py_module(py_path)

    msg = '''
OVERWROTE/created files {}, {}.
'''.format(py_path, tex_path)
    print(msg)
    
    return py_module.check_list

############################################################
# helper writers

def write_py_parsed(parse_dict: dict) -> str:
    parse_str = parse_dict['parse_str']
    st = r'''
parse_tree = \
{parse_str}
'''.format(parse_str = parse_str)
    return st

def write_py_translated(
    parse_dict: dict, tex_path: str
) -> str:
    parse_tuple = parse_dict['parse_tuple']
    translate_script = kn_translator.kn_translate(
        parse_tuple, tex_path
    )
    return translate_script

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
    """Return out path (aka appended base path)."""
    base_path = os.path.splitext(kn_path)[0]
    appended_path = base_path + base_appendage
    return appended_path

############################################################

def main() -> None:
    kn_path = sys.argv[1]
    write_output_files(kn_path)

if __name__ == '__main__':
    main()
