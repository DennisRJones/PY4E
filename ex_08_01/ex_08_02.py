print(list(range(4)))

friends = ['Joseph', 'Glenn', 'Sally']
print(len(friends))

print(list(range(len(friends))))

for i in range(len(friends)):
    print('Hello', friends[i])

for friend in friends:
    print('happy new year', friend)

for i in range(len(friends)):
    friend = friends[i]
    print('happy new year', friend)
