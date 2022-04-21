from replit import clear
import random

a1,a2,a3,a4,a5,a6,a7,a8,a9,x = 1,2,3,4,5,6,7,8,9,False

def put(turn, chooser):
  global a1,a2,a3,a4,a5,a6,a7,a8,a9
  if chooser == 'player':
    if turn == 1 and a1 == 1:
      a1 = 'X'
    elif turn == 2 and a2 == 2:
      a2 = 'X'
    elif turn == 3 and a3 == 3:
      a3 = 'X'
    elif turn == 4 and a4 == 4:
      a4 = 'X'
    elif turn == 5 and a5 == 5:
      a5 = 'X'
    elif turn == 6 and a6 == 6:
      a6 = 'X'
    elif turn == 7 and a7 == 7:
      a7 = 'X'
    elif turn == 8 and a8 == 8:
      a8 = 'X'
    elif turn == 9 and a9 == 9:
      a9 = 'X'
    else:
      print('position is already taken, try another one!')
      get_turn('player')
  elif chooser == 'ai':
    if turn == 1 and a1 == 1:
      a1 = 'O'
    elif turn == 2 and a2 == 2:
      a2 = 'O'
    elif turn == 3 and a3 == 3:
      a3 = 'O'
    elif turn == 4 and a4 == 4:
      a4 = 'O'
    elif turn == 5 and a5 == 5:
      a5 = 'O'
    elif turn == 6 and a6 == 6:
      a6 = 'O'
    elif turn == 7 and a7 == 7:
      a7 = 'O'
    elif turn == 8 and a8 == 8:
      a8 = 'O'
    elif turn == 9 and a9 == 9:
      a9 = 'O'
    elif a1 in ('X', 'O') and a2 in ('X', 'O') and a3 in ('X', 'O') and a4 in ('X', 'O') and a5 in ('X', 'O') and a6 in ('X', 'O') and a7 in ('X', 'O') and a8 in ('X', 'O') and a9 in ('X', 'O') and len(check()) < 1:
      show_board()
      print('TIE')
      exit()
    else:
      get_turn('ai')


def get_turn(chooser):
  global x,a1,a2,a3,a4,a5,a6,a7,a8,a9
  if a1 in ('X', 'O') and a2 in ('X', 'O') and a3 in ('X', 'O') and a4 in ('X', 'O') and a5 in ('X', 'O') and a6 in ('X', 'O') and a7 in ('X', 'O') and a8 in ('X', 'O') and a9 in ('X', 'O') and len(check()) < 1:
    show_board()
    print('TIE')
    exit()  
  if chooser == 'player':
    try:
      turn = int(input('Where do you want to place: '))
      put(turn, 'player')
    except:
      print('Chose one of the numbers on the board!')
      get_turn()
  elif chooser == 'ai':
    try:
      put(random.randint(1,9), 'ai')
    except:
      if not x:
        x = True
        print('Congratulations, you won!')
        exit()


def show_board():
  clear()
  print(a1, "|", a2, "|", a3)
  print('--|---|--')
  print(a4, "|", a5, "|", a6)
  print('--|---|--')
  print(a7, "|", a8, "|", a9)


def check():
  global a1,a2,a3,a4,a5,a6,a7,a8
  if a1 == a2 == a3:
    if a1 == 'X':
     winner = 'player'
    elif a1 == 'O':
      winner = 'ai'
  elif a1 == a4 == a7:
    if a1 == 'X':
     winner = 'player'
    elif a1 == 'O':
      winner = 'ai'
  elif a7 == a8 == a9:
    if a7 == 'X':
     winner = 'player'
    elif a7 == 'O':
      winner = 'ai'    
  elif a9 == a6 == a3:
    if a9 == 'X':
     winner = 'player'
    elif a9 == 'O':
      winner = 'ai'  
  elif a3 == a2 == a1:
    if a1 == 'X':
     winner = 'player'
    elif a1 == 'O':
      winner = 'ai'  
  elif a1 == a5 == a9:
    if a1 == 'X':
     winner = 'player'
    elif a1 == 'O':
      winner = 'ai'  
  elif a7 == a5 == a3:
    if a7 == 'X':
     winner = 'player'
    elif a7 == 'O':
      winner = 'ai'
  elif a2 == a5 ==a8:
    if a2 == 'X':
      winner = 'player'
    elif a2 == 'O':
      winner = 'ai'
  else:
    winner = ''
  return(winner)

while check() == '':
  show_board()
  get_turn('player')
  get_turn('ai')

show_board()
if check() == 'player':
  print('Congratulations, you won')
if check() == 'ai':
  print('The computer won, better luck next time')
