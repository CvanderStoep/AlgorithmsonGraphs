import unittest
import toposort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(toposort.dfs([[], [0], [1, 0], [2, 0], [1, 2]]), [4, 3, 2, 1, 0])  # 0-index based


if __name__ == '__main__':
    unittest.main()

