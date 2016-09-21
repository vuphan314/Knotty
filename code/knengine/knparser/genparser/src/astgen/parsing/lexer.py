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

import re
import collections


class Lexer:
    """Defines  a class that can be used to obtain a
    lexing sequence given an input file and a lexicon file
    """

    def __init__(self, lexicon_file, use_builtins=False):
        """Read the lexicon file and store a dictionary
        mapping lexeme names into corresponding regular expressions
        """
        with open(lexicon_file) as lf:
            lines = lf.readlines()

        # create an instance of lexicon dictionary
        self.lexicon_dict = collections.OrderedDict()

        # add built-in lexemes to the dictionary:
        if use_builtins:
            self.__add_builtin_lexemes()

        # read the lexicon file line by line and
        for line_number in range(len(lines)):
            line = lines[line_number]
            # skip empty lines:
            if Lexer.__is_empty_line(line):
                continue

            # read declaration from a string and raise exceptions if it
            # not of the right form
            (identifier, regular_expression) = Lexer.__parse_declaration(line)

            if identifier is None and regular_expression is None:
                raise InvalidLexemeDeclaration(line, line_number + 1)

            if identifier is None:
                raise InvalidIdentifier(line, line_number + 1)

            if regular_expression is None:
                raise InvalidRegularExpression(line, line_number + 1)

            if identifier in self.lexicon_dict:
                raise RepeatedDeclaration(identifier, line_number + 1)

            self.lexicon_dict[identifier] = regular_expression

    def get_lexing_sequence_from_file(self, input_file):

        with open(input_file, 'r') as inf:
            content = inf.read()

        return self.get_lexing_sequence(content)

    def get_lexing_sequence(self, content):
        """The method returns a lexing sequence of the form
        [(l_0,s_0),...,(l_n,s_n)], where s1+...+sn is the file content
        and l_0,...,l_n are lexeme types as defined in the specification
        """

        lexing_sequence = []

        # find the maximum prefix of the content such that it matches at least one
        # of the regular expressions in the file
        # Note that if there are multiple such regular expression, the first one
        # found will be used

        while content:
            prefix_found = False
            for last_pref_index in range(len(content), -1, -1):
                prefix = content[0:last_pref_index + 1]
                regex_found = False
                for l_type in self.lexicon_dict:
                    if self.lexicon_dict[l_type].match(prefix) is not None:
                        lexing_sequence.append((l_type, prefix))
                        regex_found = True
                        break
                if regex_found:
                    content = content[last_pref_index + 1:]
                    prefix_found = True
                    break
            if not prefix_found:
                raise LexingStuckError(lexing_sequence, content)

        return lexing_sequence

    def __add_builtin_lexemes(self):
        """The method extends the lexicon dictionary by adding built in lexemes
        with corresponding regular expressions
        """
        self.lexicon_dict["num"] = re.compile(
            r"^(-?[1-9][0-9]*"
            r"|-?0\.[0-9]+"
            r"|-?[1-9][0-9]+\.[0-9]+)\Z")

        self.lexicon_dict["spaces"] = re.compile(r"^\s+\Z")
        self.lexicon_dict["id"] = re.compile(r"^[a-zA-Z]\w*\Z")

    @staticmethod
    def __is_empty_line(line):

        return line.isspace() or line == ""

    @staticmethod
    def __parse_declaration(line):
        """ The method returns a pair (id, regex) for the declaration
        id = regex, where id is an identifier and regex is an instance of python
        regular expression object
        If the line does not start with id = , the result is (None, None).
        If the line is of the form id = expr, but expr is not a valid python regular
        expression, the method returns (id,None)
        """

        # check if the line is of the form id = regular_expression
        # and store the id and regular expression
        if line.find('=') == -1:
            return None, None

        lhs = line[0:line.index("=")].strip()
        identifier = Lexer.__parse_identifier(lhs)

        rhs = line[line.index("=") + 1:].strip()
        regular_expression = Lexer.__parse_regular_expression(rhs)

        return identifier, regular_expression

    @staticmethod
    def __parse_identifier(id_str):
        """ Return id_str if  id_str is an identifier and None otherwise """
        regex = re.compile(r"^[a-zA-Z]\w*\Z")
        if regex.match(id_str) is not None:
            return id_str
        else:
            return None

    @staticmethod
    def __parse_regular_expression(string):
        try:
            regular_expression = re.compile("^(" + string + r")\Z")
        except re.error:
            regular_expression = None

        return regular_expression


class InvalidLexemeDeclaration(Exception):
    """
    Defines a class for representing exceptions which are thrown in the event of
    an invalid lexeme declaration in the lexicon file
    """

    def __init__(self, declaration, line_number):
        super(InvalidLexemeDeclaration, self).__init__()
        self.declaration = declaration
        self.line_number = line_number

    def __repr__(self):
        return "The lexicon file contains an invalid " \
               "lexeme declaration: " + str(self.declaration) + " at line" \
                                                                "number " + str(self.line_number) + "."

    def __str__(self):
        return self.__repr__()


class InvalidRegularExpression(Exception):
    """
    Defines a class for representing exceptions which are thrown in the event of
    an invalid regular expression in the lexicon file
    """

    def __init__(self, declaration, line_number):
        super(InvalidRegularExpression, self).__init__()
        self.declaration = declaration
        self.line_number = line_number

    def __repr__(self):
        return "The lexicon file contains an invalid " \
               "regular expression on the right hand side of the declaration: " \
               + str(self.declaration) + " at line" \
                                         " number " + str(self.line_number) + "."

    def __str__(self):
        return self.__repr__()


class RepeatedDeclaration(Exception):
    """
    Defines a class for representing exceptions which are thrown in the event of
    an invalid lexeme declaration given in the lexicon file
    """

    def __init__(self, lexeme_type, line_number):
        super(RepeatedDeclaration, self).__init__()
        self.lexeme_type = lexeme_type
        self.line_number = line_number

    def __repr__(self):
        return "The lexeme type " + self.lexeme_type + " is declared for" \
                                                       " the second time at line " + str(self.line_number) + "."

    def __str__(self):
        return self.__repr__()


class InvalidIdentifier(Exception):
    """
    Defines a class for representing exceptions which are thrown in the event of
    an invalid regular expression in the lexicon file
    """

    def __init__(self, declaration, line_number):
        super(InvalidIdentifier, self).__init__()
        self.declaration = declaration
        self.line_number = line_number

    def __repr__(self):
        return "The lexicon file contains an invalid " \
               "identifier on the left hand side of the a declaration: " \
               + str(self.declaration) + " at line" \
               " number " + str(self.line_number) + "."

    def __str__(self):
        return self.__repr__()


class LexingStuckError(Exception):
    """
    Defines a class for representing exceptions which are thrown in the event when
    lexing cannot proceed starting from some position in the file
    """

    def __init__(self, lexing_sequence, suffix):
        super(LexingStuckError, self).__init__()
        self.lexing_sequence = lexing_sequence
        self.suffix = suffix

    @property
    def __repr__(self):
        return "The lexing cannot proceed starting from  " \
               + self.suffix + ". The lexing sequence obtained so far is: " \
               + str(self.lexing_sequence) + "."

    def __str__(self):
        return self.__repr__
