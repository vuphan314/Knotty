"""
Copyright (c) 2014, Evgenii Balai
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.
2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY EVGENII BALAI "AS IS" AND
ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL EVGENII BALAI OR CONTRIBUTORS BE LIABLE FOR
ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
(INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

The views and conclusions contained in the software and documentation are those
of the authors and should not be interpreted as representing official policies,
either expressed or implied, of the FreeBSD Project.
"""


from optparse import OptionParser
from parsing.parser import Parser
from parsing.lexer import *



def parse_arguments():
    """
    Returns the arguments passed to the program. The arguments are parsed from sys.argv.
    """

    parser = OptionParser()
    parser.add_option("-s", action="store_false",
                      dest="ignore_spaces", default=True)

    parser.add_option("-b", action="store_true",
                      dest="use_builtin_lexemes", default=False)

    return parser.parse_args()


def main():
    """
    Main entry point into the program.  Parse the command line arguments of the
    form  [lexicon_file grammar_file source_file].
    Calls lexer to obtain a sequence L of annotated lexemes from the source file
    and lexicon file. Calls parser to obtain an abstract syntax tree from L and
    grammar file and print it.
    """

    # read arguments
    (options, args) = parse_arguments()

    (lexicon_file, grammar_file, input_file) = args

    # create lexer instance
    lexer_instance = Lexer(lexicon_file, options.use_builtin_lexemes)

    # obtain lexing sequence from the input file
    lexing_sequence = lexer_instance.get_lexing_sequence_from_file(input_file)

    # create parser instance
    parser_instance = Parser(grammar_file, lexer_instance.lexicon_dict.keys())

    # obtain abstract syntax tree from the lexing sequence

    print(parser_instance.get_ast(lexing_sequence, options.ignore_spaces))


if __name__ == '__main__':
    main()
