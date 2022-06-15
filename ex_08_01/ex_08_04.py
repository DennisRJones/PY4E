elist = open('mbox-short.txt')
for line in elist:
    line = line.rstrip()
    words = line.split()
    #guardian
    if len(words) < 3 or words[0] != 'From':
        continue
    print(words[2])
