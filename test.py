import sys
# Change the sys path to locate a Talk of the Town repository
PATH_TO_ANYTOWN = '../anytown'
sys.path.append(PATH_TO_ANYTOWN)
# Now import from that Talk of the Town repository
from game import Game
import random
from actionselector import Departure
from song import Song, Stanza, Songs


"""GLOBAL VARS"""
DEBUG = True if raw_input('ENGAGE DEBUG MODE? ') in ('yes', 'y', 'yeah', 'ok', 'sure', 'lol yep') else False
BAR_TYPES = ['Distillery', 'Bar', 'Tavern', 'Brewery']

ACTION_SELECTORS = [
  Departure(scale=(-5,0,5))
]

SONGS = Songs

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

""" Update TalkTown """
def entertain(self, artifact, provoked_by=None):
    """Influence symbol weightings from a given artifact.

    @param artifact: The artifact under consideration
    @param provoked_by: The person who provided the artifact, if any.
    """
    symbol_set = ()
    #consider the symbols on the recent thoughts (the train)
    #consider any dramatic weightings (allusions)
    #consider songs you've heard before (memory)
    #consider action selectors symbols
    symbol_set += update_symbol_weights(self, artifact.symbols, self.salient_action_selector.symbols)
    return symbol_set

def update_symbol_weights(self, artifact_symbols, other_symbols):
    """Given an artifact's symbols and some other set of symbols:
    1) If their are overlapping symbols, multiply their weights.
    2) If their are distinct symbols in either artifact_symbols or other_symbols, include these symbols.
    """
    symbol_set = ()
    symbol_names_in_both_sets = set([s[0] for s in artifact_symbols]) | set([s[0] for s in other_symbols])
    for symbol_name in symbol_names_in_both_sets:
        artifact_symbol = filter( lambda s: s[0] == symbol_name, artifact_symbols )
        other_symbol = filter( lambda s: s[0] == symbol_name, other_symbols )
        if artifact_symbol and other_symbol:
            symbol_set += ((symbol_name, artifact_symbol[0][1] * other_symbol[0][1]),)
        elif artifact_symbol:
            symbol_set += ((symbol_name, artifact_symbol[0][1]),)
        elif other_symbol:
            symbol_set += ((symbol_name, other_symbol[0][1]),)
    return symbol_set

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
    if person.salient_action_selector is not None:
      action_people.append(person)
  return action_people

def display_title_screen():
    """Display a title screen for the command-line version of this demo."""
    import time
    title = open('title.txt', 'r').readlines()
    print '\n\n'
    for line in title:
        time.sleep(0.075)
        sys.stdout.write(line)
    print '\n\n'
    raw_input("\t\t\t\tPress enter to begin.  ")
    print '\n\n'

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
game.thought_productionist.debug = DEBUG
# Display demo title (unless debug mode is engaged)
if not DEBUG:
    display_title_screen()
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
print "\n{} begins to play...\n".format(current_song.id)

#loop through song lyrics
song_stanzas = enumerate(current_song)
current_stanza = song_stanzas.next()[1]
continue_song = True
THINKER = None
while continue_song:
  print "{}\n".format(current_stanza.lyrics)
  #have npcs consider the symbols attached to this lyric
  for person in get_people_with_actionselectors(chosen_bar.people_here_now):
    THINKER = person
    stimuli = person.mind.associate(current_stanza)
    thought = person.mind.elicit_thought(stimuli)
    #TODO: add thought to person's train of thoughts.
    if thought:
        print "{person}: {thought} ({signals})".format(
            person=person.full_name,
            thought=thought.realize(),
            signals=", ".join(
                "{signal} ({weight})".format(signal=signal, weight=weight) for signal, weight in thought.signals.iteritems()
            )
        )
        thought.execute()
        person.mind.thoughts.append(thought)
    else:
        print "{person}: ...".format(person=person.full_name)
  try:
    current_stanza = song_stanzas.next()[1]
    cont = raw_input("Continue? (yes/no): ")
    if cont.lower() not in ("yes", 'y', 'ok', 'sure'): continue_song = False
  except StopIteration:
    continue_song = False
    print "No more lyrics"
