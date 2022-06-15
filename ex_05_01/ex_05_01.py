friends = ['Joseph', 'Glenn', 'Sally']

for friend in friends:
    print('Happy New Year:', friend)
print('Done!')

largeNum = None
print(largeNum)
for iterVar in [15, 5, 33, 78, 94, 20]:
    if largeNum == None or largeNum < iterVar:
        largeNum = iterVar
        print (largeNum)
    if iterVar > 10:
        print(iterVar, "is larger than 10.")
print(largeNum)
