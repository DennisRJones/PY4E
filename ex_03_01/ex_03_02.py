sHours = input('Enter Hours: ')
sRate = input('Enter Rate: ')
fHours = float(sHours)
fRate = float(sRate)
fPay = fHours * fRate

if fHours > 40:
    print('Pay: $', fPay)

    otHours = fHours - 40
    print('Overtime Hours:', otHours)

    otPay = otHours * fRate * .5
    print('Overtime Pay: $', otPay)
    print('Total Pay: $', otPay + fPay)

else:
    print('Pay: $', fPay)
