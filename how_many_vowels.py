def count_vowels(txt):
  i = 0
  for letter in txt.lower():
    if letter == 'a' or letter == 'e' or letter == 'i' or letter == 'o' or letter == 'u':
      i += 1
  return i
