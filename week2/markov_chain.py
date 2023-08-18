import random

def generate_sentence(start_token, filenames):
  # remove all newlines and split into words

  markov_model = {}

  for filename in filenames:
    with open(filename, 'r') as f:
      tokens = f.read().replace('\n', ' ').lower().split()
      for i in range(len(tokens) - 1):
        if tokens[i] not in markov_model:
          markov_model[tokens[i]] = []
        markov_model[tokens[i]].append(tokens[i+1])

  start_token = start_token.lower()

  # if "the" in markov_model:
  #   print(markov_model["the"])

  if start_token in markov_model:
    sentence = [start_token]
    next_word = random.choice(markov_model[start_token])

    can_continue = True
    while can_continue:
      sentence.append(next_word)

      if next_word in markov_model:
        next_word = random.choice(markov_model[next_word])
        # print(next_word)
      else:
        can_continue = False
        break
      
      if next_word == ".":
        can_continue = False
        sentence.append(next_word)
        break

      if len(sentence) >= 200:
        can_continue = False
        break

    return ' '.join(sentence)
  else:
    return ""


if __name__ == '__main__':
  # The random number generator is initialised to zero here purely
  # for your own testing so that each time you run your code during
  # development, you will get the same output. Remove this to get 
  # different output each time you run your code with the same input.
  random.seed(0)

  for i in range(4):
    print(generate_sentence('There', ['single.txt']))
  print('=' * 80)
  for i in range(4):
    print(generate_sentence('the', ['jab.txt']))
  print('=' * 80)
  for i in range(4):
    print(generate_sentence('It', ['dracula.txt', 'pandp.txt']))
  print('=' * 80)
  for i in range(10):
    print(generate_sentence('Once', ['dracula.txt', 'jb.txt', 'pandp.txt', 'totc.txt']))
  print('=' * 80)
  for i in range(8):
    print(generate_sentence('cat', ['single.txt', 'textwraps.txt']))