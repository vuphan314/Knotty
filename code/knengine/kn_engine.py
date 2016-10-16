import sys
import os
import importlib

from debugger import *
import kn_parser
import kn_translator

############################################################

which_engine = 'kn_engine.py'
examples_path = 'examples/'

def write_output_file(which_engine: str) -> None:
    """Receive input path as 1st command-line argument."""
    args = sys.argv
    if len(args) == 1:
        demo_kn_path = examples_path + 'demo.kn'
        demo_py_path = \
            append_base_path(demo_kn_path, '.py')
        mess = ('\n'
            'Example invocation:' '\n\n\t' +
            which_engine + ' ' + demo_kn_path + ' \n\n'
            'The output file ' + demo_py_path + ' will be '
            'OVERWRITTEN/created.' '\n')
        print(mess)
        input('Key `Enter` to quit.' '\n')
    else:
        kn_path = sys.argv[1]
        py_path = append_base_path(kn_path, '.py')
        tex_path = append_base_path(kn_path, '.tex')

        parse_dict = kn_parser.kn_parse(kn_path)
        output_str = write_py_parsed(parse_dict)
        output_str += write_py_translated(
                parse_dict, tex_path
            )

        with open(py_path, 'w') as py_file:
            py_file.write(output_str)
        run_py_module(py_path)

        print(
            '\n' 'OVERWROTE/created file ' +
            py_path + '.')

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

def append_base_path(
            kn_path: str, base_appendage: str
        ) -> str:
    """Return output path (aka appended base path)."""
    base_path = os.path.splitext(kn_path)[0]
    py_path = base_path + base_appendage
    return py_path

def run_py_module(py_path: str) -> None:
    py_module = get_py_module(py_path)
    importlib.import_module(py_module)

def get_py_module(py_path: str) -> str:
    py_module = os.path.splitext(py_path)[0] # trim '.py'
    py_module = py_module.replace('\\', '.')
    return py_module

############################################################

if __name__ == '__main__':
    write_output_file(which_engine)
