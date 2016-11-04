'''Unit-test.'''

############################################################

import unittest

import kn_engine

############################################################

paths_lists = {
    'demo.kn':
        [('check1', 'x^{2} - 2'), ('check2', '- x^{2} - 2')],
    'oneliner.kn':
        [('ch', '\\mathrm{True}')]
}

class KnTester(unittest.TestCase):
    def test_dict(self):
        for kn_path in paths_lists:
            check_list_man = paths_lists[kn_path]

            check_list_auto = kn_engine.write_output_files(
                'examples/' + kn_path,
                force=True, keep=True
            )

            self.assertEqual(
                check_list_man, check_list_auto
            )

if __name__ == '__main__':
    unittest.main()
