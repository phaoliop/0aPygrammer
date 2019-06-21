import unittest


def solve(s):
    print(s)
    c = [s.count(w) for w in list(set(s))]
    print(c)
    for i in range(len(c)):
        tmp = c.copy()
        tmp[i]-=1
        print(tmp)
        if len(list(filter(lambda x: x>0,list(set(tmp)))))==1: return True
    return False


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(True, False)

    def test_something(self):
        self.assertEqual(solve('aaaa'), True)

    def test_something(self):
        self.assertEqual(solve('abba'), False)

    def test_something2(self):
        self.assertEqual(solve('abbba'), True)

    def test_something3(self):
        self.assertEqual(solve('aabbcc'), False)

    def test_something4(self):
        self.assertEqual(solve('aaaabb'), False)

    def test_something5(self):
        self.assertEqual(solve('aabbccddd'), True)

    def test_something6(self):
        self.assertEqual(solve('aabcde'), True)

    def test_something7(self):
        self.assertEqual(solve('abcde'), True)

    def test_something8(self):
        self.assertEqual(solve('aaabcde'), False)

    def test_something9(self):
        self.assertEqual(solve('abbccc'), False)


if __name__ == '__main__':
    unittest.main()