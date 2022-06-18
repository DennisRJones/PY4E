'''
fileHandle = open('mbox-short.txt')
count = 0
for line in fileHandle:
    count = count + 1

print(count)

fileHandleTwo = open('mbox-short.txt')
fileRead = fileHandleTwo.read()
print(len(fileRead))

fileHandleSearch = open('mbox-short.txt')
for line in fileHandleSearch:
    if line.startswith('From:'):
        line = line.rstrip()
        print(line)

fileHandleEmail = open('mbox-short.txt')
for line in fileHandleEmail:
    line = line.rstrip()
    if not '@uct.ac.za' in line:
        continue
        print(line)

#test branching in git with save in scratch file

numList = []
while True:
    inp = input('Enter a number: ')
    if inp == 'done': break
    numList.append(float(inp))

print('Average', sum(numList)/len(numList))

fhand = open('mbox-short.txt')
for line in fhand:
    line = line.rstrip()
    if not line.startswith('From '): continue
    words = line.split()
    email = words[1]
    address = email.split('@')
    print(address[1])
'''

purse = {}
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
purse[2] = 5
print(purse)
purse[2] = purse[2] + 8
print(purse[2] - 1)
print(purse)

counts = {}
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
