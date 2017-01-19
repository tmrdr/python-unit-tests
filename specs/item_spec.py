import unittest
from items.item import Item

class TestItem(unittest.TestCase):
  def setUp(self):
    self.item = Item('Generic Item', 1.99)

  def test_is_item(self):
    self.assertIsInstance(self.item, Item)

  def test_has_name(self):
    self.assertEqual(self.item.name, 'Generic Item')

  def test_has_price(self):
    self.assertEqual(self.item.price, 1.99)

  def test_set_price(self):
    self.item.price = 1.50
    self.assertEqual(self.item.price, 1.50)

  def test_set_name(self):
    self.item.name = "Common Item"
    self.assertEqual(self.item.name, "Common Item")

  def test_can_sell(self):
    self.item.quantity = 6
    self.assertEqual(self.item.quantity, 6)

    sold = self.item.sell(5)
    self.assertTrue(sold)
    self.assertEqual(self.item.quantity, 1)

  def test_can_sell_to_zero(self):
    self.item.quantity = 6
    sold = self.item.sell(6)
    self.assertTrue(sold)
    self.assertEqual(self.item.quantity, 0)

  def test_no_sell_past_zero(self):
    self.item.quantity = 6
    sold = self.item.sell(7)
    self.assertFalse(sold)

    # quantity should be unaffected if the sale doesn't go through.
    self.assertEqual(self.item.quantity, 6)

  def test_no_sell_after_zero(self):
    self.item.quantity = 6
    first_sale = self.item.sell(6)
    self.assertTrue(first_sale)

    # quantity should go to zero.
    self.assertEqual(self.item.quantity, 0)

    # no more sales should be made.
    second_sale = self.item.sell(1)
    self.assertFalse(second_sale)

    # quantity should stay at zero.
    self.assertEqual(self.item.quantity, 0)

if __name__ == '__main__':
  unittest.main()
