class Art:
  def __init__(self, artist, title, medium, year):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    
  def __repr__(self):
    return "{0}. \"{1}\". {2}, {3}.".format(self.artist, self.title, self.year, self.medium)
  
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandlin (Fanny Tellier)", "oil on canvas", 1910)

print(girl_with_mandolin)
  
