mode = input('Enter math operation(+,-,*,/):')
num1 = float(input('Enter first number: '))
num2 = float(input('Enter second number'))
if mode == '+':
    print(f'Anwer is:{num1 + num2}')
elif mode == '-':
    print(f'Anwer is:{ num1- num2}')
elif mode == '*':
    print(f'Anwer is:{num1 * num2}')
elif mode == '/':
    print(f'Anwer is:{num1 / num2}')
else:
    print('Input Error!')




