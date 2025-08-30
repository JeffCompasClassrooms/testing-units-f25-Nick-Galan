import unittest
from circle import *  

class CircleTesting(unittest.TestCase):
    def test_radius_size_valid(self):
        c = Circle(1)
        self.assertEqual(c.setRadius(9), True)
        self.assertEqual(c.setRadius(45), True)
        self.assertEqual(c.setRadius(99), True)
        self.assertEqual(c.setRadius(23), True)

    def test_radius_size_neg(self):
        c = Circle(1)
        self.assertEqual(c.setRadius(-5), False)
        self.assertEqual(c.setRadius(-20), False)
        self.assertEqual(c.setRadius(-99), False)
        self.assertEqual(c.setRadius(-87347), False)

    def test_radius_size_zero(self):
        c = Circle(1)
        self.assertEqual(c.setRadius(0), True)

    def test_get_area(self):
        c = Circle(5)
        self.assertEqual(c.getArea(), 78.53981633974483)

        c = Circle(0)
        self.assertEqual(c.getArea(), 0)

        c = Circle(10)
        self.assertEqual(c.getArea(), 314.1592653589793)

    def test_get_circumference(self):
        c = Circle(5)
        self.assertEqual(c.getCircumference(), 31.41592653589793)

        c = Circle(10)
        self.assertEqual(c.getCircumference(), 62.83185307179586)

        c = Circle(0)
        self.assertEqual(c.getCircumference(), 0)

    
    def test_valid_radius_update(self):
        c = Circle(5)
        self.assertEqual(c.setRadius(10), True)
        self.assertEqual(c.getRadius(), 10)

    def test_invalid_radius_update(self):
        c = Circle(5)
        self.assertEqual(c.setRadius(-10), False)
        self.assertEqual(c.getRadius(), 5)

if __name__ == "__main__":
    unittest.main()
