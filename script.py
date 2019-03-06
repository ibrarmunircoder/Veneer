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
      
class Client:
  def __init__(self, name, location, is_museum):
    self.name = name
    self.is_museum = is_museum
    if is_museum:
      self.location = location
    else:
      self.location = "Private Collection"
  
girl_with_mandolin = Art("Picasso, Pablo", "Girl with a Mandlin (Fanny Tellier)", "oil on canvas", 1910)

print(girl_with_mandolin)

veneer = Marketplace()
print(veneer.show_listings())

edytta = Client("Edytta  Halpirt", None, False)
moma = Client("The MOMA", "New York", True)
