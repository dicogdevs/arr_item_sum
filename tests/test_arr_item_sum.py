import unittest
from arr_item_sum.arr_item_sum import arr_item_sum


class TestArrItemSum(unittest.TestCase):
    def test_empty_list(self):
        self.assertEqual(arr_item_sum([]), 0)

    def test_single_item(self):
        self.assertEqual(arr_item_sum([5]), 5)

    def test_multiple_items(self):
        self.assertEqual(arr_item_sum([1, 2, 3, 4, 5]), 15)

    # def test_negative_numbers(self):
    #   self.assertEqual(arr_item_sum([-1, -2, -3, -4, -5]), -15)

    # def test_mix_of_positive_and_negative_numbers(self):
    #    self.assertEqual(arr_item_sum([-1, 2, -3, 4, -5]), -3)


if __name__ == '__main__':
    unittest.main()
