'''
import urllib.request, urllib.parse, urllib.error

hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
for line in hand:
    print(line.decode().strip())
'''
import urllib.request, urllib.parse, urllib.error

hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}
for line in hand:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)
