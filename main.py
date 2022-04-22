from replit import clear
import random

a1,a2,a3,a4,a5,a6,a7,a8,a9,x = 1,2,3,4,5,6,7,8,9,False
print('Modes:\n1. Multiplayer\n2. AI')
mode = input('Chose a mode: ')
if mode in ('1', 'Multiplayer', 'multiplayer', 'MULTIPLAYER'):
  mode = 'multiplayer'
elif mode in ('2', 'Ai', 'ai', 'AI'):
  mode = 'ai'




def put(turn, chooser):
  global a1,a2,a3,a4,a5,a6,a7,a8,a9
  if turn == 1 and a1 == 1:
    a1 = chooser
  elif turn == 2 and a2 == 2:
    a2 = chooser
  elif turn == 3 and a3 == 3:
    a3 = chooser
  elif turn == 4 and a4 == 4:
    a4 = chooser
  elif turn == 5 and a5 == 5:
    a5 = chooser
  elif turn == 6 and a6 == 6:
    a6 = chooser
  elif turn == 7 and a7 == 7:
    a7 = chooser
  elif turn == 8 and a8 == 8:
    a8 = chooser
  elif turn == 9 and a9 == 9:
    a9 = chooser
  elif chooser == 'X':
    print('position is already taken, try another one!')
    get_turn(chooser)
  else:
    get_turn(chooser)



def get_turn(chooser):
  global x,a1,a2,a3,a4,a5,a6,a7,a8,a9
  if chooser == 'X':
    try:
      if mode == 'ai':
        put(int(input('Where do you want to place: ')), 'X')
      elif mode == 'multiplayer':
        put(int(input('Player 1, Where do you want to place: ')), 'X')
    except:
      print('Chose one of the numbers on the board!')
      get_turn()
  elif chooser == 'O':
    try:
      if mode == 'ai':
        put(random.randint(1,9), 'O')
      elif mode == 'multiplayer':
        put(int(input('Player 2, Where do you want to place: ')), 'O')
    except:
      if not x:
        x = True
        print('X won')
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
     winner = 'X'
    elif a1 == 'O':
      winner = 'O'
  elif a1 == a4 == a7:
    if a1 == 'X':
     winner = 'X'
    elif a1 == 'O':
      winner = 'O'
  elif a7 == a8 == a9:
    if a7 == 'X':
     winner = 'X'
    elif a7 == 'O':
      winner = 'O'    
  elif a9 == a6 == a3:
    if a9 == 'X':
     winner = 'X'
    elif a9 == 'O':
      winner = 'O'  
  elif a3 == a2 == a1:
    if a1 == 'X':
     winner = 'X'
    elif a1 == 'O':
      winner = 'O'  
  elif a1 == a5 == a9:
    if a1 == 'X':
     winner = 'X'
    elif a1 == 'O':
      winner = 'O'  
  elif a7 == a5 == a3:
    if a7 == 'X':
     winner = 'X'
    elif a7 == 'O':
      winner = 'O'
  elif a2 == a5 ==a8:
    if a2 == 'X':
      winner = 'X'
    elif a2 == 'O':
      winner = 'O'
  else:
    winner = ''
  return(winner)

def full():
  if a1 in ('X', 'O') and a2 in ('X', 'O') and a3 in ('X', 'O') and a4 in ('X', 'O') and a5 in ('X', 'O') and a6 in ('X', 'O') and a7 in ('X', 'O') and a8 in ('X', 'O') and a9 in ('X', 'O') and len(check()) < 1:
    return(True)
  else:
    return(False)


def play():
  global mode
  while check() == '' and not full():
    show_board()
    get_turn('X')
    if check() == '' and not full():
      show_board()
      get_turn('O')
    else:
      pass
  play()

try:
  play()
except:
  pass

show_board()
if check() == 'X':
  show_board()
  print('X won')
  exit()
if check() == 'O':
  show_board()
  print('O won')
  exit()
else:
  print('TIE')
  exit()



