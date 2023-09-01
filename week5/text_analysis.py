# read texts.txt to get a list of other text files to read.
with open("texts.txt", "r") as f:
    texts = f.read().strip().split("\n")

# read the other text files and store how many times words of length 1, 2, 3, etc appear.
word_lengths_all = {}
for text in texts:
    with open(text, "r") as f:
        word_lengths = []
        words = f.read().split()
        # find longest word
        longest_word = 0
        for word in words:
            word = word.strip(",.?!-")
            if len(word) > longest_word:
                longest_word = len(word)
        # initialize word_lengths
        for i in range(longest_word):
            word_lengths.append(0)

        # word lists
        for word in words:
            word = word.strip(",.?!-")
            word_lengths[len(word) - 1] += 1
        word_lengths_all[text] = word_lengths

# read unknown.txt and calculate cosine similarity with other texts as read earlier.
with open("unknown.txt", "r") as f:
    unknown = f.read().split()
    # find longest word
    longest_word = 0
    for word in unknown:
        word = word.strip(",.?!-")
        if len(word) > longest_word:
            longest_word = len(word)
    # initialize word_lengths
    unknown_word_lengths = []
    for i in range(longest_word):
        unknown_word_lengths.append(0)

    # word lists
    for word in unknown:
        word = word.strip(",.?!-")
        unknown_word_lengths[len(word) - 1] += 1

import math


def dot_product(arr1, arr2):
    return sum(x * y for x, y in zip(arr1, arr2))


def norm(arr):
    return math.sqrt(sum(x ** 2 for x in arr))


def cosine_similarity(arr1, arr2):
    if len(arr1) != len(arr2):
        # pad with zeros
        if len(arr1) > len(arr2):
            arr2 += [0] * (len(arr1) - len(arr2))
        else:
            arr1 += [0] * (len(arr2) - len(arr1))

    dot_prod = dot_product(arr1, arr2)
    norm_prod = norm(arr1) * norm(arr2)

    if norm_prod == 0:
        return 0.0  # Handle zero division

    return dot_prod / norm_prod


# calculate cosine similarity
import math

cosine_similarities = {}
for text in texts:
    cosine_similarities[text] = cosine_similarity(
        word_lengths_all[text], unknown_word_lengths
    )

# sort by similarity, print results as {similarity} {filename}
sorted_similarities = sorted(cosine_similarities.items(), key=lambda x: x[1], reverse=True)
for text, similarity in sorted_similarities:
    print(f"{similarity} {text}")