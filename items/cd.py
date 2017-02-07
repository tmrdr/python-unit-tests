from .item import Item

class Cd(Item):
    def __init__(self, name, price, artist, tracks, runtime):
      super().__init__(name, price)
      self.tracks = tracks
      self.artist = artist
      self.runtime = runtime
