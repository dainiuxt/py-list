class MyGrid(list):
  def __contains__(self, type):
    for val in self:
      if isinstance(val, type):
        return True
    return False

cells = MyGrid([1, 2, 3, 4, 5, 6, 7, 8, 9])

playfield = f"{cells[0]} {cells[1]} {cells[2]}\n{cells[3]} {cells[4]} {cells[5]}\n{cells[6]} {cells[7]} {cells[8]}\n"
win_combinations = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]
played_x = []
played_o = []

x = True
print(playfield)

while not str in cells:
  active = int(input("Select cell: "))
  if x:
    symbol = "X"
    played_x.append(active)
    x = not x
  elif not x:
    symbol = "O"
    played_o.append(active)
    x = not x
  print(played_x)
  break

# print(symbol)
# print(play)
