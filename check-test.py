win_combinations = ["123", "456", "789", "147", "258", "369", "159", "357"]
mylist = [8, 5, 3, 6, 7]

for combination in win_combinations:
  len = 0
  for c in combination:
  # print(combination)
    if c in ''.join(map(str, (sorted(mylist)))):
      len += 1
  if len == 3:
    win = True
  else:
    win = False

print(''.join(map(str, (sorted(mylist)))))
print(win)