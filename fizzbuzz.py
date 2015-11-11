# fizzbuzz

import sys

if len(sys.argv) > 1:
    try:
        n = int(sys.argv[1])
    except ValueError:
        print('Argument must be an integer, using n = 100')
        n = 100
else:    
    my_input = input('Please enter an integer: ')
    try:
        n = int(my_input)
    except ValueError:
        print('Argument must be an integer, using n = 100')
        n = 100

print('Fizz buzz counting up to %d' % n)

for i in range(0,n + 1):
    if (i % 3 == 0) & (i % 5 == 0):
        print('FizzBuzz')
    elif i % 3 == 0:
        print('Fizz')
    elif i % 5 == 0:
        print('Buzz')
    else:
        print(i)
        
        
    