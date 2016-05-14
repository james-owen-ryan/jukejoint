class Song(object):
  #stanzas= [ Stanza('never gonna give you up', (('up', 10), ('down', 10))) ]
  def __init__(self, id, stanzas):
    self.id = id
    self.stanzas = stanzas

  def __iter__(self):
    return iter(self.stanzas)

class Stanza(object):
  #lyrics= 'never gonna give you up, never gonna let you down'
  #signals= ( ('up', 10), ('down', 10) )
  def __init__(self, lyrics, signals):
    self.lyrics = lyrics
    self.signals = signals

Songs = [
  Song(id='A song of love and commitment', stanzas=(
      Stanza(
        lyrics=
"""We're no strangers to love
You know the rules and so do I
A full commitment's what I'm thinking of
You wouldn't get this from any other guy""",
        signals=(('love', 1), ('relationship', 1), ('commitment', 1), ('man', 1))
      ),
      Stanza(
        lyrics="""I just wanna tell you how I'm feeling
Gotta make you understand""",
        signals=(('relationship', 1), ('honest', 1), ('love', 1))
      ),
      Stanza(
        lyrics="""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",
        signals=(('relationship', 1), ('commitment', 1), ('love', 1), ('lie', 1), ('leave', 1))
      ),
      Stanza(
        lyrics="""We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it""",
        signals=(('relationship', 1), ('commitment', 1), ('shy', 1), ('desire', 1))
      ),
      Stanza(
        lyrics="""And if you ask me how I'm feeling
Don't tell me you're too blind to see""",
        signals=(('relationship', 1), ('obvious', 1))
      ),
      Stanza(
        lyrics="""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",
        signals=(('relationship', 1), ('commitment', 1), ('love', 1), ('lie', 1), ('leave', 1))
      ),
      Stanza(
        lyrics="""Never gonna give you up
Never gonna let you down
Never gonna run around and desert you
Never gonna make you cry
Never gonna say goodbye
Never gonna tell a lie and hurt you""",
        signals=(('relationship', 1), ('commitment', 1), ('love', 1), ('lie', 1), ('leave', 1))
      ),
      Stanza(
        lyrics="""(Ooh, give you up)
(Ooh, give you up)
Never gonna give, never gonna give
(Give you up)
Never gonna give, never gonna give
(Give you up)""",
        signals=(('commitment', 2),)
      ),
      Stanza(
        lyrics="""We've known each other for so long
Your heart's been aching, but
You're too shy to say it
Inside, we both know what's been going on
We know the game and we're gonna play it""",
        signals=(('relationship', 1), ('commitment', 1), ('shy', 1), ('desire', 1))
      ),
      Stanza(
        lyrics="""I just wanna tell you how I'm feeling
Gotta make you understand""",
        signals=(('relationship', 1), ('honest', 1), ('love', 1))
      ),
    )
  ),
  Song(id='A coming of age song dealing with a youthful marriage and lost love', stanzas=(
      Stanza(
        lyrics="""I come from down in the valley
where mister when you're young
They bring you up to do like your daddy done
Me and Mary we met in high school
when she was just seventeen
We'd ride out of this valley down to where the fields were green""",
        signals=(('father', 1), ('relationship', 2), ('youth', 1), ('love', 2), ('home', 1), ('school', 1))
      ),
      Stanza(
        lyrics="""We'd go down to the river
And into the river we'd dive
Oh down to the river we'd ride""",
        signals=(('relationship', 1), ('youth', 1), ('love', 1))
      ),
      Stanza(
        lyrics="""Then I got Mary pregnant
and man that was all she wrote
And for my nineteenth birthday I got a union card and a wedding coat
We went down to the courthouse
and the judge put it all to rest
No wedding day smiles no walk down the aisle
No flowers no wedding dress""",
        signals=(('relationship', 2), ('relationship', 1), ('youth', 1), ('marriage', 2), ('children', 1))
      ),
      Stanza(
        lyrics="""That night we went down to the river
And into the river we'd dive
Oh down to the river we did ride""",
        signals=(('relationship', 1), ('youth', 1), ('love', 1))
      ),
      Stanza(
        lyrics="""But I remember us riding in my brother's car
Her body tan and wet down at the reservoir
At night on them banks I'd lie awake
And pull her close just to feel each breath she'd take
Now those memories come back to haunt me
they haunt me like a curse
Is a dream a lie if it don't come true
Or is it something worse
that sends me down to the river
though I know the river is dry
That sends me down to the river tonight
Down to the river
my baby and I
Oh down to the river we ride""",
        signals=(('brother', 1), ('remember', 2), ('memory', 2), ('bad memory', 2), ('lost love', 1),)
      )
    )
  ),
  Song(id='A song honoring the family of a coal miner', stanzas=(
      Stanza(
        lyrics="""Well, I was borned a coal miner's daughter
In a cabin, on a hill in Butcher Holler
We were poor but we had love,
That's the one thing that daddy made sure of
He shoveled coal to make a poor man's dollar""",
        signals=(('home', 1), ('low wage', 1), ('job', 1), ('youth', 1), ('father', 2), ('love', 2), ('family', 2), ('the mine', 1), ('poor', 1), ('daughter', 1),)
      ),
      Stanza(
        lyrics="""My daddy worked all night in the Van Lear coal mines
All day long in the field a hoin' corn
Mommy rocked the babies at night
And read the Bible by the coal oil light
And ever' thing would start all over come break of morn""",
        signals=(('home', 1), ('farm', 1), ('family', 2), ('child', 1), ('repetition', 1), ('work', 2), ('job', 1), ('youth', 1), ('father', 2), ('mother', 2), ('poor', 1))
      ),
      Stanza(
        lyrics="""Daddy loved and raised eight kids on a miner's pay
Mommy scrubbed our clothes on a washboard ever' day
Why I've seen her fingers bleed
To complain, there was no need
She'd smile in mommy's understanding way""",
        signals=(('home', 1), ('endurance', 2), ('family', 2), ('work', 2), ('job', 1), ('youth', 1), ('children', 1), ('father', 1), ('mother', 2), ('poor', 1))
      ),
      Stanza(
        lyrics="""In the summertime we didn't have shoes to wear
But in the wintertime we'd all get a brand new pair
From a mail order catalog
Money made from selling a hog
Daddy always managed to get the money somewhere""",
        signals=(('home', 1), ('farm', 1), ('family', 2), ('youth', 1), ('father', 1), ('poor', 1))
      ),
      Stanza(
        lyrics="""Yeah, I'm proud to be a coal miner's daughter
I remember well, the well where I drew water
The work we done was hard
At night we'd sleep 'cause we were tired
I never thought of ever leaving Butcher Holler""",
        signals=(('home', 2), ('life time', 1), ('farm', 1), ('job', 1), ('family', 2), ('youth', 1), ('father', 1), ('poor', 1), ('daughter', 1),)
      ),
      Stanza(
        lyrics="""Well a lot of things have changed since a way back then
And it's so good to be back home again
Not much left but the floor, nothing lives here anymore
Except the memory of a coal miner's daughter""",
        signals=(('home', 1), ('memory', 1), ('job', 1), ('family', 1), ('return', 3), ('daughter', 1), ('poor', 1))
      ),
    )
  ),
  Song(id="A song about finding one's way after a breakup", stanzas=(
      Stanza(
        lyrics="""So many times
Said it was forever
Said our love would always be true
Something in my heart always knew
I'd be lying here beside you
On my own
On my own
On my own""",
        signals=(('relationship', 1), ('alone', 2), ('foresight', 1), ('leave', 1), ('love', 1))
      ),
      Stanza(
        lyrics="""So many promises
Never should be spoken
Now I know what loving you cost
Now we're up to talking divorce
And we weren't even married
On my own
Once again now
One more time
By myself""",
        signals=(('relationship', 1), ('alone', 2), ('divorce', 1), ('marriage', 1), ('promise', 1), ('leave', 1))
      ),
      Stanza(
        lyrics="""No one said it was easy
But it once was so easy
Well I believed in love
Now here I stand
I wonder why""",
        signals=(('relationship', 1), ('alone', 2), ('love', 1), ('confusion', 1))
      ),
      Stanza(
        lyrics="""I'm on my own
Why did it end this way
On my own
This wasn't how it was supposed to be
On my own
I wish that we could do it all again""",
        signals=(('relationship', 1), ('alone', 2), ('confusion', 1), ('end', 1))
      ),
      Stanza(
        lyrics="""So many times
I know I should have told you
Losing you it cut like a knife
You walked out and there went my life
I don't want to live without you
On my own
On my own
On my own""",
        signals=(('relationship', 1), ('alone', 2), ('pain', 1), ('end', 1))
      ),
      Stanza(
        lyrics="""This wasn't how it was supposed to end
I wish that we could do it all again
I never dreamed I'd spend one night alone
On my own, I've got to find where I belong again
I've got to learn how to be strong again
I never dreamed I'd spend one night alone
By myself by myself""",
        signals=(('relationship', 1), ('alone', 1), ('end', 1), ('again', 2), ('endurance', 2))
      ),
      Stanza(
        lyrics="""I've got to find out what was mine again
My heart is saying that it's my time again
And I have faith that I will shine again
I have faith in me
On my own
On my own
On my own""",
        signals=(('relationship', 1), ('alone', 2), ('end', 1), ('again', 2), ('endurance', 2))
      ),
    )
  ),
]