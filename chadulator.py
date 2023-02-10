# chadulator

firstNum = int(input('First number: ')) 
operation = input('Enter operation(+, -, *, /): ')
secondNum = int(input('Second number: ')) 

if(operation == '+'):
    if(firstNum == 0 and secondNum == 0):
        print('0 + 0 = 0')

if(operation == '-'):
    if(firstNum == 0 and secondNum == 0):
        print('0 - 0 = 0')

if(operation == '*'):
    if(firstNum == 0 and secondNum == 0):
        print('0 * 0 = 0')

if(operation == '/'):
    if(firstNum == 0 and secondNum == 0):
        print('0 / 0 = Error')
