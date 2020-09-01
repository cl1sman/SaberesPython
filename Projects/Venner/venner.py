class Marketplace:
  def __init__(self):
    self.listings = []

  def add_listing(self, new_listing):
    self.listings.append(new_listing)

  def remove_listing(self, new_listing):
    self.listings.remove(new_listing)

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
            self.location = 'Private Collection'
    
    def sell_artwork(self, artwork, price):
        if artwork.owner == self:
            new_listing = Listing(artwork, price, self)
            venner.add_listing(new_listing)
    
    def buy_artwork(self, artwork):
        if artwork.owner != self:
            art_listing = None
            for listing in venner.listings:
                if listing.art == artwork:
                    art_listing = listing
                    break
            if art_listing != None:
                art_listing.art.owner = self
                venner.remove_listing(art_listing)

class Art:
  def __init__(self, artist, title, medium, year, owner):
    self.artist = artist
    self.title = title
    self.medium = medium
    self.year = year
    self.owner = owner
  def __repr__(self):
    return '{artist}. {title}. {year}, {medium}, {name}, {location}'.format(artist=self.artist, title=self.title, year=self.year, medium=self.medium, name=self.owner.name, location=self.owner.location)

class Listing:
  def __init__(self, art, price, seller):
    self.art = art
    self.price = price
    self.seller = seller


  def __repr__(self):
      return '{art_title}, {price}'.format(art_title=self.art.title, price=self.price)


# print(Art('Monet, Claude','\"Vétheuil in the Fog\"', str(1879), 'oil on canvas'))

venner = Marketplace()


edytta = Client('Edytta Halpirt', None, False)
moma = Client('The MOMA', 'New York', True)

girl_with_mandolin = Art('Picasso, Pablo', '\"Girl with a Mandolin (Fanny Tellier)\"', str(1910), 'oil on canvas', edytta)
print(girl_with_mandolin)

edytta.sell_artwork(girl_with_mandolin, '$6M (USD)')

venner.show_listings()

moma.buy_artwork(girl_with_mandolin)
print(girl_with_mandolin)

venner.show_listings()