T = int(input())

for _ in range(T):
    case = input()
    add_O = 0
    store_O = 0
    for i in range(len(case)):
      if case[i] == 'O':
        add_O += 1
        store_O += add_O
      elif case[i] == 'X':
        add_O = 0
    print(store_O)