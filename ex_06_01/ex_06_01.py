str = 'X-DSPAM-Confidence: 0.8475 '

cPlace = str.find(':')

strNum = str[cPlace + 1:]


num = strNum.strip()

fNum = float(num)
print(num)
print(fNum)
