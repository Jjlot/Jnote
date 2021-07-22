#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import unittest
from source.a_template import add_two


class TestCase(unittest.TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def eq3(self):
        ret = add_two(1, 2)
        self.assertEqual(ret, 3)

    def not_eq4(self):
        ret = add_two(2, 2)
        self.assertNotEqual(ret, 4)


if __name__ == '__main__':
    # suite = unittest.TestSuite()
    # suite.addTest(DatabaseTestCase('eq3'))

    suite = unittest.TestLoader().loadTestsFromTestCase(TestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
