from sort import quick_sort_1
from sort import buble_sort_1
from sort import buble_sort_2

import unittest


class Test_sort(unittest.TestCase):

    def test_sort(self):
        self.assertEqual(quick_sort_1.quick_sort(
            [8, 4, 3, 9, 6]), [3, 4, 6, 8, 9])

    def test_sort2(self):
        self.assertEqual(buble_sort_1.buble_sort(
            [8, 4, 3, 9, 6]), [3, 4, 6, 8, 9])

    def test_sort3(self):
        self.assertEqual(buble_sort_2.buble_sort(
            [8, 4, 3, 9, 6]), [3, 4, 6, 8, 9])


if __name__ == "__main__":
    unittest.main()
