def display(r1, r2, r3):
  print(r1)
  print(r2)
  print(r3)

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
row2[1] = 'x'

def user_choice():
  choice = ''
  acceptable_range = range(0,10)
  within_range = False

  while choice.isdigit() == False or within_range == False:
    choice = input('please enter a number (0-9): ')

    if choice.isdigit() == False:
      print('sorry not a digit')
      continue

    if int(choice) in acceptable_range:
      within_range = True

  return int(choice)

# user_choice()

game_list = [0,1,2]

def display_game(game_list):
  print('here is the current list: ')
  print(game_list)

def position_choice():
  choice = 'wrong'

  while choice not in ['0','1','2']:
    choice = input('Pick a position (0,1,2): ')

    if choice not in ['0','1','2']:
      print('sorry, invalid choice!')

  return int(choice)

def replacement_choice(game_list, position):

  user_placement = input('type a string to place at position: ')

  game_list[position] = user_placement
  
  return game_list

def gameon_choice():
  choice = 'wrong'

  while choice not in ['Y','N']:
    choice = input('keep playing? (Y or N): ')

    if choice not in ['Y', 'N']:
      print('sorry, invalid choice!')

  if choice == 'Y':
    return True
  else:
    return False

game_on = True
game_list = [0,1,2]

while game_on:
  display_game(game_list)
  position = position_choice()
  game_list = replacement_choice(game_list, position)
  display_game(game_list)

  game_on = gameon_choice()
  