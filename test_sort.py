import unittest
import sort

class TestCaseInsertionSort(unittest.TestCase):

    def test_insertion_sort(self):
        sortable = [1,3,5,2,4]
        sorted_list = [1,2,3,4,5]
        sort.insertion_sort(sortable)
        self.assertEqual(sortable, sorted_list)

    def test_gapped_insertion_sort1(self):
        sortable = [1,3,5,2,4]
        sorted_list = [1,2,3,4,5]
        gap = 1
        sort.gapped_insertion_sort(sortable, gap)
        self.assertEqual(sortable, sorted_list)

    def test_gapped_insertion_sort2(self):
        sortable = [1,3,5,2,4]
        sorted_list = [1,3,4,2,5]
        gap = 2
        sort.gapped_insertion_sort(sortable, gap)
        self.assertEqual(sortable, sorted_list)

    # gap larger than largest gap in list
    def test_gapped_insertion_sort5(self):
        sortable = [5,4,3,2,1]
        sorted_list = [5,4,3,2,1]
        gap = 5
        sort.gapped_insertion_sort(sortable, gap)
        self.assertEqual(sortable, sorted_list)

    def test_shell_sort(self):
        sortable = [1,3,5,2,4]
        sorted_list = [1,2,3,4,5]
        sort.shell_sort(sortable)
        self.assertEqual(sortable, sorted_list)

        

if __name__ == '__main__':
    unittest.main()