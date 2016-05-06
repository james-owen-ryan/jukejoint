class Song(object):
  #stanzas= [ Stanza('never gonna give you up', (('up', 10), ('down', 10))) ]
  def __init__(self, id, stanzas):
    self.id = id
    self.stanzas = stanzas

  def __iter__(self):
    return iter(self.stanzas)

class Stanza(object):
  #lyrics= 'never gonna give you up, never gonna let you down'
  #symbols= ( ('up', 10), ('down', 10) )
  def __init__(self, lyrics, symbols):
    self.lyrics = lyrics
    self.symbols = symbols