# read texts.txt to get a list of other text files to read.
with open("texts.txt", "r") as f:
    texts = f.read().strip().split("\n")
  
# read the other text files and store how many times words of length 1, 2, 3, etc appear.
word_lengths_all = {}
for text in texts:
    with open(text, "r") as f:
        word_lengths = {}
        words = f.read().split()
        for word in words:
            word = word.strip(",.?!-")
            if len(word) not in word_lengths:
                word_lengths[len(word)] = 0
            word_lengths[len(word)] += 1
        word_lengths_all[text] = word_lengths

print(word_lengths_all)

# read unknown.txt and calculate cosine similarity with other texts as read earlier.
with open("unknown.txt", "r") as f:
    unknown = f.read().split()
    unknown = [word.strip(",.?!-") for word in unknown]
    unknown = [word for word in unknown if word != ""]
    unknown = [word.lower() for word in unknown]
    