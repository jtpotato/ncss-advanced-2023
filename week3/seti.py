def alien2float(input_alien):
  lookup = ["a", "e", "i", "o", "u"]
  lookup_upper = ["A", "E", "I", "O", "U"]

  # check if input is valid
  for number in input_alien:
    if number not in lookup and number not in lookup_upper:
      return None

  is_integer = True
  decimal_index = 0

  for number in input_alien:
    if number in lookup:
      is_integer = False
      decimal_index = input_alien.index(number)
      break

  if decimal_index == 0 and is_integer == True:
    decimal_index = len(input_alien)

  whole_number = input_alien[:decimal_index]
  fractional_number = input_alien[decimal_index:]

  # print(whole_number, fractional_number)

  for number in whole_number:
    if number in lookup:
      return None
  
  for number in fractional_number:
    if number in lookup_upper:
      return None

  # reverse whole number
  whole_number = whole_number[::-1]

  decimal_whole_number = 0

  for i in range(len(whole_number)):
    if whole_number[i] in lookup_upper:
      decimal_whole_number += lookup_upper.index(whole_number[i]) * (5 ** i)

  # fractional number
  for i in range(len(fractional_number)):
    if fractional_number[i] in lookup:
      decimal_whole_number += lookup.index(fractional_number[i]) * (5 ** -(i+1))

  return decimal_whole_number


if __name__ == '__main__':
  # Run the examples in the question.
  print(repr(alien2float('IUae')))
  print(repr(alien2float('OUAooea')))
  print(repr(alien2float('iuAE')))
  print(repr(alien2float('IUA')))
  print(repr(alien2float('iua')))