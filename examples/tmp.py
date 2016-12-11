import kn_lib

check_list = []




kn_lib.write_tex_file(check_list, r'../examples/tmp.tex', 'w')

syntax_tree = \
  ('kn_root'
  )

lexing_sequence = [('key_fun', 'function'), ('kn_id', 'X'), ('l_paren', '('), ('kn_num', 'i'), ('r_paren', ')'), ('key_ret', 'return'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('kn_num', '2'), ('op_minus', '-'), ('kn_id', 't'), ('op_exp', '^'), ('op_minus', '-'), ('kn_num', '2')]
