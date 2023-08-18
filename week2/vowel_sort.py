def novowelsort(the_list):
  vowels = ['a', 'e', 'i', 'o', 'u']
  the_list.sort(key=lambda word: [char for char in word.lower() if char not in vowels])
  return the_list


if __name__ == '__main__':
  # Example calls to your function.
  print(novowelsort(['alpha', 'beta']))
  print(novowelsort(['once', 'upon', 'abc', 'time', 'there', 'were', 'some', 'words']))