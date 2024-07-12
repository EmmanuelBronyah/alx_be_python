import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
  
  def setUp(self):
    """Set up the SimpleCalculator instance before each test."""
    self.calc = SimpleCalculator()
  
  def test_addition(self):
    """Test the addition method."""
    self.assertEqual(self.calc.add(2, 3), 5)
    self.assertEqual(self.calc.add(-1, 1), 0)
    self.assertEqual(self.calc.add(-1, -1), -2)
  
  def test_subtract(self):
    """Test the subtract method."""
    self.assertEqual(self.calc.subtract(1, 1), 0)
    self.assertEqual(self.calc.subtract(-1, 4), -5)
    self.assertEqual(self.calc.subtract(-3, -1), -2)
  
  def test_multiply(self):
    """Test the subtract method."""
    self.assertEqual(self.calc.multiply(2, 2), 4)
    self.assertEqual(self.calc.multiply(-2, 4), -8)
    self.assertEqual(self.calc.multiply(-3, -1), 3)
  
  def test_divide(self):
    """Test the subtract method."""
    self.assertEqual(self.calc.divide(6, 3), 2)
    self.assertEqual(self.calc.divide(-2, 4), -0.5)
    self.assertEqual(self.calc.divide(-5, -1), 5)
    self.assertEqual(self.calc.divide(7, 0), None)

if __name__ == "__main__":
  unittest.main()