# Decrement test.

import unittest


class DecrementTest(unittest.TestCase):
    def testBasic(self):
        x = 2
        x--
        self.assertEqual(x, 1)
        x --
        self.assertEqual(x, 0)

    def test_in_loop(self):
        original_x = x = 2
        decrementation_number = 10
        START_FROM_INDEX_ONE = 1
        for i in range(START_FROM_INDEX_ONE, decrementation_number + START_FROM_INDEX_ONE):
            x--
            self.assertEqual(x, original_x - i)

    def test_backward_compatibility_for_plusplus_token(self):
        self.assertEqual(1--1, 2)
        self.assertEqual(1-- 1, 2)
        x = 2
        self.assertEqual(x--1, 3)
        self.assertEqual(x-- 1, 3)
        self.assertEqual(x--x, 4)
        self.assertEqual(--x, 2)


if __name__ == '__main__':
    unittest.main()
