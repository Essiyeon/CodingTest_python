string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
count = [0] * 26

for char in string:
  idx = alphabet.index(char)
  count[idx] += 1

print(*count)