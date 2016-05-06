import sys
# Change the sys path to locate a Talk of the Town repository
PATH_TO_ANYTOWN = '../anytown'
sys.path.append(PATH_TO_ANYTOWN)
# Now import from that Talk of the Town repository
from game import Game
import random
from actionselector import QuitJob
from song import Song, Stanza


"""GLOBAL VARS"""
BAR_TYPES = ['Distillery', 'Bar', 'Tavern', 'Brewery']

ACTION_SELECTORS = [
  QuitJob(scale=(-5,0,5))
]

SONGS = [
  Song(id='TEST SONG 1', stanzas=(
      Stanza(lyrics='Never gonna give you up', symbols=('up', 10)),
      Stanza(lyrics='Never gonna let you down', symbols=('down', 10))
    )
  )
]

THOUGHTS = [
  #Display text/Id, associated symbols, precondition, effects.
  ('I am feeling kinda up!', ['up'], lambda person: True, lambda person: True),
  ('I am feeling kinda down...', ['down'], lambda person: 'I am feeling kinda up!' in person.recent_thoughts, lambda person: True),
  ('I feel great!', ['posemo'], lambda person: True, lambda person: True)
]
THOUGHT_EFFECT_INDEX = 3
THOUGHT_ID_INDEX = 0
THOUGHT_PRECONDITION_INDEX = 2

""" IDEAS """
#Have jukeboxes be an object that Business' may optionally have.

#PEOPLE COULD SHOW UP WITH A.S. ALREADY. WE COULD RIG IT IN FOR DIFFICULTY/INTERESTING SITUATIONS.

#Run the symbol tagger over our own english text in the Thoughts as well. Otherwise, everytime I add a new symbol type I have to go
#over all my old thoughts and see if this new symbol should be attached to them as well.

""" TODOS """
#person.recent_thoughts is currently just the english text and not the actual Thought.

#make 'salient_action_selector' a property of person.py? Think about how action selectors will be handled by people. Will
#they just have one action selector they work on at a time? Multiple? Will some be foregrounded but others backgrounded?

#CHECK IF NPCs NOTICE THE SONG CHANGE, HAVE OPINIONS ABOUT THE SONG (have they encountered it before?!).

""" TalkTown Functions """
def boss(self):
    """Return the person who is this person's boss at their job, or None is this person has no job.
    Note that if a person owns the business, they are considered their own boss."""
    try:
      return self.occupation.company.owner.person if self.occupation else None
    except Exception as e:
      return None

def likes(self, person):
    threshold = ['somewhat high', 'high', 'very high', 'extremely high']
    try:
      return True if self.relationships[person].charge_str in threshold else False
    except Exception as e:
      return False

def dislikes(self, person):
    threshold = ['somewhat low', 'low', 'very low', 'extremely low']
    try:
      return True if self.relationships[person].charge_str in threshold else False
    except Exception as e:
      return False

""" FUNCTIONS """
def setup():
  game = Game()
  print "Simulating a town's history..."
  try:
      game.establish_setting()
  except KeyboardInterrupt:
      pass
  game.enact_no_fi_simulation()
  return game

def has_alcohol(city, bar_types):
  for bar_type in bar_types:
    if len(city.businesses_of_type(bar_type)) > 0:
      return True
  return False

def get_alcohol_businesses(city, bar_types):
  bars = []
  for bar_type in bar_types:
    for bar in city.businesses_of_type(bar_type):
      bars.append(bar)
  return bars

def get_applicable_actionselectors(person, action_selectors):
  """Returns the action selectors that this person passes the preconditions for"""
  possible_selectors = []
  for action_selector in action_selectors:
    if action_selector.precondition(person):
      possible_selectors.append(action_selector)
  return possible_selectors

def get_people_with_actionselectors(people):
  action_people = []
  for person in people:
    if hasattr(person, 'salient_action_selector'):
      action_people.append(person)
  return action_people

def generate_description_of_bar(bar):
  print '{DESCRIPTION OF BAR}'

def generate_description_of_people(people):
  print '{DESCRIPTION OF PEOPLE IN BAR}'

def generate_jukebox_instructions():
  print '{INSTRUCTIONS ON HOW TO USE JUKEBOX}'

def thought_from_symbols(person, symbols, thoughts):
  passable_thoughts = []
  for thought in thoughts:
    if thought[THOUGHT_PRECONDITION_INDEX](person):
      passable_thoughts.append(thought)
  return random.choice(passable_thoughts)

#Guarantee that the game will generate a city with a bar.
game = setup()
while has_alcohol(game.city, BAR_TYPES) is False:
  game = setup()

#Allow the user to select the bar they want to enter.
bars = get_alcohol_businesses(game.city, BAR_TYPES)
print '--Here are the bars available to enter--'
for index, bar in enumerate(bars):
  print '{}: {}, {} people'.format(index, bar.name, len(bar.people_here_now))
print '----------------------------------------'

#Handle users input for bar selection.
selection_index = int(raw_input('You chose: '))
selection_name = bars[selection_index].name
chosen_bar = game.find_co(selection_name)

#Give people in the bar action selectors.
for person in chosen_bar.people_here_now:
  possible_selectors = get_applicable_actionselectors(person, ACTION_SELECTORS)
  try:
    person.salient_action_selector = random.choice(possible_selectors)
  except IndexError: #no possible selectors are available to this person.
    person.salient_action_selector = None
  print '{} is debating about {}'.format(person.full_name, person.salient_action_selector)

#Generate and (eventually) display pre-game text to the user.
chosen_bar_description = generate_description_of_bar(chosen_bar)
people_description = generate_description_of_people(chosen_bar.people_here_now)
instructions = generate_jukebox_instructions()

#Display the songs to the user.
for index, song in enumerate(SONGS):
  print "{}: {}".format(index, song.id)

#Get the users choice of song.
selection_index = int(raw_input('You chose: '))
current_song = SONGS[selection_index]
#Inform user and NPCs that a new song is starting
print "{} begins to play...".format(current_song.id)

#loop through song lyrics
song_stanzas = enumerate(current_song)
current_stanza = song_stanzas.next()[1]
continue_song = True
while continue_song:
  print current_stanza.lyrics
  #have npcs consider the symbols attached to this lyric
  for person in get_people_with_actionselectors(chosen_bar.people_here_now):
    thought = thought_from_symbols(person, current_stanza.symbols, THOUGHTS)
    thought[THOUGHT_EFFECT_INDEX](person) #execute the effects of the thought
    person.recent_thoughts.append(thought[0])
    print "{}: {}".format(person.full_name, thought[THOUGHT_ID_INDEX])
  try:
    current_stanza = song_stanzas.next()[1]
    cont = raw_input("Continue? (yes/no): ")
    if cont != "yes": continue_song = False
  except StopIteration:
    continue_song = False
    print "No more lyrics"
