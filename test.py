import sys
# Change the sys path to locate a Talk of the Town repository
PATH_TO_ANYTOWN = './talktown'
sys.path.append(PATH_TO_ANYTOWN)
# Now import from that Talk of the Town repository
from game import Game
import random
from song import songs
from business import Bar

"""GLOBAL VARS"""
DEBUG = True if raw_input('ENGAGE DEBUG MODE? ') in ('yes', 'y', 'yeah', 'ok', 'sure', 'lol yep') else False

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

def get_applicable_actionselectors(person, action_selectors):
  """Returns the action selectors that this person passes the preconditions for"""
  possible_selectors = []
  for action_selector in action_selectors:
    if action_selector.precondition(person):
      possible_selectors.append(action_selector)
  return possible_selectors

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

def display_bar_to_enter(bars):
  print '-----------------------------------------'
  for index, bar in enumerate(bars):
    print '{}: {}, {} people'.format(index, bar.name, len(bar.people_here_now))
  print '-----------------------------------------'

def display_intro_text():
  print '\n\n'
  print """You step into the bar. The walls are slightly peeling and smoke fills the air.
A person catches your eye"""
  print '\n\n'
  raw_input("\t\t\t\tPress enter to continue.  ")
  print '\n\n'

def display_jukebox_instructions():
  print '{INSTRUCTIONS ON HOW TO USE JUKEBOX}'
  print '\n\n'
  raw_input("\t\t\t\tPress enter to continue.  ")
  print '\n\n'

def display_songs():
  for index, song in enumerate(songs):
      print "{}: {}".format(index, song.name)

#Rig the generation of the city to always have 3 bars.
game = setup()
while len(game.city.businesses_of_type('Bar')) < 3:
  owner = game._determine_who_will_establish_new_business(business_type=Bar)
  Bar(owner=owner)

game.thought_productionist.debug = DEBUG

#Rig the city to have bars with 1,2 and 3 people, respectively.
num_people_in_bar = 1
for bar in game.city.businesses_of_type('Bar'):
  if len(bar.people_here_now) > num_people_in_bar:
    bar.people_here_now = list(bar.people_here_now)[:num_people_in_bar]
  while len(bar.people_here_now) < num_people_in_bar:
    game.random_person.go_to(bar)
  num_people_in_bar += 1

# Display demo title (unless debug mode is engaged)
if not DEBUG:
    display_title_screen()

#Allow the user to select the bar they want to enter.
bars = game.city.businesses_of_type('Bar')
display_bar_to_enter(bars)

#Handle users input for bar selection.
selection_index = int(raw_input('Select a bar to enter: '))
chosen_bar = bars[selection_index]

#Introduce the characters and the setting.
if not DEBUG: display_intro_text()

#Introduce instructions on how to play.
if not DEBUG: display_jukebox_instructions()

has_finished = False
while not has_finished:
  #Display the songs available to the user.
  display_songs()

  #Get the users choice of song.
  selection_index = int(raw_input('You chose: '))
  current_song = songs[selection_index]

  #Loop through song lyrics
  continue_song = True
  THINKER = None
  while continue_song:

    #Play the next section of the song, unless the song is over.
    try:
      current_song.play_next_section()

      #Everyone in the bar will consider the song lyrics.
      for person in chosen_bar.people_here_now:
        THINKER = person
        stimuli = person.mind.associate({'signals': [(current_song.current_theme, 1)]})
        thought = person.mind.elicit_thought(stimuli)
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

      #Allow the player to stop the song mid-play.
      cont = raw_input("Continue? (yes/no): ")
      if cont.lower() not in ("yes", 'y', 'ok', 'sure'): 
        continue_song = False
        current_song.stop()

    except StopIteration:
      continue_song = False

    if chosen_bar.people_here_now == 0:
      has_finished = True # Game Over.
