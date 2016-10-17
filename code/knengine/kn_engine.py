import sys
import os
import importlib

from debugger import *
import kn_parser
import kn_translator

############################################################

def write_output_files(kn_path: str) -> list:
    """Receive in path as 1st command-line argument."""
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
    py_module = run_py_module(py_path)
    
    mess = '''
OVERWROTE/created files {}, {}.
'''.format(py_path, tex_path)
    print(mess)
    
    return py_module.check_list

############################################################
# helper writers

def write_py_parsed(parse_dict: dict) -> str:
    parse_str = parse_dict['parse_str']
    st = '''
parse_tree = \\
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

def run_py_module(py_path: str):
    py_module_name = get_py_module_name(py_path)
    mod = importlib.import_module(py_module_name)
    return mod

def get_py_module_name(py_path: str) -> str:
    # trim '.py'
    py_module_name = os.path.splitext(py_path)[0]

    for sep in {'\\', '/'}:
        py_module_name = py_module_name.replace(sep, '.')
    return py_module_name

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

if __name__ == '__main__':
    kn_path = sys.argv[1]
    write_output_files(kn_path)
