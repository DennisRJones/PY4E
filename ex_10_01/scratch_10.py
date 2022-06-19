'''
d = {'a':10, 'c':22, 'b':1}
print(d.items())

tmp = []
for k,v in d.items():
    tmp.append((v,k))

print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)
'''
'''
#pull file
fhand = open('intro.txt')
#create dictionary
counts = {}
#fill dictionary with words in file
#acompanied with how many times they appear
for line in fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
#create list and
#fill it with touples with values before keys from dic
lst = []
for k,v in counts.items():
    ntup = (v,k)
    lst.append(ntup)
#sort in reverse order
lst = sorted(lst, reverse=True)
#print top ten listed words, key first
for v,k in lst[:10]:
    print(k, v)
'''

c = {'a':10, 'b':1, 'c':22}
sList = sorted([(v,k) for k,v in c.items()], reverse=True)
print(sList)
