import cmath
import math

while True:
    x =  int(input('Enter Number:  '))

    result = math.factorial(x - 1) - x*(math.floor((math.factorial(x - 1)/x))) - x + 1

    print(result)

    if result == 0:
        print('Entered Number is Prime')
    else:
        print('Non-prime Number')
