import unittest

def rgb(r, g, b):
    colors = [d if d<=255 else 255 for d in [w if w>=0 else 0 for w in (r,g,b)]]
    rpt = []
    for c in colors:
        c = str(hex(c)).split('x')[1]
        c = {1:'0'}.get(len(c),'') + c
        rpt.append(c.upper())
    return ''.join(rpt)

class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(rgb(0, 0, 0), "000000", "testing zero values")

    def test_something2(self):
        self.assertEqual(rgb(1, 2, 3), "010203", "testing near zero values")

    def test_something3(self):
        self.assertEqual(rgb(255, 255, 255), "FFFFFF", "testing max values")

    def test_something4(self):
        self.assertEqual(rgb(254, 253, 252), "FEFDFC", "testing near max values")

    def test_something5(self):
        self.assertEqual(rgb(-20, 275, 125), "00FF7D", "testing out of range values")


if __name__ == '__main__':
    unittest.main()