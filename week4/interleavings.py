def interleave(modified_a, modified_b, interleaved_string, interleavings_result):
  if len(modified_a) == 0:
    interleavings_result.append(interleaved_string + modified_b)
  elif len(modified_b) == 0:
    interleavings_result.append(interleaved_string + modified_a)
  else:
    interleave(modified_a[1:], modified_b, interleaved_string + modified_a[0], interleavings_result)
    interleave(modified_a, modified_b[1:], interleaved_string + modified_b[0], interleavings_result)

def interleavings(a, b):
  interleavings_result = []
  interleave(a, b, '', interleavings_result)

  # sort interleavings result
  interleavings_result.sort()

  return interleavings_result


if __name__ == '__main__':
  # Run the examples in the question.
  result = interleavings('ab', 'cd')
  print(result)
  result = interleavings('a', 'cd')
  print(interleavings('cd', 'ab'))
  print(result)