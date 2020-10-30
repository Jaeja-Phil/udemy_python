board = [
  [' ',' ',' '],
  [' ',' ',' '],
  [' ',' ',' '],
]

players = {
  "one": "",
  "two": "",
}

player1 = "" 
player2 = ""

while len(player1) != 1 or len(player2) != 1:
  player1 = input('please enter a letter for player1: ')
  player2 = input('please enter a letter for player2: ')

players.one = player1
players.two = player2

def play_game:
  