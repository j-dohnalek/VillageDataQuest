import unittest
from dataquest import Square, Point

class TestStringMethods(unittest.TestCase):

    def test_intersect_1(self):
        for i in range(5):
            a = Square(Point(3, 2))
            b = Square(Point(1+i, 0))
            print('{}-{}'.format(1+i, 0))
            self.assertFalse(a.intersects(b))

    def test_intersect_2(self):
        for i in range(5):
            a = Square(Point(3, 2))
            b = Square(Point(1+i, 4))
            print('{}-{}'.format(1+i, 0))
            self.assertFalse(a.intersects(b))


    def test_intersect_3(self):
        for i in range(5):
            a = Square(Point(3, 2))
            b = Square(Point(1, 0+i))
            print('{}-{}'.format(1, 0+i))
            self.assertFalse(a.intersects(b))

    def test_intersect_4(self):
        for i in range(5):
            a = Square(Point(3, 2))
            b = Square(Point(5, 0+i))
            print('{}-{}'.format(5, 0+i))
            self.assertFalse(a.intersects(b))


if __name__ == '__main__':
    unittest.main()