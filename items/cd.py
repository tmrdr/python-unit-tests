from .item import Item

class Cd(Item):
  def __init__(self, name, price, artist, tracks, runtime):
    super().__init__(name, price)
    self.artist = artist
    self.tracks = tracks
    self.runtime = runtime
