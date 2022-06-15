counter = {}
names = ['jon', 'peter', 'scot', 'jon', 'peter']
for name in names:
    counter[name] = counter.get(name, 0) + 1
print(counter)
