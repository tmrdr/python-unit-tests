import unittest
from items.item import Item
from items.digital_item import DigitalItem

class TestDigitalItem(unittest.TestCase):
  def setUp(self):
    self.digital_item = DigitalItem("wonderwall.mp3", .99)

  def test_is_item(self):
    self.assertIsInstance(self.digital_item, Item)

  def test_is_digital(self):
    self.assertIsInstance(self.digital_item, DigitalItem)

  def test_has_name(self):
      self.assertEqual(self.digital_item.name, "wonderwall.mp3")

  def test_has_price(self):
      self.assertEqual(self.digital_item.price, .99)

  def test_set_name(self):
      self.digital_item.name = "titanic.mov"
      self.assertEqual(self.digital_item.name, "titanic.mov")

  def test_set_price(self):
      self.digital_item.price = 249.99
      self.assertEqual(self.digital_item.price, 249.99)

  def test_can_sell_one(self):
      sold = self.digital_item.sell(1)
      self.assertTrue(sold)
      self.assertEqual(self.digital_item.quantity, 1)

  def test_can_sell_many(self):
      sold = self.digital_item.sell(4)
      self.assertTrue(sold)
      self.assertEqual(self.digital_item.quantity, 1)

  def test_can_sell_millions(self):
      # Python allows an underscore syntax in numbers to act like commas
      sold = self.digital_item.sell(4_000_000)
      self.assertTrue(sold)
      self.assertEqual(self.digital_item.quantity, 1)
