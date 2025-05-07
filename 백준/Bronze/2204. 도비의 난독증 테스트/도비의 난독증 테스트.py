while True:
  n = int(input())

  if n == 0:
    break;

  words = []
  lower_words = []
  for _ in range(n):
    words.append(input())
  # print(words)
  for word in words:
    lower_words.append(word.lower())
  # print(lower_words)
  first_word = min(lower_words)
  # print(first_word)
  index = lower_words.index(first_word)
  print(words[index])