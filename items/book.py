from .item import Item

class Book(Item):
  def __init__(self, name, price, pages, author):
    super().__init__(name, price)
    self.pages = pages
    self.author = author
