class Art:
  def __init__(self, artist, title, medium, year):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    
  def __repr__(self):
    return "{0}. \"{1}\". {2}, {3}.".format(self.artist, self.title, self.year, self.medium)
  
class Marketplace:
  def __init__(self):
    self.listings = []
    
  def add_listing(self, new_listing):
    self.listings.append(new_listing)
    
  def remove_listing(self, expired_listing):
    self.listings.pop(expired_listing)
    
  def show_listings(self):
    for listing in self.listings:
      print(listing)
  
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandlin (Fanny Tellier)", "oil on canvas", 1910)

print(girl_with_mandolin)

veneer = Marketplace()
print(veneer.show_listings())
