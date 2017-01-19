from .item import Item

class Bluray(Item):
  def __init__(self, name, price, runtime, director):
    super().__init__(name, price)
    self.runtime = runtime
    self.director = director
