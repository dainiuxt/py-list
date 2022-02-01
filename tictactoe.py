x = True
win = False
turn = 0
played_x = []
played_o = []
win_combinations = ["123", "456", "789", "147", "258", "369", "159", "357"]
grid = [1, 2, 3, 4, 5, 6, 7, 8, 9]

def get_playfield():
  playfield = f"\n{grid[0]} {grid[1]} {grid[2]}\n{grid[3]} {grid[4]} {grid[5]}\n{grid[6]} {grid[7]} {grid[8]}"
  print(f"{playfield}")
get_playfield()

def check_win(list):
  for combination in win_combinations:
    len = 0
    for c in combination:
      if c in ''.join(map(str, (sorted(list)))):
        len += 1
      if len == 3:
        return True

while win == False:
  turn += 1
  if x:
    symbol = "X"
    active = int(input("Select cell for X: "))
    if type(grid[active - 1]) is int:
      played_x.append(active)
      grid[active - 1] = symbol
      get_playfield()
      if check_win(played_x):
        print(f"{symbol} won!")
        win = True
      x = not x
    elif type(grid[active - 1]) is str:
      print("Choose another cell!")
  elif not x:
    symbol = "O"
    active = int(input("Select cell for O: "))
    if type(grid[active - 1]) is int:
      played_o.append(active)
      grid[active - 1] = symbol
      get_playfield()
      if check_win(played_o):
        print(f"{symbol} won!")
        win = True        
      x = not x
    elif type(grid[active - 1]) is str:
      print("Choose another cell!")
  if turn == 9 and win == False:
    print("It's a tie.")
    win = True
