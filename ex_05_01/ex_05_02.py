usrTotal = 0.0
count = 0

while True:
    usrInput = input('Enter a number: ')
    if usrInput == 'done':
        break
    try:
        fUsrInput = float(usrInput)
    except:
        print('bad data')
        continue

    usrTotal = usrTotal + fUsrInput
    count = count + 1

print(usrTotal, count, usrTotal/count)
