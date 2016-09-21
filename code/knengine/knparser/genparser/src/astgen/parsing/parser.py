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

# fix line numbers; add parsing function!

import re
from .ast import AST

# constants:
# list of operations allowed on trees
ALLOWED_OPERATIONS = ['cut_root']


class Parser:
    """Defines  a class that can be used to obtain an
    abstract syntax tree given a grammar file and a sequence of
    annotated lexemes
    """

    def __init__(self, grammar_file, allowed_terminals):
        """Read the grammar file and store a list of all grammar rules
        Raise an exception in case of a syntax error or if a rule
        in grammar file contains an undefined non-terminal
        """

        self.terminals = allowed_terminals

        with open(grammar_file) as gf:
            lines = gf.readlines()

        # create list of production rules
        self.grammar_rules = []

        # read the grammar file line by line and

        # a list that stores line numbers for the rules
        # rule_line[i] is the line of the i-th rule;
        self.rule_lines = []

        # parse lines one by one
        for line_number in range(len(lines)):
            line = lines[line_number]
            # skip empty lines:
            if Parser.__is_empty_line(line):
                continue

            # read a grammar rule from line and raise exceptions if it
            # not of the right form
            try:
                rule = GrammarRule(line)
            except InvalidGrammarRule as invalid_rule:
                invalid_rule.set_line(line_number + 1)
                raise invalid_rule

            self.grammar_rules.append(rule)
            self.rule_lines.append(line_number + 1)

        # obtain list of non-terminals of the grammar
        self.non_terminals = [rule.non_term for rule in self.grammar_rules]

        # check grammar rules for satisfying the conditions specified
        # in the documentation
        self.__check_rules()





    def get_ast(self, lexing_sequence, ignore_spaces=True, starting_symbol=None):
        """ get abstract syntax tree from the lexing sequence
        If ignore_spaces = True, drop all lexemes annotated by spaces type
        If starting symbol is provided, generate a tree from a production with the symbol
        on the left hand side; otherwise generate a tree where
        the starting non-terminal occurs in the LHS of the first rule of the grammar
        """
        # remove all spaces if needed
        if ignore_spaces:
            lexing_sequence = [l for l in lexing_sequence if l[0] != 'spaces']

        # The result of the parsing is defined to be the abstract
        # syntax tree matching the lexing sequence l_1 , . . . , l_n
        # on the starting symbol of G.

        if starting_symbol is None:
               starting_symbol = self.grammar_rules[0].non_term

        # create dictionaries for memoisation of functions __r and __r_aux
        dict_r = {}
        dict_r_aux = {}

        # Call the R function defined in the document.
        return self.__r(starting_symbol, 0, len(lexing_sequence) - 1, lexing_sequence, dict_r, dict_r_aux)

    def __r(self, symbol, b, e, lexing_sequence, dict_r, dict_r_aux):
        """The function returns an abstract syntax tree R(S,b,e) as specified
        in section 3.4 of the document or None if the tree does not exist
        """
        # check if the value was previously computed
        # and return the computed value if this is the case
        if (symbol, b, e) in dict_r:
            return dict_r[(symbol, b, e)]

        # if b = e and S is lb , RG,L (S, b, e) contains only one node
        # labeled by (lb , sb )
        if b == e and symbol == lexing_sequence[b][0]:
            return AST(lexing_sequence[b])

        # if S is a non-terminal of G,
        if symbol in self.non_terminals:
            # and there is a statement in G of the form
            # S(b 1 . . . b m ) = a 1 (t 1 ) . . . a n (t n )
            for rule in self.grammar_rules:
                if rule.non_term == symbol:
                    # here we will use a recursive auxiliary function that
                    # will try all possible values for k1,...,kn
                    # to find a suitable combination (page 7 of the doc)
                    # we will start from searching for the value of k1
                    # corresponding to rhs_i = 0 in __r_aux call
                    ast_list = self.__r_aux(b, e, lexing_sequence, rule, 0, dict_r, dict_r_aux)
                    if ast_list is not None:
                        # build the tree !
                        # check if b_1 is a member of tau_1
                        # and, if so, return the corresponding tree
                        beta_0 = rule.beta_list[0]
                        if beta_0 in rule.tau_list:
                            dict_r[(symbol, b, e)] = ast_list\
                                             [rule.tau_list.index(beta_0)]
                            return ast_list[rule.tau_list.index(beta_0)]

                        # else we construct a tree with a root b_0
                        # and some children
                        root = rule.beta_list[0]
                        children = []
                        for beta in rule.beta_list[1:]:
                            # if beta is in tau list, we attach
                            # the tree corresponding to a_i
                            # to the root of the tree we construct
                            if beta in rule.tau_list:
                                tree_idx = rule.tau_list.index(beta)
                                children.append(ast_list[tree_idx].repr())
                            else:
                                # beta is of the form operation(tau)
                                operation = beta[:beta.find('(')]
                                tau = beta[beta.find('(') + 1:-1]
                                tree_idx = rule.tau_list.index(tau)

                                children += {
                                    'cut_root':
                                    ast_list[tree_idx].children_list()
                                }[operation]
                        dict_r[(symbol, b, e)] = AST(root, children)
                        return  AST(root, children)
        dict_r[(symbol, b, e)] = None


    def __r_aux(self, b, e, lexing_sequence, rule, rhs_i, dict_r, dict_r_aux):
        """Let the rule be S(b_1 ... b_m ) = a_0 (t_0) ... a_(n-1) (t_(n-1))
        and the lexing sequence be l_0,...,l_(k-1).
        The function returns a list of abstract trees t_0,...,t_(n-rhs_i)
        such that for 0<=j<=(n-rhs_i+1) t_j is an abstract syntax tree
        matching a sequence
        l_(b+k_(rhs_i)+...+k_(rhs_i+j-1))...l_(b+rhs_i+...+k_(rhs_i+j)-1)
        on the symbol alpha_(rhs_i)
        """

        if (b, e, rule, rhs_i) in dict_r_aux:
            return dict_r_aux[(b, e, rule, rhs_i)]

        n = len(rule.alpha_list)

        # if rhs_i = n-1, we are at the last symbol of the rhs of the rule
        # in this case we need to match alpha_(n-1)
        # with the entire sequence left
        if rhs_i == n - 1:
            tree = self.__r(rule.alpha_list[rhs_i], b, e, lexing_sequence, dict_r, dict_r_aux)
            result = [tree] if tree is not None else None
            dict_r_aux[(b, e, rule, rhs_i)] = result
            return result

        # searching for cur_k_size = k_(k_index) from 1 up to the maximum
        # number such that there is still at least one non-terminal in
        # the sequence l_(b+k_(k_index+1)+...+k_(index+i))...l_e
        # for each of the remaining alpha_(k_index+1)...alpha_n
        for cur_k_size in range(1, e - b - n + rhs_i + 3):
            # try to build t_0
            t_head = self.__r(rule.alpha_list[rhs_i], b,
                              b + cur_k_size - 1, lexing_sequence, dict_r, dict_r_aux)
            if t_head is not None:
                # try to build t_1,...,t_(n-k_index)
                t_tail = self.__r_aux(b + cur_k_size, e,
                                      lexing_sequence, rule, rhs_i + 1, dict_r, dict_r_aux)
                if t_tail is not None:
                    dict_r_aux[(b, e, rule, rhs_i)] = [t_head] + t_tail
                    return [t_head] + t_tail
        dict_r_aux[(b, e, rule, rhs_i)] = None

    def __check_rules(self):
        """ # check rules for conditions specified in the documentation"""

        for rule_idx in range(len(self.grammar_rules)):
            rule = self.grammar_rules[rule_idx]

            # rule_ok = True iff the rule satisfies all the conditions
            rule_ok = True

            #1. A non-terminal name is not the same as any terminal name
            if rule.non_term in self.terminals:
                rule_ok = False

            # 2. Each beta_i for i>=1 is of one of the forms c or f(c),
            # where c is an element of the sequence tau_1 ... tau_n; and
            #       f is an operation
            # note: the fact that f is an operation was checked previously
            # each beta_i occurs in tau_1 ... tau_n exactly once
            #
            # If beta_0 is of one of the forms tau_j or f(tau_j),
            # for some j, then
            #    - beta_1 occurs in tau_1,..tau_n exactly once
            #    - m must be equal to 1,
            # otherwise beta_1 is an identifier

            for b_idx in range(0, len(rule.beta_list)):
                beta = rule.beta_list[b_idx]
                if beta.find('(') != -1:
                    rule_ok = rule_ok and beta[-1] == ')'
                    argument = beta[beta.find('(') + 1:-1]
                    if argument not in rule.tau_list or \
                       rule.tau_list.count(argument) > 1:
                        rule_ok = False
                else:
                    beta_in_tau = beta in rule.tau_list
                    if not beta_in_tau and b_idx > 0:
                        rule_ok = False

                    if beta_in_tau and b_idx == 0 and len(rule.beta_list) > 1:
                        rule_ok = False

                    if beta_in_tau and rule.tau_list.count(beta) > 1:
                        rule_ok = False

            # 3. each alpha_i is either a non-terminal or terminal
            # of the grammar

            for alpha in rule.alpha_list:
                if alpha not in self.non_terminals \
                        and alpha not in self.terminals:
                    rule_ok = False

            # raise an exception if the rule does not satisfy one
            # of the conditions
            if not rule_ok:
                invalid_rule_ex = InvalidGrammarRule(rule)
                invalid_rule_ex.set_line(self.rule_lines[rule_idx])
                raise invalid_rule_ex

    @staticmethod
    def __is_empty_line(line):
        return line.isspace() or line == ""


class GrammarRule:
    """Defines a production rule of the form

      """

    def __init__(self, line):
        """ parse a grammar  rule of the form
         nt(beta_1...beta_m) = alpha_1(tau_1)...alpha_n(tau_n) from the line
         """

        # store the line representing the rule
        self.raw_string = line.strip()

        # check if there is an ::= symbol in the line
        if line.find('::=') == -1:
            raise InvalidGrammarRule(line)

        # parse lhs
        lhs = line[0:line.index('::=')].strip()

        if lhs.find('(') == -1 or lhs[-1] != ')':
            raise InvalidGrammarRule(line)

        self.non_term = lhs[:lhs.find('(')]
        self.beta_list = lhs[lhs.find('(') + 1:-1].split()

        # parse rhs
        rhs_list = line[line.index('::=') + 3:].split()

        if not self.beta_list or not rhs_list:
            raise InvalidGrammarRule(line)

        self.alpha_list = []
        self.tau_list = []

        for rhs_term in rhs_list:
            if rhs_term.find('(') == -1:
                self.alpha_list.append(rhs_term)
                # we allow a shorthand alpha for alpha(alpha)
                self.tau_list.append(rhs_term)
            else:
                self.alpha_list.append(rhs_term[:rhs_term.find('(')])
                self.tau_list.append(rhs_term[rhs_term.find('(') + 1:-1])

        # check that all members of alpha and tau lists are identifiers:
        all_ok = True

        for rhs_id in self.tau_list + self.alpha_list:
            all_ok = all_ok and GrammarRule.__is_identifier(rhs_id)

        if not all_ok:
            raise InvalidGrammarRule(line)

        # check that all members of beta are either identifiers or of
        # the form cut_root(id), where id is an identifier

        for beta in self.beta_list:
            beta_ok = True

            if beta.find('(') == -1:
                # beta is an identifier
                beta_ok = beta_ok and GrammarRule.__is_identifier(beta)
            else:
                # beta is of the form operation(argument)
                beta_ok = True

                operation = beta[:beta.find('(')]
                beta_ok = beta_ok and beta[-1] == ')'

                argument = beta[beta.find('(') + 1:-1]
                beta_ok = beta_ok and GrammarRule.__is_identifier(argument)
                beta_ok = beta_ok and operation in ALLOWED_OPERATIONS

            if not beta_ok:
                raise InvalidGrammarRule(line)

    def __repr__(self):
        return self.raw_string

    def __str__(self):
        return self.__repr__()

    @staticmethod
    def __is_identifier(id_str):
        """ Return true if  id is an identifier and False otherwise """
        regex = re.compile(r"^[a-zA-Z]\w*\Z")
        return regex.match(id_str) is not None


class InvalidGrammarRule(Exception):
    """
    Defines a class for representing exceptions which are thrown in the event of
    an invalid lexeme declaration in the lexicon file
    """

    def __init__(self, rule):
        super(InvalidGrammarRule, self).__init__()
        self.rule = rule
        self.line_number = None

    def __repr__(self):
        return "The grammar file contains an invalid " \
               "grammar rule: " + str(self.rule) + " at line" \
                                                   " number " + str(self.line_number) + "."

    def __str__(self):
        return self.__repr__()

    def set_line(self, line_number):
        self.line_number = line_number
