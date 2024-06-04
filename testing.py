import unittest
import math


class MyTestCase(unittest.TestCase):

    def test_sin(self):
        x = 45
        precision = 2
        result = round(math.sin(math.radians(x)), precision)
        self.assertEqual(result, 0.71)

    def test_cos(self):
        x = 60
        precision = 4
        result = round(math.cos(math.radians(x)), precision)
        self.assertEqual(result, 0.5)

    def test_tan(self):
        x = 60
        precision = abs(-8)
        result = round(math.tan(math.radians(x)), precision)
        self.assertEqual(result, 1.73205081)

    def test_cot(self):
        x = 35
        precision = abs(-5)
        result = round(1/math.tan(x), precision)
        self.assertEqual(result, 2.11053)

if __name__ == '__main__':
    unittest.main()
