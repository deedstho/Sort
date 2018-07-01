import unittest
import sort

class TestCaseInsertionSort(unittest.TestCase):

    def test_insert(self):
        test_list = [1,3,4,2]
        correct_list = [1,2,3,4]
        destination_index = 1
        source_index = 3
        sort.insert(test_list, destination_index, source_index)
        self.assertEqual(test_list, correct_list)

    def test_insert2(self):
        test_list2 = [1,3,4,2,7]
        correct_list2 = [1,2,3,4,7]
        destination_index2 = 1
        source_index2 = 3
        sort.insert(test_list2, destination_index2, source_index2)
        self.assertEqual(test_list2, correct_list2)

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