import sys
sys.path.insert(1, 'knparser/')
import os

from tester import *
from knparser import kn_parser

def write_output_file():
    """Receive input path as 1st command-line argument."""
    args = sys.argv
    if len(args) == 1:
        demo_input_path = 'examples/demo.kn'
        demo_output_path = get_output_path(demo_input_path)
        mess = ('\n'
            'Example invocation:' '\n\n\t'
            'py kn_engine.py ' + demo_input_path + ' \n\n'
            'The output file ' + demo_output_path + ' will be '
            'OVERWRITTEN/created.' '\n')
        print(mess)
        input('Key `Enter` to quit.' '\n')
    else:
        input_path = sys.argv[1]
        output_path = get_output_path(input_path)
        output_string = get_output_string(input_path)
        with open(output_path, 'w') as output_file:
            output_file.write(output_string)
        print('\n' 'OVERWROTE/created file ' + output_path + '.')

def get_output_string(input_path: str) -> str:
    """Return str (to be written in output file)."""
    lexed_parsed = kn_parser.kn_parse(input_path)
    parsed = lexed_parsed['parsed']
    parsed = str(parsed) + '\n'
    return parsed

def get_output_path(input_path: str) -> str:
    """Return output path (aka appended base path)."""
    base_appendage = '_parsed_auto.txt'
    base_path = os.path.splitext(input_path)[0]
    output_path = base_path + base_appendage
    return output_path

if __name__ == '__main__':
    write_output_file()
