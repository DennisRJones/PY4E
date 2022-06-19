#get file from user and make sure its good
fh = input('Enter File: ')

if fh == 'quit':
    quit()

try:
    handle = open(fh)
except:
    print('File missing')
    quit()

#create a dictionary and insert tuples of words and their
#total count of appearences
di = {}
for line in handle:
    line = line.rstrip()
    words = line.split()
    for word in words:
        di[word] = di.get(word, 0) + 1

#Sort a list of tuples, switched to value key, and reverse
#order.

#print(di)
#print('SPACE')
x = sorted([(v,k) for k,v in di.items()], reverse = True)
#print(x)
#print(x[:10])
#print(type(x))

#print the top ten in key value order.
for v,k in x[:10]:
    print(k,v)
