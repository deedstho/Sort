import unittest
import sort
import time
import random

class TestTime(unittest.TestCase):

    random_numbers = []

    def setUp(self):
        # create random list
        random.seed()
        for number in range(0,20000):
            self.random_numbers.append(random.randint(1,100000))
        self.started_at = time.time()

    def tearDown(self):
        elapsed = time.time() - self.started_at
        print('{} ({}s)'.format(self.id(), round(elapsed, 2)))

    # insertion
    def test_random_insertion_sort(self):
        sortable = self.random_numbers
        sort.insertion_sort(sortable)

    # shell
    def test_random_shell_sort(self):
        sortable = self.random_numbers
        sort.shell_sort(sortable)

        

if __name__ == '__main__':
    unittest.main()