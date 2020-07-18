# isnt test.

import unittest


class IsntTest(unittest.TestCase):
    def testEquals(self):
        x = 2
        y = 2
        self.assertFalse(x isnt y)

    def testDiffers(self):
        x = 2
        y = 3
        self.assertTrue(x isnt y)


if __name__ == '__main__':
    unittest.main()
