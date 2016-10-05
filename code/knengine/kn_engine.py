import sys
# sys.path.insert(1, 'knparser/')
import os

from debugger import *
# from knparser import kn_parser
import kn_parser

which_engine = 'kn_engine.py'
examples_path = 'examples/'
base_appendage = '_parsed_auto.txt'

def write_output_file(which_engine: str, base_appendage: str) -> None:
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
        output_path = get_output_path(input_path, base_appendage)
        output_str = get_output_str(input_path)
        with open(output_path, 'w') as output_file:
            output_file.write(output_str)
        print('\n' 'OVERWROTE/created file ' + output_path + '.')

def get_output_str(input_path: str) -> str:
    output_list = get_output_tree(input_path)
    output_str = str(output_list) + '\n'
    return output_str

def get_output_tree(input_path: str) -> list:
    """Return parse-tree (possibly None)."""
    lexed_parsed = kn_parser.kn_parse(input_path)
    parsed = lexed_parsed['parsed']
    return parsed

def get_output_path(input_path: str, base_appendage: str) -> str:
    """Return output path (aka appended base path)."""
    base_path = os.path.splitext(input_path)[0]
    output_path = base_path + base_appendage
    return output_path

if __name__ == '__main__':
    write_output_file(which_engine, base_appendage)
