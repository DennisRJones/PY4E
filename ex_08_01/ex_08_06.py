#get file from user
handle = open(input('Enter file: '))

#turn words from file into dictionary and count (key, value)
counts = {}
for line in handle:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

#identify the word counted the most
mostWord = None
mostCount = None
for word,count in counts.items():
    if mostCount == None or mostCount < count:
        mostWord = word
        mostCount = count

print('Highest Counted Word in file is:', mostWord, mostCount)
