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

Songs = [
  Song(id='A song of love and commitment', stanzas=(
      Stanza(
        lyrics=
"""We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy""",
        symbols=(('love', 10), ('relationship', 5), ('commitment', 10))
      ),
      Stanza(
        lyrics="""I just wanna tell you how I'm feeling
Gotta make you understand""",
        symbols=(('relationship', 5), ('honest', 5), ('love', 5))
      ),
      Stanza(
        lyrics="""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",
        symbols=(('relationship', 5), ('commitment', 10), ('love', 5))
      ),
      Stanza(
        lyrics="""We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it""",
        symbols=(('relationship', 2), ('commitment', 10), ('hidden love', 5))
      ),
      Stanza(
        lyrics="""And if you ask me how I'm feeling
Don't tell me you're too blind to see""",
        symbols=(('relationship', 2), ('denied love', 5))
      ),
      Stanza(
        lyrics="""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",
        symbols=(('relationship', 5), ('commitment', 10), ('love', 5))
      ),
      Stanza(
        lyrics="""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",
        symbols=(('relationship', 5), ('commitment', 10), ('love', 5))
      ),
      Stanza(
        lyrics="""(Ooh, give you up)
(Ooh, give you up)
Never gonna give, never gonna give
(Give you up)
Never gonna give, never gonna give
(Give you up)""",
        symbols=(('commitment', 10),)
      ),
      Stanza(
        lyrics="""We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it""",
        symbols=(('relationship', 2), ('commitment', 10), ('hidden love', 5))
      ),
      Stanza(
        lyrics="""I just wanna tell you how I'm feeling
Gotta make you understand""",
        symbols=(('relationship', 5), ('honest', 5), ('love', 5))
      ),
    )
  ),
]