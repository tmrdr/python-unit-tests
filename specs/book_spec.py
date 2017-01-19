import unittest
from items.item import Item
from items.book import Book

class TestBook(unittest.TestCase):
  def setUp(self):
    self.book = Book('Lord of the Rings', 7.99, 650, "JRR Tolkien")

  def test_is_item(self):
    self.assertIsInstance(self.book, Item)

  def test_is_book(self):
    self.assertIsInstance(self.book, Book)

  def test_has_name(self):
      self.assertEqual(self.book.name, "Lord of the Rings")

  def test_has_price(self):
      self.assertEqual(self.book.price, 7.99)

  def test_has_pages(self):
      self.assertEqual(self.book.pages, 650)

  def test_has_author(self):
      self.assertEqual(self.book.author, "JRR Tolkien")

  def test_set_name(self):
      self.book.name = "The Hobbit"
      self.assertEqual(self.book.name, "The Hobbit")

  def test_set_price(self):
      self.book.price = 12.95
      self.assertEqual(self.book.price, 12.95)

  def test_set_pages(self):
      self.book.pages = 999
      self.assertEqual(self.book.pages, 999)

  def test_set_author(self):
      self.book.author = "JK Rowling"
      self.assertEqual(self.book.author, "JK Rowling")
