#!/usr/bin/python3
import random
number = random.randint(-1000, 10000)
digit = abs(number) % 10
if number >= 0:
    last_digit = number % 10
else:
    last_digit = ((number * -1) % 10) * -1
display = "Last digit of %d is %d and is" % (number, last_digit)
if last_digit > 5:
    print(display, "greater than 5")
elif last_ digit == 0:
    print(display, "0")
else:
    print(display, "less than 6 and not 0")
