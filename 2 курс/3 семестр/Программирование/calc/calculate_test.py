from calculate import *
import unittest

T_PARAMS = {'precision': 0.0001,
            'output_type': float,
            'possible_types': (int, float)
            }


class CalculateTest(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(calculate(1.5, 2.01, 3.003, '+', **T_PARAMS), 6.513)

    def test_mult(self):
        self.assertEqual(calculate(4.0, 4.0, 4.0, '*', **T_PARAMS), 64.0)

    def test_diff(self):
        self.assertEqual(calculate(15, 5, 3, '-', **T_PARAMS), 7.0)

    def test_div_1(self):
        self.assertIsNone(calculate(2.0, 9.0, 0, '/', **T_PARAMS))

    def test_div_2(self):
        self.assertEqual(calculate(12, 3, 2, '/', **T_PARAMS), 2.0)

    def test_power(self):
        self.assertEqual(calculate(2, 4, '^', **T_PARAMS), 16.0)

    def test_log(self):
        self.assertEqual(calculate(2, 4, 'log', **T_PARAMS), 0.5)


if __name__ == '__main__':
    unittest.main()
