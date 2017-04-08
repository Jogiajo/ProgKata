import unittest
from src import hst2_ remove_duplicates, hst2_isogram, hst2_longest, hst2_my_sort, hst2_power

class LabTestCase(unittest.TestCase):

    def test_isogram(self):
        self.assertEqual( ("abolishment", True),  is_isogram("abolishment"), msg=None)

    def test_longest(self):
        self.assertEqual("Andela", longest("This is Andela"), msg=None)

    def test_power(self):
        self.assertEqual(2, print (power(2, 3)), msg=None)

    def test_my_sort(self):
        self.assertEqual([1, 3, 5, 7, 9, 2, 4, 6, 8], my_sort([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]), msg=None)

    def test_remove_duplicates(self):
        self.assertEqual(('abc', 5), remove_duplicates('aaabbbac') , msg=None)

if __name__ == '__main__':
    unittest.main()