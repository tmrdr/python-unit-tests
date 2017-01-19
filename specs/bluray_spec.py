import unittest
from items.item import Item
from items.bluray import Bluray

class TestBluray(unittest.TestCase):
  def setUp(self):
    self.bluray = Bluray("Rushmore", 9.99, 102, "Wes Anderson")

  def test_is_item(self):
    self.assertIsInstance(self.bluray, Item)

  def test_is_bluray(self):
    self.assertIsInstance(self.bluray, Bluray)

  def test_has_name(self):
    self.assertEqual(self.bluray.name, "Rushmore")

  def test_has_price(self):
    self.assertEqual(self.bluray.price, 9.99)

  def test_has_runtime(self):
    self.assertEqual(self.bluray.runtime, 102)

  def test_has_director(self):
    self.assertEqual(self.bluray.director, "Wes Anderson")

  def test_set_name(self):
    self.bluray.name = "Jurassic Park"
    self.assertEqual(self.bluray.name, "Jurassic Park")

  def test_set_price(self):
    self.bluray.price = 24.00
    self.assertEqual(self.bluray.price, 24.00)

  def test_set_runtime(self):
    self.bluray.runtime = 120
    self.assertEqual(self.bluray.runtime, 120)

  def test_set_director(self):
    self.bluray.director = "Steven Spielberg"
    self.assertEqual(self.bluray.director, "Steven Spielberg")

if __name__ == '__main__':
    unittest.main()
