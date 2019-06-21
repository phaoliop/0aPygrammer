import unittest


def find_uniq(arr):
    tmp = list(set(arr))
    if (arr.count(tmp[0])) == 1:
        return tmp[0]
    else:
        return tmp[1]


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(find_uniq([1, 1, 1, 2, 1, 1]), 2)

    def test_something2(self):
        self.assertEqual(find_uniq([0, 0, 0.55, 0, 0]), 0.55)

    def test_something3(self):
        self.assertEqual(find_uniq([3, 10, 3, 3, 3]), 10)


if __name__ == '__main__':
    unittest.main()
