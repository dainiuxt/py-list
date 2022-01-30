# First player is always "X"
x = True
win = False
turn = 0

# initialize and display game grid in console
cells = [1, 2, 3, 4, 5, 6, 7, 8, 9]
playfield = f"{cells[0]} {cells[1]} {cells[2]}\n{cells[3]} {cells[4]} {cells[5]}\n{cells[6]} {cells[7]} {cells[8]}\n"
print(f"{playfield}")

# played cells
played_x = []
played_o = []

# Winning combinations
win_combinations = ["123", "456", "789", "147", "258", "369", "159", "357"]

# The game
while win == False:
  active = int(input("Select cell: "))
  turn += 1
  if x:
    symbol = "X"
    if type(cells[active - 1]) is int:
      played_x.append(active)
      cells[active - 1] = symbol
      playfield = f"{cells[0]} {cells[1]} {cells[2]}\n{cells[3]} {cells[4]} {cells[5]}\n{cells[6]} {cells[7]} {cells[8]}\n"
      print(f"{playfield}")
      for combination in win_combinations:
        len = 0
        for c in combination:
          if c in ''.join(map(str, (sorted(played_x)))):
            len += 1
        if len == 3:
          win = True
          print(f"{symbol} won!")
      x = not x
    elif type(cells[active - 1]) is str:
      print("Choose another cell!")
  elif not x:
    symbol = "O"
    if type(cells[active - 1]) is int:
      played_o.append(active)
      cells[active - 1] = symbol
      playfield = f"{cells[0]} {cells[1]} {cells[2]}\n{cells[3]} {cells[4]} {cells[5]}\n{cells[6]} {cells[7]} {cells[8]}\n"
      print(f"{playfield}")
      for combination in win_combinations:
        len = 0
        for c in combination:
          if c in ''.join(map(str, (sorted(played_o)))):
            len += 1
        if len == 3:
          win = True
          print(f"{symbol} won!")        
      x = not x
    elif type(cells[active - 1]) is str:
      print("Choose another cell!")
  if win == False and turn == 9:
    print("It's a tie.")
