#chapter 11 notes
'''
hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if line.find('From:') >= 0:
        print(line)
'''
'''
import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('^From:', line):
        print(line)
'''
'''
import re
x = 'My 2 favorite numbers are 19 and 42'
#y = re.findall('[0-9]+', x)
#print(y)
#y = re.findall('[AEIOU]+', x)
#print(y)
y = re.findall('^M.+?e', x)
print(y)
'''
'''
import re
x = 'From: Using the : character'
y = re.findall('^F.+:', x)
print(y)
'''
'''
import re
x = 'From stephen.marqard@uct.ac.za stephen.marqard@uct.ac.za Sat Jan 5
09:14:16 2008'
y = re.findall('\S+@\S+', x)
print(y)
'''
'''
import re
hand = open('mbox-short.txt')
numlist = []
for line in hand:
    line = line.rstrip()
    stuff = re.findall('^X-DSPAM-Confidence: ([0-9.]+)', line)
    if len(stuff) != 1: continue
    num = float(stuff[0])
    numlist.append(num)
print('Maximum:', max(numlist))
'''
