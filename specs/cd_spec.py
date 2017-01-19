import unittest
from items.item import Item
from items.cd import Cd

class TestCd(unittest.TestCase):
  def setUp(self):
    self.cd = Cd("Tea for the Tillerman", 17.32, "Cat Stevens", 11, 36)

  def test_is_item(self):
    self.assertIsInstance(self.cd, Item)

  def test_is_cd(self):
    self.assertIsInstance(self.cd, Cd)

  def test_has_name(self):
      self.assertEqual(self.cd.name, "Tea for the Tillerman")

  def test_has_price(self):
      self.assertEqual(self.cd.price, 17.32)

  def test_has_artist(self):
      self.assertEqual(self.cd.artist, "Cat Stevens")

  def test_has_tracks(self):
      self.assertEqual(self.cd.tracks, 11)

  def test_has_runtime(self):
      self.assertEqual(self.cd.runtime, 36)

  def test_set_name(self):
      self.cd.name = "Pinkerton"
      self.assertEqual(self.cd.name, "Pinkerton")

  def test_set_price(self):
      self.cd.price = 12.95
      self.assertEqual(self.cd.price, 12.95)

  def test_set_artist(self):
      self.cd.artist = "Weezer"
      self.assertEqual(self.cd.artist, "Weezer")

  def test_set_tracks(self):
      self.cd.tracks = 13
      self.assertEqual(self.cd.tracks, 13)

  def test_set_runtime(self):
      self.cd.runtime = 67
      self.assertEqual(self.cd.runtime, 67)
