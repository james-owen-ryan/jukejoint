import sys
import time
import datetime
# Change the sys path to locate a Talk of the Town repository
PATH_TO_ANYTOWN = '../anytown'
sys.path.append(PATH_TO_ANYTOWN)
# Now import from that Talk of the Town repository
from game import Game
from person import Person, PersonExNihilo
import random
from song import songs
from business import Bar

"""GLOBAL VARS"""
DEBUG = True if raw_input('ENGAGE DEBUG MODE? ').lower() in ('yes', 'y', 'yeah', 'ok', 'sure', 'lol yep') else False
THINKERS = set()

""" FUNCTIONS """
def setup():
  game = Game()
  # Set date of gameplay to 1987
  date_gameplay_begins = (1987, 10, 18)
  game.ordinal_date_that_gameplay_begins = ( datetime.date(*date_gameplay_begins).toordinal() )
  print "Simulating a town's history..."
  try:
      game.establish_setting()
  except KeyboardInterrupt:
      pass
  game.enact_no_fi_simulation()
  for person in game.city.residents:
      person.made_decision = False
  Person.make_decision = have_person_storm_out_of_bar
  PersonExNihilo.make_decision = have_person_storm_out_of_bar
  return game

def get_applicable_actionselectors(person, action_selectors):
  """Returns the action selectors that this person passes the preconditions for"""
  possible_selectors = []
  for action_selector in action_selectors:
    if action_selector.precondition(person):
      possible_selectors.append(action_selector)
  return possible_selectors

def display_opening_sequence():
    """Display a title screen for the command-line version of this demo."""
    import time
    title = open('title.txt', 'r').readlines()
    print '\n\n'
    for line in title:
        time.sleep(0.075)
        sys.stdout.write(line)
    print '\n\n'
    raw_input("\t\t\t\tPress enter to continue.  ")
    print '\n\n'

def display_bar_to_enter(bars):
  print '-----------------------------------------'
  for index, bar in enumerate(bars):
    print '\t\t\t\t{}: {}, {} people'.format(index, bar.name, len(bar.people_here_now))
  print '-----------------------------------------'

def display_intro_text():

    print '\t\t\t\t{}'.format(
        '-'*len("QUENCHING {}'S THIRST SINCE {}".format(chosen_bar.city.name.upper(), chosen_bar.founded))
    )
    print '\t\t\t\t{}'.format(
        '-' * len("QUENCHING {}'S THIRST SINCE {}".format(chosen_bar.city.name.upper(), chosen_bar.founded))
    )
    print '\t\t\t\t{bar_name}'.format(bar_name=chosen_bar.name.upper())
    print "\t\t\t\tQUENCHING {}'S THIRST SINCE {}".format(chosen_bar.city.name.upper(), chosen_bar.founded)
    print "\t\t\t\t\t\tCOLOR TV".format(chosen_bar.city.name, chosen_bar.founded)
    print "\t\t\t\t\t\tJUKEBOX".format(chosen_bar.city.name, chosen_bar.founded)
    print '\t\t\t\t{}'.format(
        '-' * len("QUENCHING {}'S THIRST SINCE {}".format(chosen_bar.city.name.upper(), chosen_bar.founded))
    )
    print '\t\t\t\t{}'.format(
        '-' * len("QUENCHING {}'S THIRST SINCE {}".format(chosen_bar.city.name.upper(), chosen_bar.founded))
    )
    raw_input('')
    raw_input("\n\t\t\t\tKrmmph.")
    raw_input("\n\n\t\t\t\tClick.")
    raw_input("\n\n\t\t\t\tClick.")
    raw_input('\n\n\t\t\t\t{person_in_bar}: "That machine\'s got a mind of its own!"'.format(
        person_in_bar=list(chosen_bar.people_here_now)[0].name
    ))
    raw_input("\n\n\t\t\t\tBzz.")
    raw_input('\n\n\t\t\t\t{person_in_bar}: "Maybe it\'s haunted."'.format(
        person_in_bar=(
            list(chosen_bar.people_here_now)[1].name if len(chosen_bar.people_here_now) > 1 else
            list(chosen_bar.people_here_now)[1].name
        )
    ))
    raw_input("\n\n\t\t\t\tClick.")
    raw_input("\n\n\t\t\t\tClick.")
    raw_input("\n\n\t\t\t\tPop.")
    raw_input('\n\n\t\t\t\t{person_in_bar}: "It\'s been playing songs all by itself!"'.format(
        person_in_bar=list(chosen_bar.people_here_now)[0].name
    ))
    raw_input("\n\n\t\t\t\tBzzzzzz.")
    INITIAL_THOUGHTS = [
        "You've got to come to a decision, {}. Do you stay here... or do you go?".format(
            list(chosen_bar.people_here_now)[0].first_name
        ),
        "I really need to figure this out, and figure it out now. I just don't know if I can leave this town."
    ]
    for i, person in enumerate(list(chosen_bar.people_here_now)):
        print "\t\t\t\t\n\n{}: ({})".format(
            person.name, INITIAL_THOUGHTS[i]
        )
        raw_input('')
    raw_input("\n\t\t\t\tBzzzzzzzzzzzzzzzzzzzzzzzzz.")
    raw_input("\n\n\t\t\t\tBzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.")
    print '\n\n'
    # raw_input("\t\t\t\tPress enter to continue.  ")
    # print '\n\n'

def display_closing_text():
    raw_input("\n\n\t\t\t\tClick.")
    raw_input("\n\n\t\t\t\tClick.")
    raw_input("\n\n\t\t\t\tPop.")
    raw_input("\n\n\t\t\t\tFIN")
    print "\n\n"

def display_jukebox_instructions():
  print '{INSTRUCTIONS ON HOW TO USE JUKEBOX}'
  print '\n\n'
  raw_input("\t\t\t\tPress enter to continue.  ")
  print '\n\n'

def display_songs():
  print '\n'
  for index, song in enumerate(songs):
      print "\t\t\t\t{}: {}".format(index, song.name)

def have_person_storm_out_of_bar(person):
    print '\n\n'
    print "\t\t\t\t{} storms out of the bar.".format(person.name)
    chosen_bar.people_here_now.remove(person)

#Rig the generation of the city to always have 3 bars.
game = setup()
while not game.city.businesses_of_type('Bar'):
  owner = game._determine_who_will_establish_new_business(business_type=Bar)
  Bar(owner=owner)

game.thought_productionist.debug = DEBUG

# #Rig the city to have bars with 1,2 and 3 people, respectively.
# num_people_in_bar = 1
# for bar in game.city.businesses_of_type('Bar'):
#   if len(bar.people_here_now) > num_people_in_bar:
#     bar.people_here_now = list(bar.people_here_now)[:num_people_in_bar]
#   while len(bar.people_here_now) < num_people_in_bar:
#     game.random_person.go_to(bar)
#   num_people_in_bar += 1

#Rig the city to have a bar with two people in it
num_people_to_target = 2
oldest_bar_in_town = min(game.city.businesses_of_type('Bar'), key=lambda b: b.founded)
if len(oldest_bar_in_town.people_here_now) > num_people_to_target:
    for person in list(oldest_bar_in_town.people_here_now)[num_people_to_target:]:
        person.go_to(person.home, 'home')
while len(oldest_bar_in_town.people_here_now) < num_people_to_target:
    adults_in_town = [p for p in game.city.residents if p.adult]
    random.choice(adults_in_town).go_to(oldest_bar_in_town, 'leisure')
chosen_bar = oldest_bar_in_town

# Display demo title (unless debug mode is engaged)
if not DEBUG:
    display_opening_sequence()

#Allow the user to select the bar they want to enter.
# bars = game.city.businesses_of_type('Bar')
# display_bar_to_enter(bars)

#Handle users input for bar selection.
# selection_index = int(raw_input('Select a bar to enter: '))
# chosen_bar = bars[1]  # FORCE TWO-PERSON BAR

#Introduce the characters and the setting.
if not DEBUG: display_intro_text()

#Introduce instructions on how to play.
# if not DEBUG: display_jukebox_instructions()

has_finished = False
while not has_finished:
  #Display the songs available to the user.
  display_songs()

  #Get the users choice of song.
  song_selected = False
  while not song_selected:
      try:
        selection_index = int(raw_input('\n\n\t\t\t\t'))
        current_song = songs[selection_index]
        song_selected = True
      except ValueError:
        pass

  #Loop through song lyrics
  continue_song = True
  THINKER = None
  while continue_song:

    #Play the next section of the song, unless the song is over.
    try:
      current_song.play_next_section()
      raw_input('')

      #Everyone in the bar will consider the song lyrics.
      for person in list(chosen_bar.people_here_now):
        THINKERS.add(person)
        THINKER = person
        stimuli = person.mind.associate(current_song)
        thought = person.mind.elicit_thought(stimuli)
        if thought:
            if DEBUG: 
              print "\n{person}: {thought} ({signals})\n".format(
                  person=person.full_name,
                  thought=thought.realize(),
                  signals=", ".join(
                      "{signal} ({weight})".format(signal=signal, weight=weight) for signal, weight in thought.signals.iteritems()
                  )
              )
            else:
              print "\n{person}: ({thought})".format(
                person=person.name,
                thought=thought.realize().lstrip()
              )
            thought.execute()
            person.mind.thoughts.append(thought)
            if person.made_decision:
                have_person_storm_out_of_bar(person=person)
        else:
            print "{person}: (...)".format(person=person.name)
        raw_input('')

      #Allow the player to stop the song mid-play.
      # print '\n'
      # raw_input("\t\t\t\tPress enter to continue.  ")
      # print '\n'

    except StopIteration:
      continue_song = False
      has_finished = True
      display_closing_text()

    # if chosen_bar.people_here_now == 0:
    #   has_finished = True # Game Over.


def replay():
    for p in THINKERS:
        print "{}\tDO: {}\tDON'T: {}".format(
            p.name,
            p.mind.receptors['do depart'].voltage if 'do depart' in p.mind.receptors else 0,
            p.mind.receptors["don't depart"].voltage if "don't depart" in p.mind.receptors else 0
        )
        for t in p.mind.thoughts:
            print '\t{}'.format(t.realize())
