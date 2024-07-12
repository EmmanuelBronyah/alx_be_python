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
  
  def test_subtraction(self):
    """Test the subtract method."""
    self.assertEqual(self.calc.subtraction(1, 1), 0)
    self.assertEqual(self.calc.subtraction(-1, 4), -5)
    self.assertEqual(self.calc.subtraction(-3, -1), -2)
  
  def test_multiplication(self):
    """Test the subtract method."""
    self.assertEqual(self.calc.multiplication(2, 2), 4)
    self.assertEqual(self.calc.multiplication(-2, 4), -8)
    self.assertEqual(self.calc.multiplication(-3, -1), 3)
  
  def test_division(self):
    """Test the subtract method."""
    self.assertEqual(self.calc.division(6, 3), 2)
    self.assertEqual(self.calc.division(-2, 4), -0.5)
    self.assertEqual(self.calc.division(-5, -1), 5)
    self.assertEqual(self.calc.division(7, 0), None)

if __name__ == "__main__":
  unittest.main()