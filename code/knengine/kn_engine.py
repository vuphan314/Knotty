import sys
import os
import importlib

from debugger import *
import kn_parser
import kn_translator

############################################################

which_engine = 'kn_engine.py'
examples_path = 'examples/'
base_appendage = '_auto.py'

def write_output_file(
        which_engine: str, base_appendage: str
        ) -> None:
    """Receive input path as 1st command-line argument."""
    args = sys.argv
    if len(args) == 1:
        demo_input_path = examples_path + 'demo.kn'
        demo_output_path = \
            get_output_path(demo_input_path, base_appendage)
        mess = ('\n'
            'Example invocation:' '\n\n\t' +
            which_engine + ' ' + demo_input_path + ' \n\n'
            'The output file ' + demo_output_path + ' will be '
            'OVERWRITTEN/created.' '\n')
        print(mess)
        input('Key `Enter` to quit.' '\n')
    else:
        input_path = sys.argv[1]
        translate_str = get_translate_str(input_path)
        output_path = get_output_path(
            input_path, base_appendage)
        with open(output_path, 'w') as output_file:
            output_file.write(translate_str)
            run_output_module(output_path)
        print(
            '\n' 'OVERWROTE/created file ' +
            output_path + '.')

def get_translate_str(input_path):
    parse_tree = kn_parser.kn_parse(input_path)
    translate_str = kn_translator.kn_translate(parse_tree)
    return translate_str

def get_output_path(
        input_path: str, base_appendage: str
        ) -> str:
    """Return output path (aka appended base path)."""
    base_path = os.path.splitext(input_path)[0]
    output_path = base_path + base_appendage
    return output_path

def run_output_module(output_path: str) -> None:
    output_module = get_output_module(output_path)
    importlib.import_module(output_module)
    tst()

def get_output_module(output_path: str) -> str:
    output_module = os.path.splitext(output_path)[0]
    output_module = output_module.replace('\\', '.')
    return output_module

############################################################

if __name__ == '__main__':
    write_output_file(which_engine, base_appendage)
