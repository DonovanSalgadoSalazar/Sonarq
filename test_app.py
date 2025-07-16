 import unittest
from app import calculate_area

class TestArea(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(calculate_area(2), 12.56)

    def test_area_zero(self):
        self.assertEqual(calculate_area(0), 0)

    def test_area_negative(self):
        self.assertIsNone(calculate_area(-3))

if __name__ == '__main__':
    unittest.main()import unittest
from app import calculate_area

class TestArea(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(calculate_area(2), 12.56)

    def test_area_zero(self):
        self.assertEqual(calculate_area(0), 0)

    def test_area_negative(self):
        self.assertIsNone(calculate_area(-3))

if __name__ == '__main__':
    unittest.main()import unittest
from app import calculate_area

class TestArea(unittest.TestCase):
    def test_area_positive(self):
        self.assertEqual(calculate_area(2), 12.56)

    def test_area_zero(self):
        self.assertEqual(calculate_area(0), 0)

    def test_area_negative(self):
        self.assertIsNone(calculate_area(-3))

if __name__ == '__main__':
    unittest.main()
