
import unittest

from eternal.main import calculate, main

"""
Run with PYTHONPATH=. python tests/test_dummy.py
"""


class TestDummy(unittest.TestCase):

    def test_fun(self):
        weekday = calculate(2001, 1, 3)
        self.assertEqual(weekday, 2005)

        retcode = main(("--year", "2001", "--month", "1", "--day", "3"))
        self.assertEqual(retcode, 0)

    def test_bad_day(self):
        try:
            weekday=calculate(2000,-4,12)
            self.assertTrue(False)
        except:
            pass
        try:
            weekday=calculate(1990,34,12)
            self.assertTrue(False)
        except:
            pass
        try:
            weekday=calculate(2006,'fas',12)
            self.assertTrue(False)
        except:
            pass

    def test_neg_month(self):
        try:
            weekday = calculate(2000, 4, 0)
            self.assertTrue(False)
        except:
            pass
        try:
            weekday = calculate(1990, 7, 13)
            self.assertTrue(False)
        except:
            pass
        try:
            weekday = calculate(2006, 23, 'fasf')
            self.assertTrue(False)
        except:
            pass



if __name__ == '__main__':
    unittest.main()
