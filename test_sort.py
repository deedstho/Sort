import unittest
import sort

class TestCaseInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        sortable = [1,3,5,2,4]
        sorted_list = [1,2,3,4,5]
        sort.insertion_sort(sortable)
        self.assertEqual(sortable, sorted_list)

    def test_range(self):
        self.assertEqual(  range(5, -1, -1) , [5, 4, 3, 2, 1, 0])

    def test_range2(self):
        self.assertEqual(  range(0, 5) , [0,1,2,3,4])

if __name__ == '__main__':
    unittest.main()