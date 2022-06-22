'''
import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))

cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
mysock.send(cmd)

while True:
    data = mysock.recv(512)
    if (len(data) < 1):
        break
    print(data.decode(), end = '')
mysock.close()
'''
'''
import urllib.request, urllib.parse, urllib.error

hand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')

counts = {}
for line in hand:
    words = line.decode().split()
    print(line.decode().strip())
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)

maxWord = None
maxCount = None
for k,v in counts.items():
    if maxCount == None or maxCount < v:
        maxWord = k
        maxCount = v

print('Word used most: -', maxWord, '- It is used', maxCount, 'times.')
'''

import urllib.request, urllib.parse, urllib.error

hand = urllib.request.urlopen('http://www.dr-chuck.com/page1.htm')
for line in hand:
    print(line.decode().strip())
