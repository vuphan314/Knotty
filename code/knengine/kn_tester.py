import unittest

import kn_engine

file_tree_dict = {
        'empty.kn':
            None,
        'oneliner.kn':
            ['knStats', ['funDef', ['formFunExpr', ('kn_id', 'c')], ['defBody', ['letCls', ['letCl', ('kn_id', 'tmp'), ('kn_numeral', '1')]], ['retCl', ['condTerm', ('kn_id', 'tmp'), ('key_truth', 'true'), ('kn_numeral', '0')]]]]]
    }

class KnTester(unittest.TestCase):

    def test_dict(self):
        for k in file_tree_dict:
            v = file_tree_dict[k]

            input_path = kn_engine.examples_path + k
            output_list = kn_engine.get_output_list(input_path)

            self.assertEqual(v, output_list)

if __name__ == '__main__':
    unittest.main()
    input('Key `Enter` to quit.' '\n')
