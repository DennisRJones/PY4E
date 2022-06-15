#computing time and a half utilizing a function that takes param hours and rate

#function comuputing pay. includes pay for overtime at 1.5 pay
def computePay(hours, rate):
    pay = hours * rate
    if hours > 40:
        otHours = hours - 40
        otPay = otHours * rate * .5
        totalPay = otPay + pay
        return(totalPay)
    else:
        return(pay)

sHours = input('Enter Hours: ')
sRate = input('Enter Rate: ')
try:
    fHours = float(sHours)
    fRate = float(sRate)
except:
    print('Error, please enter numeric input')
    quit()

tPay = computePay(fHours, fRate)

print('Pay is: $', tPay)
